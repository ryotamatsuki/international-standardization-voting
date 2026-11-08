"""P2 minimum extension: global pricing best-response proof and proposal scope.
Pure-pricing existence under weighted compatibility, four-country/firm Salop.
Exact SymPy interval certificates at d=1/3, x in [0,1].
DO NOT interpret unanimity as the actual ISO technical consensus procedure.
"""
from itertools import product
from sympy import (Matrix, eye, Rational as R, symbols, factor, Poly, binomial,
                   simplify, diff, solve)
x = symbols('x', real=True)
d=R(1,3)
L=Matrix([[1 if i==j else -R(1,2) if (i-j)%4 in (1,3) else 0
           for j in range(4)] for i in range(4)])
I=eye(4)
STATES=list(product((0,1),repeat=4))
O=(1,1,1,0);F=(1,1,1,1)
weights=[R(11,50),R(2,5),R(7,50),R(6,25)]
k=R(1,100)

def full_market(s):
    m=sum(s[:3])
    a=Matrix([d*s[i]*(m-1+x*s[3]) for i in range(3)]
             +[d*x*m*s[3]])
    p=[factor(t) for t in ((I+L).inv()*(Matrix([1]*4)+L*a))]
    r=[factor(R(1,2)+(a[i]-p[i]-a[(i+1)%4]+p[(i+1)%4])/2)
       for i in range(4)]
    le=[1-r[(i-1)%4] for i in range(4)]
    assert all(simplify(r[i]+le[i]-p[i])==0 for i in range(4))
    cs=factor(sum((a[i]-p[i])*p[i]-(r[i]**3+le[i]**3)/3
                  for i in range(4)))
    profit=[factor(z*z/4) for z in p]
    return a,p,r,le,cs,profit

def positive(expr,remove_zero_at_origin=False):
    v=factor(expr)
    if remove_zero_at_origin and v.subs(x,0)==0:
        v=factor(v/x)
    polynomial=Poly(v,x)
    n=polynomial.degree()
    c=polynomial.all_coeffs()[::-1]
    bernstein=[sum(c[k]*binomial(j,k)/binomial(n,k) for k in range(j+1))
               for j in range(n+1)]
    assert all(q>0 for q in bernstein),(v,bernstein)

def verify_pricing(market):
    n=0
    for state,(a,p,r,le,cs,profit) in market.items():
        for i in range(4):
            b=[factor(p[j]-a[j]) for j in range(4)]
            r0=r[i]+p[i]/2; le0=le[i]+p[i]/2
            # These conditions imply q_i(z)<=(2p_i-z)_+ for every z>=0:
            tests=[p[i],r[i],1-r[i],le[i],1-le[i],
                   r0,le0,R(3,2)-r0,R(3,2)-le0,
                   1-r0+le0,1-le0+r0,
                   2-b[(i+2)%4]-a[i],
                   b[(i+2)%4]-b[i]+4-4*r[i],
                   b[(i+2)%4]-b[i]+4-4*le[i]]
            for z in tests:
                assert Poly(factor(z),x).degree()<=1
                positive(z)
                n+=1
    assert n==896
    return n

def verify_adoption(market):
    strict=equal=0
    for state in STATES:
        for i in range(3):
            if state[i]:continue
            other=list(state);other[i]=1;other=tuple(other)
            gain=factor(market[other][-1][i]-market[state][-1][i])
            if gain==0:equal+=1
            else:
                positive(gain,True)
                strict+=1
    assert (strict,equal)==(21,3)
    entrant=factor(market[F][-1][3]-market[O][-1][3]-k*x*x)
    assert entrant==x*(301*x+3250)/32400
    positive(entrant,True)
    return strict,equal,entrant

def compare_costs(market,c0):
    _,_,_,_,cs0,pi0=market[O]
    _,_,_,_,cs1,pi1=market[F]
    dcs=factor(cs1-cs0)
    gains=[factor(weights[i]*dcs/4+pi1[i]-pi0[i]
                  -(k*x*x if i==3 else 0)
                  -(c0*x*x if i==0 else 0))
           for i in range(4)]
    assert all(positive(g,True) is None for g in gains[1:])
    positive(diff(gains[1],x))
    support=factor(gains[0]/x)
    cutoff=solve(support,x)[0]
    assert 0<cutoff<1
    world=factor(sum(gains))
    optimum=solve(diff(world,x),x)[0]
    assert 0<cutoff<optimum<1
    assert diff(world,x,2)<0
    print('c0=',c0,'country0 cutoff=',cutoff,'welfare optimum=',optimum,
          'majority proposer scope=1')
    print('country changes:',gains)
    for z in (cutoff,optimum,R(1)):
        print('scope',z,'world gain',factor(world.subs(x,z)),
              'decimal',float(world.subs(x,z)))
    return cutoff,optimum,world

if __name__=='__main__':
    markets={z:full_market(z) for z in STATES}
    print('PRICE GLOBAL BEST RESPONSE:',verify_pricing(markets),
          'strict endpoint-affine inequalities')
    print('ADOPTION:',verify_adoption(markets))
    xC,xW,W=compare_costs(markets,R(3,10))
    assert xC==R(2842,19097) and xW==R(6925,8869)
    assert simplify(W-x*(13850-8869*x)/32400)==0
    xC2,xW2,W2=compare_costs(markets,R(1,2))
    assert xC2==R(2842,32057) and xW2==R(6925,15349)
    assert W2.subs(x,1)<0<W2.subs(x,xC2)
    # No-go under sole entrant's cost and voluntary implementation.
    dd,kappa=symbols('dd kappa',positive=True)
    B=dd*(216-94*dd)/144
    C=47*dd*dd/144
    ae=5*dd*(12-10*dd)/144
    be=25*dd*dd/144
    lower=factor(B-2*ae+2*(C-be)*x)
    assert simplify(lower-dd*(96+6*dd+44*dd*x)/144)==0
    print('NO-GO: net social marginal gain >=',lower,
          'at every privately implementable scope x>0')
    print('PASS. NOTE: c0 unavoidable external adjustment cost not microfounded.')
