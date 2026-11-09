"""Exact diagnostic only; no nationally voted standard or price-market equilibrium.
Run: python code/verify_optional_profile_scope.py  (requires sympy)
Potential adopters: cost coefficient c~U[0,1]; payoff if implementing
s*(b+theta*a) - c*s**2, outside payoff zero.
"""
import sympy as sp
s,b,theta,V = sp.symbols('s b theta V', positive=True)
a_inner=b/(s-theta)
s0=b+theta
I_outer=s*a_inner**2
W_inner=V*s+s*(b+theta)-s**2/sp.Integer(2)
W_outer=sp.factor(V*I_outer+s*a_inner*(b+theta*a_inner)-s*s*a_inner*a_inner/sp.Integer(2))
assert sp.simplify(sp.diff(I_outer,s)+b*b*(s+theta)/(s-theta)**3)==0
assert sp.simplify(sp.diff(W_outer,s)+b*b*(V*(s+theta)+s*theta)/(s-theta)**3)==0
assert sp.simplify(W_inner.subs(s,s0)-W_outer.subs(s,s0))==0
assert sp.simplify(s0-I_outer.subs(s,s0))==0
print('a_partial:',a_inner)
print('I_partial:',sp.factor(I_outer))
print('dI_partial/ds:',sp.factor(sp.diff(I_outer,s)))
print('W_full:',sp.factor(W_inner))
print('W_partial:',W_outer)
print('dW_partial/ds:',sp.factor(sp.diff(W_outer,s)))
base={b:sp.Rational(1,4),theta:sp.Rational(1,4),V:1}
for ss in [sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Integer(1)]:
    aa=sp.Integer(1) if ss<=s0.subs(base) else sp.factor(a_inner.subs(base).subs(s,ss))
    II=sp.factor(ss*aa*aa)
    WW=sp.factor((W_inner if ss<=s0.subs(base) else W_outer).subs(base).subs(s,ss))
    print('s',ss,'adoption',aa,'pairwise',II,'social_welfare',WW)
    assert 0<aa<=1
assert sp.factor(I_outer.subs(base).subs(s,1))==sp.Rational(1,9)
assert sp.factor(W_outer.subs(base).subs(s,1))==sp.Rational(1,6)
assert sp.factor(W_inner.subs(base).subs(s,sp.Rational(1,2)))==sp.Rational(5,8)
# General differentiable F with density f(z). Stable interior fixed point.
a,fx,z=sp.symbols('a fx z',positive=True)
da=-fx*z/(s-theta*fx)
dI=sp.factor(a*a+2*s*a*da)
assert sp.simplify(dI-a*a*(1-(2*z*fx/a)/(1-theta*fx/s)))==0
# With theta=0, negative effective-interoperability derivative still occurs.
assert sp.simplify(sp.diff(I_outer.subs(theta,0),s)+b*b/s**2)==0
print('PASS: exact algebra, 4 rational scenarios, general-F elasticity, theta=0 ablation')
