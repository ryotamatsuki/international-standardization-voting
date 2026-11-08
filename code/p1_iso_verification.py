"""Independent reproducibility checks for the 4-firm ISO-voting P1 model.
Run: python p1_iso_verification.py
Requires sympy. Exact demand uses a finite partition of the Salop circle.
This script provides checks; the accompanying argument establishes the parameter-interval lemma.
"""
import itertools
from fractions import Fraction
import sympy as sp

d = sp.symbols('d', positive=True, real=True)
w0,w1,w2,w3 = sp.symbols('w0 w1 w2 w3', real=True)
w = (w0,w1,w2,w3)
P = sp.Matrix([[sp.Integer(2) if i==j else (-sp.Rational(1,2) if (i-j)%4 in (1,3) else sp.Integer(0)) for j in range(4)] for i in range(4)])

def eq_and_welfare(qualities):
    a=list(qualities)
    rhs=sp.Matrix([1+a[i]-(a[(i-1)%4]+a[(i+1)%4])/2 for i in range(4)])
    prices=list(P.inv()*rhs)
    right=[sp.factor(sp.Rational(1,2) +(a[i]-prices[i]-a[(i+1)%4]+prices[(i+1)%4])/2) for i in range(4)]
    left=[sp.factor(1-right[(i-1)%4]) for i in range(4)]
    quantities=[sp.factor(left[i]+right[i]) for i in range(4)]
    CS=sp.factor(sum((a[i]-prices[i])*quantities[i]-(left[i]**3+right[i]**3)/3 for i in range(4)))
    profits=[sp.factor(prices[i]*quantities[i]) for i in range(4)]
    return prices, quantities, CS, profits

old=eq_and_welfare((2*d,2*d,2*d,0))
new=eq_and_welfare((3*d,3*d,3*d,3*d))
prices0, q0, cs0, pi0=old
prices1, q1, cs1, pi1=new
assert prices0==[1+d/3,1+d/6,1+d/3,1-5*d/6]
assert all(sp.simplify(z-1)==0 for z in prices1)
assert sp.simplify(cs1-cs0 - d*(216-13*d)/36)==0
assert sp.simplify(pi1[0]-pi0[0]+d*(d+6)/9)==0
assert sp.simplify(cs1-cs0+sum(pi1)-sum(pi0)-d*(216-47*d)/36)==0

# Each market has density n_i/4 and aggregate population N=1.
def welfare(i, state):
    _,_,CS, profits=state
    return sp.factor((w[i]*CS+profits[i])/4)

delta=[sp.factor(welfare(i,new)-welfare(i,old)) for i in range(4)]
assert sp.simplify(delta[0]-d*(w0*(216-13*d)-4*(d+6))/144)==0
assert sp.solve(delta[0].subs(w0,sp.Rational(12,100)),d) == [sp.Rational(48,139)]

# Nearest-neighbor comparison: all possible nonnegative price deviations,
# when 1/3 <= d <= 3/8, have demand max(0, 2*pstar-z).
# Exact demand over four unit intervals, clipping pairwise quadratic distance
# differences, which are affine on each interval.
def dist(x,j):
    r=abs(x-j)
    return min(r, 4-r)

def exact_demand(i,z,prices,qualities):
    pp=list(prices); pp[i]=float(z)
    aa=list(qualities)
    total=0.0
    for k in range(4):
        low,high=0.0,1.0
        for j in range(4):
            if i==j: continue
            left=(pp[i]-aa[i]+dist(k,i)**2)-(pp[j]-aa[j]+dist(k,j)**2)
            right=(pp[i]-aa[i]+dist(k+1,i)**2)-(pp[j]-aa[j]+dist(k+1,j)**2)
            slope=right-left
            if abs(slope)<1e-12:
                if left>1e-12: high=-1;break
            elif slope>0:
                high=min(high,-left/slope)
            else:
                low=max(low,-left/slope)
        total+=max(0,high-low)
    return total

for dd in (sp.Rational(1,3), sp.Rational(48,139), sp.Rational(3,8)):
    ps=[float(v.subs(d,dd)) for v in prices0]
    aa=[2*float(dd)]*3+[0.0]
    for i in range(4):
        for z in (0,.1,.4,ps[i],2*ps[i],3.,5.):
            numerical=exact_demand(i,z,ps,aa)
            theoretical=max(0,2*ps[i]-z)
            assert abs(numerical-theoretical)<1e-8, (dd,i,z,numerical,theoretical)

def profile_qualities(bits):
    standards=['S' if bits[i] else ('L' if i<3 else 'M') for i in range(4)]
    return tuple(d*(standards.count(standards[i])-1) for i in range(4))

legacy=(0,0,0,0)
all_new=(1,1,1,1)
for i in range(4):
    ddold=eq_and_welfare(profile_qualities(legacy))
    dev=list(legacy);dev[i]=1
    dddev=eq_and_welfare(profile_qualities(tuple(dev)))
    gain=sp.factor(welfare(i,dddev)-welfare(i,ddold))
    if i in (0,2):
        assert sp.simplify(gain + d*(w[i]*(576+34*d)+168+7*d)/576)==0
    elif i==3:
        assert gain==0
    assert float(gain.subs({d:sp.Rational(7,20),w[i]:sp.Rational(1,4)}))<=1e-10

    ddnew=eq_and_welfare(profile_qualities(all_new))
    dev=list(all_new);dev[i]=0
    ddd=eq_and_welfare(profile_qualities(tuple(dev)))
    stay_gain=sp.factor(welfare(i,ddnew)-welfare(i,ddd))
    assert sp.simplify(stay_gain-d*(w[i]*(216-13*d)+60-25*d)/144)==0
    assert float(stay_gain.subs({d:sp.Rational(7,20),w[i]:sp.Rational(1,4)}))>0

print('Independent symbolic identities: PASS')
print('Exact demand benchmark deviations: PASS')
print('All-new adoption is a strict NE with zero switching cost: PASS')
print('Status quo adoption is a weak NE (firm 3 indifferent): PASS')
print('Voting reversal: d* =',sp.Rational(48,139),'=',float(sp.Rational(48,139)))
print('Note: selection of a continuation equilibrium after ISO acceptance/rejection is NOT established by these checks.')
