"""P1-KS: K-country voting, four-firm production, quota and fractional ownership.
Exact symbolic coefficient certificates on beta in [1/10,1/2], h in [3/4,5/4].
This verifies *reduced selected-interior-FE-price* continuation outcomes only.
Run: python code/verify_ks_K_country_quota_20261109.py
"""
from math import comb
from itertools import product
import sympy as S
b,h,u,v=S.symbols("beta h u v")
R=S.Rational
A=12-5*b+4*b*h
J=24-9*b+4*b*h
E=24-21*b+4*b*b+(8*b*b-20*b)*h
prices=[A/(4*(3-b)),J/(8*(3-b)),A/(4*(3-b)),E/(8*(3-b))]
q=[(8-3*b)*A/(16*(3-b)*(2-b)),J/(8*(3-b)),
   (8-3*b)*A/(16*(3-b)*(2-b)),E/(4*(3-b)*(2-b))]
HM=S.Matrix([[1,1,1,0],[1,1,1,0],[1,1,1,0],[0,0,0,1]])
net=list(b*HM*(h*S.ones(4,1)+S.Matrix(q)/4))
right=[R(1,2)+(net[i]-prices[i]-net[(i+1)%4]+prices[(i+1)%4])/2
       for i in range(4)]
cs_old=sum((net[i]-prices[i])*q[i]-
           (right[i]**3+(1-right[(i-1)%4])**3)/3 for i in range(4))
D=S.factor((4*b*(4*h+1)-R(13,3)-cs_old)/4)
dpi=[S.factor(R(1,4)-prices[i]*q[i]/4) for i in range(4)]
kL=R(1,100)
tau_o=S.factor(-dpi[0]/D)
tau_c=S.factor(-dpi[1]/D)
world=S.factor(D+sum(dpi)-kL)
# The least possible aggregator population is 0.87.
aggregator_lower=S.factor(R(87,100)*D+dpi[1]+dpi[2]+dpi[3]-kL)

RECT=(R(1,10),R(1,2),R(3,4),R(5,4))
def bernstein_min(pol,rect):
    lo,hi,lowh,highh=rect
    z=S.Poly(S.expand(S.sympify(pol).subs(
        {b:lo+(hi-lo)*u,h:lowh+(highh-lowh)*v},simultaneous=True)),u,v)
    nx=z.degree(u);ny=z.degree(v)
    assert nx>=0 and ny>=0
    terms=dict(z.terms())
    return min(sum(val*R(comb(i,k),comb(nx,k))*R(comb(j,l),comb(ny,l))
                   for (k,l),val in terms.items() if k<=i and l<=j)
               for i in range(nx+1) for j in range(ny+1))

def certify_positive(expression,label,rect=RECT):
    num,den=S.fraction(S.cancel(expression))
    midpoint={b:(rect[0]+rect[1])/2,h:(rect[2]+rect[3])/2}
    assert expression.subs(midpoint)>0,(label,"midpoint")
    if den.subs(midpoint)<0:num,den=-num,-den
    assert bernstein_min(num,rect)>0,(label,"numerator")
    assert bernstein_min(den,rect)>0,(label,"denominator")
    print("CERTIFIED:",label)

def allocate(K,quota):
    """K national voters, four global firms. Each column of ownership sums to 1."""
    assert K>=2 and 2<=quota<=K
    blockers=K-quota+1
    remaining=quota-1
    epsilon=R(1,100) if remaining>1 else R(0)
    w=[R(3,25)/blockers]*blockers + [R(22,25)-epsilon]
    w += [epsilon/(remaining-1)]*(remaining-1) if remaining>1 else []
    omega=[[S.Integer(0) for _ in range(4)] for _ in range(K)]
    for i in range(blockers):omega[i][0]=R(1,blockers)
    for j in (1,2,3):omega[blockers][j]=S.Integer(1)
    assert len(w)==K and sum(w)==1 and all(x>0 for x in w)
    assert [sum(omega[i][j] for i in range(K)) for j in range(4)]==[1]*4
    return w,omega,blockers

def vote(K,quota,beta,installed_base):
    weights,ownership,r=allocate(K,quota)
    sub={b:beta,h:installed_base}
    d=D.subs(sub)
    changes=[z.subs(sub) for z in dpi]
    values=[S.factor(weights[i]*d+sum(ownership[i][j]*changes[j]
                    for j in range(4))-ownership[i][3]*kL)
            for i in range(K)]
    yes=sum(1 for x in values if x>0)
    assert sum(values)==world.subs(sub)
    return yes,values

if __name__=="__main__":
    certify_positive(D,"consumer surplus per person")
    certify_positive(world,"world net gains")
    certify_positive(aggregator_lower,"main positive voter")
    certify_positive(R(13,125)-tau_o.subs(b,R(1,10)),
                     "low-beta threshold below .104",
                     (R(1,10),R(1,10),R(3,4),R(5,4)))
    certify_positive(tau_o.subs(b,R(1,2))-R(1,8),
                     "high-beta threshold above .125",
                     (R(1,2),R(1,2),R(3,4),R(5,4)))
    certify_positive(R(3,50)-tau_c.subs(b,R(1,2)),
                     "central incumbent threshold below .06",
                     (R(1,2),R(1,2),R(3,4),R(5,4)))
    # Those 6 interval certificates + construction prove: for EVERY
    # K>=2 and 2<=q<=K, all voters support at beta=.1 and exactly
    # q-1 voters support at beta=.5, for EVERY h in [.75,1.25].
    for K,quota in [(2,2),(4,3),(5,4),(6,5),(8,6),(12,9),(20,15),(20,20)]:
        for installed in [R(3,4),R(1),R(5,4)]:
            low,_=vote(K,quota,R(1,10),installed)
            high,_=vote(K,quota,R(1,2),installed)
            assert low==K and high==quota-1
        print(f"K={K}, quota={quota}: yes-count {K}->{quota-1}; rejection at upper beta")
    for beta in [R(1,10),R(1,2)]:
        print("beta",beta,"world gain",world.subs({b:beta,h:1}),
              "outer threshold",tau_o.subs({b:beta,h:1}))
    print("WARNING: does NOT prove nonlocal Bertrand equilibrium or novelty.")
