"""Independent exact SymPy verification of P1 with endogenous installed-base/network users.
Checks all 16 interior price candidates, adoption equilibria at endpoints, and exact
comparative static signs. IMPORTANT: no global nonlocal price-Nash proof is supplied.
Run: python code/verify_ks_userbase_vote_reversal_20261109.py
"""
from itertools import product
from sympy import (Matrix, eye, Rational as R, symbols, simplify, factor,
                   diff, cancel, fraction, Poly, binomial, expand, nroots)

b,t=symbols('b t', real=True)
L=Matrix([[1 if i==j else -R(1,2) if (i-j)%4 in (1,3) else 0
           for j in range(4)] for i in range(4)])
BASE=Matrix([1]*4)
STATES=list(product((0,1),repeat=4))
O=(1,1,1,0);F=(1,1,1,1);I=(0,0,0,0)
W=[R(3,25),R(1,2),R(3,25),R(13,50)]
KL=R(1,100);KH=R(2,5)

def evaluate(s,beta):
    group=['L' if s[i] else f'private_{i}' for i in range(4)]
    H=Matrix([[int(group[i]==group[j]) for j in range(4)] for i in range(4)])
    C=eye(4)-beta*L*H/4
    Cinv=C.inv();T=Cinv*L
    E=Matrix.diag(*[T[i,i] for i in range(4)])
    rhs=Matrix([1]*4)+beta*L*H*BASE
    p=(T+E).inv()*Cinv*rhs
    q=Cinv*(rhs-L*p)
    a=beta*H*(BASE+q/4)
    p=[factor(x) for x in p];q=[factor(x) for x in q];a=[factor(x) for x in a]
    right=[factor(R(1,2)+(a[i]-p[i]-a[(i+1)%4]+p[(i+1)%4])/2)
           for i in range(4)]
    left=[1-right[(i-1)%4] for i in range(4)]
    assert all(simplify(q[i]-right[i]-left[i])==0 for i in range(4))
    cs=factor(sum((a[i]-p[i])*q[i]-(right[i]**3+left[i]**3)/3
                  for i in range(4)))
    pi=[factor(p[i]*q[i]/4) for i in range(4)]
    return {'p':p,'q':q,'a':a,'right':right,'pi':pi,'cs':cs}

def is_ne(s,data,fee):
    for i in range(4):
        alt=list(s);alt[i]=1-alt[i];alt=tuple(alt)
        current=data[s]['pi'][i]-(fee if i==3 and s[3] else 0)
        deviated=data[alt]['pi'][i]-(fee if i==3 and alt[3] else 0)
        if deviated>current:return False
    return True

def bernstein_positive(f):
    num,den=fraction(cancel(f))
    assert den.subs(b,R(3,10))!=0
    sg=1 if den.subs(b,R(3,10))>0 else -1
    transformed=Poly(expand((sg*num).subs(b,R(1,10)+R(2,5)*t)),t)
    n=transformed.degree()
    coefs=[transformed.nth(k) for k in range(n+1)]
    bern=[sum(coefs[k]*binomial(j,k)/binomial(n,k)
              for k in range(j+1)) for j in range(n+1)]
    return all(v>0 for v in bern)

if __name__=='__main__':
    for beta in [R(1,10),R(1,2)]:
        data={s:evaluate(s,beta) for s in STATES}
        assert all(all(x>0 for x in z['p']) and
                   all(0<x<1 for x in z['right']) for z in data.values())
        reject=[s for s in STATES if is_ne(s,data,KH)]
        accept=[s for s in STATES if is_ne(s,data,KL)]
        assert reject==[I,O] and accept==[I,F]
        old=data[O];full=data[F]
        assert full['p']==[1]*4 and full['q']==[1]*4
        dcs=full['cs']-old['cs']
        dpi=[full['pi'][i]-old['pi'][i] for i in range(4)]
        dw=[factor(W[i]*dcs/4+dpi[i]-(KL if i==3 else 0))
            for i in range(4)]
        assert (all(z>0 for z in dw) if beta==R(1,10)
                else (dw[0]<0 and dw[1]>0 and dw[2]<0 and dw[3]>0))
        assert sum(dw)>0
        print('beta',beta,'prices(O)',old['p'],'demand(O)',old['q'])
        print('national welfare difference',[float(v) for v in dw],
              'world net gain',float(sum(dw)))
        print('adoption NE reject',reject,'approve',accept)
    old=evaluate(O,b);full=evaluate(F,b)
    dcs=factor(full['cs']-old['cs'])
    dpi=[factor(full['pi'][i]-old['pi'][i]) for i in range(4)]
    wstar=factor(-4*dpi[0]/dcs)
    delta0=factor(R(3,25)*dcs/4+dpi[0])
    roots=[z for z in nroots(fraction(cancel(delta0))[0],maxsteps=200)
           if abs(float(z.as_real_imag()[1]))<1e-10 and R(1,10)<float(z)<R(1,2)]
    assert len(roots)==1
    assert bernstein_positive(diff(wstar,b))
    assert bernstein_positive(dcs)
    assert bernstein_positive(dpi[3]-KL)
    assert bernstein_positive(KH-dpi[3])
    assert bernstein_positive(R(1,2)*dcs/4+dpi[1])
    assert bernstein_positive(R(13,50)*dcs/4+dpi[3]-KL)
    assert bernstein_positive(dcs/4+sum(dpi)-KL)
    for i in [0,1]:
        alt=list(O);alt[i]=0;alt=tuple(alt)
        assert bernstein_positive(old['pi'][i]-evaluate(alt,b)['pi'][i])
    print('critical beta',roots[0])
    print('country support population threshold:',wstar)
    print('PASS: exact identities and interval signs.')
    print('WARNING: global price best responses and all SPNE not proved.')
