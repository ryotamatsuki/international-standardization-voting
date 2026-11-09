"""Exact Nash equilibrium, comparative statics and rational checks.
This is a minimal version-migration investment game, NOT an ISO theorem.
Requires SymPy. Run: python code/verify_version_migration_20261109.py
"""
import sympy as sp
b,L,T,g=sp.symbols("b L T g",real=True,positive=True)
r,y=sp.symbols("r y",real=True,nonnegative=True)
pi_L=L*b*r+g*b*r*y-r*r/2
pi_F=T*(1-b)*y+g*b*r*y-y*y/2
sol=sp.solve([sp.diff(pi_L,r),sp.diff(pi_F,y)],(r,y),dict=True)[0]
rstar=sp.factor(sol[r]); ystar=sp.factor(sol[y])
assert sp.simplify(rstar-(L*b+g*b*T*(1-b))/(1-g*g*b*b))==0
assert sp.simplify(ystar-(T*(1-b)+g*L*b*b)/(1-g*g*b*b))==0
assert sp.simplify(sp.diff(pi_L,r).subs({r:rstar,y:ystar}))==0
assert sp.simplify(sp.diff(pi_F,y).subs({r:rstar,y:ystar}))==0
assert sp.diff(pi_L,r,2)==-1 and sp.diff(pi_F,y,2)==-1
N=sp.factor(sp.diff(ystar,b)*(1-g*g*b*b)**2)
assert sp.simplify(N-(-T+2*g*L*b+2*T*g*g*b-T*g*g*b*b))==0
assert sp.simplify(N.subs(b,0)+T)==0
assert sp.simplify(N.subs(b,1)-(2*g*L-T*(1-g*g)))==0
assert sp.simplify(sp.diff(N,b)-(2*g*L+2*T*g*g*(1-b)))==0
assert sp.simplify(ystar.subs(b,0)-T)==0
assert sp.simplify(ystar.subs(b,1)-g*L/(1-g*g))==0
assert sp.simplify(ystar.subs(g,0)-T*(1-b))==0
pl0=sp.simplify(pi_L.subs({r:rstar,y:ystar},simultaneous=True).subs(b,0))
pf0=sp.simplify(pi_F.subs({r:rstar,y:ystar},simultaneous=True).subs(b,0))
pl1=sp.factor(pi_L.subs({r:rstar,y:ystar},simultaneous=True).subs(b,1))
pf1=sp.factor(pi_F.subs({r:rstar,y:ystar},simultaneous=True).subs(b,1))
assert pl0==0 and pf0==T*T/2
assert sp.simplify(pl1-L*L/(2*(1-g*g)**2))==0
assert sp.simplify(pf1-g*g*L*L/(2*(1-g*g)**2))==0
args={g:sp.Rational(1,2),L:2,T:1}
for bb in [sp.Rational(0),sp.Rational(1,4),sp.Rational(1,2),sp.Rational(3,4),sp.Rational(1)]:
    rr=sp.factor(rstar.subs(args).subs(b,bb))
    yy=sp.factor(ystar.subs(args).subs(b,bb))
    print('b=',bb,'legacy effort=',rr,'frontier effort=',yy,'bridge output=',sp.factor(bb*rr))
    assert rr>=0 and yy>=0
assert sp.factor(ystar.subs(args).subs(b,1))==sp.Rational(4,3)
assert sp.factor(ystar.subs(args).subs(b,0))==1
assert sp.factor(N.subs(args).subs(b,1))>0
print('r*(b)=',rstar)
print('y*(b)=',ystar)
print('dy/db numerator=',N)
print('binary producer profit b=0=',pl0+pf0,'b=1=',pl1+pf1)
print('PASS all exact symbolic first-order, uniqueness, comparative static and rational checks')
