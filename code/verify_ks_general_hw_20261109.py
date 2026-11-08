"""P1-KS: common installed base h, arbitrary country population shares.
Exact SymPy bivariate Bernstein sign certificates for beta in [1/10,1/2],
h in [3/4,5/4], with N=1, k_L=1/100 and k_H=2/5.
Results CONDITIONAL on selected interior FE price-FOC continuations.
This does not prove global Bertrand best responses or all-SPNE uniqueness.
Run: python code/verify_ks_general_hw_20261109.py
"""
from functools import lru_cache
from itertools import product
from math import comb
import sympy as S

B,H,U,V=S.symbols('beta h u v',real=True)
R=S.Rational
ONE=S.ones(4,1)
L=S.Matrix([[1 if i==j else -R(1,2) if (i-j)%4 in (1,3) else 0
             for j in range(4)] for i in range(4)])
LOWB,HIGHB=R(1,10),R(1,2)
LOWH,HIGHH=R(3,4),R(5,4)
O=(1,1,1,0);F=(1,1,1,1);I=(0,0,0,0)
STATES=list(product((0,1),repeat=4))
KLOW=R(1,100);KHIGH=R(2,5)

@lru_cache(None)
def evaluate(state):
    groups=['L' if state[i] else 'X'+str(i) for i in range(4)]
    adjacency=S.Matrix([[int(groups[i]==groups[j]) for j in range(4)]
                        for i in range(4)])
    C=S.eye(4)-B*L*adjacency/4
    T=C.inv()*L
    rhs=ONE+B*H*L*adjacency*ONE
    p=(T+S.diag(*[T[i,i] for i in range(4)])).inv()*C.inv()*rhs
    q=C.inv()*(rhs-L*p)
    a=B*adjacency*(H*ONE+q/4)
    p=[S.factor(z) for z in p]
    q=[S.factor(z) for z in q]
    a=[S.factor(z) for z in a]
    right=[S.factor(R(1,2)+(a[i]-p[i]-a[(i+1)%4]+p[(i+1)%4])/2)
           for i in range(4)]
    left=[1-right[(i-1)%4] for i in range(4)]
    for i in range(4):
        assert S.cancel(q[i]-left[i]-right[i])==0
    cs=S.factor(sum((a[i]-p[i])*q[i]-(left[i]**3+right[i]**3)/3
                    for i in range(4)))
    pi=[S.factor(p[i]*q[i]/4) for i in range(4)]
    return dict(p=p,q=q,a=a,right=right,pi=pi,cs=cs)

@lru_cache(None)
def bernstein_coefficients(poly, box):
    b0,b1,h0,h1=box
    pp=S.Poly(S.expand(S.sympify(poly).subs(
        {B:b0+(b1-b0)*U,H:h0+(h1-h0)*V},simultaneous=True)),U,V)
    n=pp.degree(U);m=pp.degree(V)
    if n<0 or m<0:return []
    terms=dict(pp.terms())
    return [sum(c*R(comb(i,k),comb(n,k))*R(comb(j,l),comb(m,l))
                for (k,l),c in terms.items() if k<=i and l<=j)
            for i in range(n+1) for j in range(m+1)]

def certify(expr,label,box=(LOWB,HIGHB,LOWH,HIGHH),depth=5):
    numerator,denominator=S.fraction(S.cancel(expr))
    center={B:(box[0]+box[1])/2,H:(box[2]+box[3])/2}
    val=S.cancel(expr).subs(center)
    if val<=0:raise AssertionError((label,'nonpositive at center',val))
    if denominator.subs(center)<0:
        numerator,denominator=-numerator,-denominator
    def recurse(pol,region,d):
        values=bernstein_coefficients(pol,region)
        if values and all(x>0 for x in values):return
        if d==0:raise AssertionError((label,'not certified',region,min(values)))
        a,z,e,f=region
        if z-a>=f-e:
            mid=(a+z)/2
            recurse(pol,(a,mid,e,f),d-1)
            recurse(pol,(mid,z,e,f),d-1)
        else:
            mid=(e+f)/2
            recurse(pol,(a,z,e,mid),d-1)
            recurse(pol,(a,z,mid,f),d-1)
    recurse(numerator,box,depth)
    recurse(denominator,box,depth)

