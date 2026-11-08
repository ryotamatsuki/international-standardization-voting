"""Requires p2_unanimity_vs_majority_20261109.py in the same code/ directory.
Exact P2 cyber spillover, voluntary adoption cap, q=4 versus q=3, mitigation checks.
The imported code checks 896 pricing inequalities for all 16 adoption profiles.
"""
from sympy import Rational as R, symbols, factor, diff, solve, simplify, fraction, cancel
from p2_unanimity_vs_majority_20261109 import (
    x, STATES, O, F, weights, k, full_market, verify_pricing, verify_adoption)

markets={state: full_market(state) for state in STATES}
assert verify_pricing(markets)==896
assert verify_adoption(markets)[:2]==(21,3)
_,_,_,_,C_O,Pi_O=markets[O]
_,_,_,_,C_F,Pi_F=markets[F]
DC=factor(C_F-C_O)
DPI=[factor(Pi_F[i]-Pi_O[i]) for i in range(4)]

e=symbols('e',real=True)
attacker_payoff=x*e-R(10)*e*e/2
opt_effort=solve(diff(attacker_payoff,e),e)[0]
assert opt_effort==x/10 and diff(attacker_payoff,e,2)<0
P=factor(x*opt_effort)
assert P==x*x/10

D3=R(2)
entry=factor(DPI[3]-k*x*x-D3*P)
assert simplify(entry-x*(3250-6179*x)/32400)==0
xA=R(3250,6179)
assert entry.subs(x,xA/2)>0 and entry.subs(x,(1+xA)/2)<0

c=symbols('c',real=True)
W0=factor(weights[0]*DC/4+DPI[0]-c*x*x)
W1=factor(weights[1]*DC/4+DPI[1])
W2=factor(weights[2]*DC/4+DPI[2])
W3=factor(weights[3]*DC/4+DPI[3]-k*x*x-D3*P)
assert simplify(W3-x*(6982-6101*x)/32400)==0
assert all(z.subs(x,xA)>0 for z in [W1,W2,W3])
W=factor(W0+W1+W2+W3)
xU=R(2842)/(64800*c-343)
xW=R(6925)/(32400*c+5629)
assert simplify(W0.subs(x,xU))==0
assert simplify(diff(W,x).subs(x,xW))==0
assert all(diff(W,x,2).subs(c,v)<0 for v in [R(3,10),R(7,10)])

for cc in [R(3,10),R(7,10)]:
    xu=xU.subs(c,cc);xw=xW.subs(c,cc)
    assert 0<xu<xw<xA<1
    out=(W.subs({c:cc,x:xu}),W.subs({c:cc,x:xw}),W.subs({c:cc,x:xA}))
    print('c0',cc,'x (unanimity,social,3-of-4)',xu,xw,xA)
    print('welfare:',out,'decimals:',[float(z) for z in out])
    assert out[0]>0 and out[1]>out[0] and out[1]>out[2]
    if cc==R(3,10): assert out[2]>out[0]
    if cc==R(7,10): assert out[2]<0

# Exact rational-affine positivity of gaps for all c in [.3,.7].
for expression in [xW-xU,xA-xW]:
    numerator,denominator=fraction(cancel(expression))
    assert all(numerator.subs(c,z)>0 and denominator.subs(c,z)>0
               for z in [R(3,10),R(7,10)])

# Costly legacy-network retrofit: small cost F0=0.01 restores country0 Yes at cap.
gross0=factor(weights[0]*DC/4+DPI[0]).subs(x,xA)
assert gross0==R(11239865,458160492)
assert gross0-R(1,100)>0
assert R(1,100)<R(3,10)*xA*xA

# Alternative social accounting includes outsider hacker's surplus.
hacker_surplus=factor(attacker_payoff.subs(e,opt_effort))
assert hacker_surplus==x*x/20
for cc in [R(3,10),R(7,10)]:
    W_adding_actor=factor(W.subs(c,cc)+hacker_surplus)
    alt_opt=solve(diff(W_adding_actor,x),x)[0]
    assert 0<alt_opt<xA
    if cc==R(7,10): assert W_adding_actor.subs(x,xA)<0
print('PASS: attacker microfoundation, binding voluntary adoption and scope outcomes.')