def run():
    old=evaluate(O);full=evaluate(F)
    dcs=S.factor(full['cs']-old['cs'])
    dpi=[S.factor(full['pi'][i]-old['pi'][i]) for i in range(4)]
    tau_o=S.factor(-4*dpi[0]/dcs)
    tau_c=S.factor(-4*dpi[1]/dcs)
    assert S.factor(full['cs']-(4*B*(4*H+1)-R(13,3)))==0
    assert all(S.factor(full['p'][i]-1)==0 and
               S.factor(full['q'][i]-1)==0 for i in range(4))
    A=12-5*B+4*B*H
    J=24-9*B+4*B*H
    E=24-21*B+4*B**2+(8*B**2-20*B)*H
    checks=[(old['p'][0],A/(4*(3-B))),
            (old['q'][0],(8-3*B)*A/(16*(3-B)*(2-B))),
            (old['p'][1],J/(8*(3-B))),
            (old['q'][1],J/(8*(3-B))),
            (old['p'][3],E/(8*(3-B))),
            (old['q'][3],E/(4*(3-B)*(2-B)))]
    assert all(S.factor(x-y)==0 for x,y in checks)
    tests=[
      (dcs,'CS gain>0'),
      (S.diff(dcs,B),'CS gain increases'),
      (-dpi[0],'outer profit loss'),
      (-S.diff(dpi[0],B),'outer loss increases'),
      (-dpi[1],'central profit loss'),
      (dpi[3]-KLOW,'entrant join gain>kL'),
      (KHIGH-dpi[3],'entrant join gain<kH'),
      (S.diff(tau_o,B),'outer tau increases beta'),
      (S.diff(tau_c,B),'central tau increases beta'),
      (S.diff(tau_o,H),'outer tau increases h'),
      (R(1,2)*dcs/4+dpi[1],'central country yes'),
      (R(13,50)*dcs/4+dpi[3]-KLOW,'entrant country yes'),
      (dcs/4+sum(dpi)-KLOW,'world gain positive'),
      (S.diff(dcs/4+sum(dpi),B),'world gain increases'),
      (dcs/4+sum(dpi)-dpi[3],'world gross gain>join gain'),
    ]
    for expr,label in tests:certify(expr,label)
    print('PASS: 15 exact sign certificates throughout the beta/h rectangle')
    representatives=(I,(1,1,0,0),(1,0,1,0),O,F)
    n=0
    for st in representatives:
        zz=evaluate(st)
        for i in range(4):
            for expression in [zz['p'][i],zz['q'][i],zz['right'][i],
                               1-zz['right'][i]]:
                certify(expression,'price-demand regularity'+str((st,i,n)))
                n+=1
    print('PASS:',n,'regularity inequalities over 5 rotation classes (16 states)')
    positive=equal=0
    for st in STATES:
        for i in range(3):
            if st[i]:continue
            alt=list(st);alt[i]=1;alt=tuple(alt)
            gain=S.factor(evaluate(alt)['pi'][i]-evaluate(st)['pi'][i])
            if gain==0:equal+=1
            else:
                certify(gain,'incumbent adoption '+str((st,i)))
                positive+=1
    assert positive==21 and equal==3
    print('PASS: incumbent L adoption comparisons = 21 strictly positive, 3 zero')
    certify(R(13,125)-tau_o.subs(B,LOWB),'low beta tau<.104',
            (LOWB,LOWB,LOWH,HIGHH))
    certify(tau_o.subs(B,HIGHB)-R(1,8),'high beta tau>.125',
            (HIGHB,HIGHB,LOWH,HIGHH))
    certify(R(3,50)-tau_c.subs(B,HIGHB),'central tau high beta<.06',
            (HIGHB,HIGHB,LOWH,HIGHH))
    print('PASS: uniform population open set and vote reversal')
    for hh in [R(3,4),R(1),R(5,4)]:
        root=S.nsolve((tau_o-R(3,25)).subs(H,hh),B,R(7,20),prec=32)
        print('h',hh,'critical beta',root,
              'tau(.1)',S.N(tau_o.subs({B:LOWB,H:hh}),12),
              'tau(.5)',S.N(tau_o.subs({B:HIGHB,H:hh}),12))
    print('WARNING: no global nonlocal price-Nash theorem proved')

if __name__=='__main__':
    run()
