"""Gate 4: exact symbolic verification of FDIS voting and costly technical objections.
All negative ballots are assumed to contain legitimate technical comments.
This is a regression suite, not machine-checked proof of the economic game.
"""
from itertools import product
import sympy as s

N,d=s.symbols('N d',positive=True)
w0,w2,lam0,lam2=s.symbols('w0 w2 lam0 lam2',positive=True)
c0,c2=s.symbols('c0 c2',positive=True)

def loss(w,lam):
    return s.factor(N*d*(4*lam*(d+6)-w*(216-13*d))/144)

L0=loss(w0,lam0)
L2=loss(w2,lam2)
assert s.simplify(L0-N*d*((4*lam0+13*w0)*d+24*lam0-216*w0)/144)==0
for w,lam,c,L in [(w0,lam0,c0,L0),(w2,lam2,c2,L2)]:
    a=4*lam+13*w
    b=24*lam-216*w
    doc_threshold=(-b+s.sqrt(b*b+576*a*c/N))/(2*a)
    assert s.simplify(L.subs(d,doc_threshold)-c)==0
    assert s.simplify(s.diff(L,d)-N/144*(2*a*d+b))==0

def fdis_pass(ballots):
    Y=ballots.count('Y')
    B=ballots.count('N') # all N must include technical comments
    cast=Y+B
    return cast>0 and 3*Y>=2*cast and 4*B<=cast

for ballots in product('YNA',repeat=4):
    Y=ballots.count('Y');B=ballots.count('N')
    assert fdis_pass(ballots)==(Y+B>0 and Y>=3*B),ballots

for ballots,approved in [('YYYY',True),('YYYN',True),('YYNN',False),
                         ('YYNA',False),('YYAA',True)]:
    assert fdis_pass(tuple(ballots))==approved

# Country 1 and 3 vote Yes; countries 0 and 2 can abstain or file No.
def payoffs(a0,a2,L0,L2,c0,c2):
    approved=fdis_pass(('Y',a0,a2,'Y'))
    return (-(L0 if approved else 0)-(c0 if a0=='N' else 0),
            -(L2 if approved else 0)-(c2 if a2=='N' else 0))

example={(a,b):payoffs(a,b,s.Rational(5),s.Rational(5),
                        s.Rational(1),s.Rational(1))
         for a,b in product('AN',repeat=2)}
nash=[]
for (a,b),pay in example.items():
    alt0=('N' if a=='A' else 'A',b)
    alt2=(a,'N' if b=='A' else 'A')
    if pay[0]>=example[alt0][0] and pay[1]>=example[alt2][1]:
        nash.append((a,b))
assert set(nash)=={('N','A'),('A','N')}

p0=1-c2/L2
p2=1-c0/L0
assert s.simplify(-c0+(1-p2)*L0)==0
assert s.simplify(-c2+(1-p0)*L2)==0
Ppass=s.factor((1-p0)*(1-p2))
assert s.simplify(Ppass-c0*c2/(L0*L2))==0

original={N:1,w0:s.Rational(3,25),w2:s.Rational(3,25),
          lam0:1,lam2:1,d:s.Rational(3,8),
          c0:s.Rational(1,10000),c2:s.Rational(1,10000)}
assert L0.subs(original)==L2.subs(original)==s.Rational(11,25600)
assert s.factor(p0.subs(original))==s.Rational(211,275)
assert s.factor(p2.subs(original))==s.Rational(211,275)
assert s.factor(Ppass.subs(original))==s.Rational(4096,75625)
assert 0<original[c0]<L0.subs(original) and 0<original[c2]<L2.subs(original)

asym={N:1,w0:s.Rational(3,25),w2:s.Rational(13,100),
      lam0:1,lam2:1,d:s.Rational(4,5),
      c0:s.Rational(1,1000),c2:s.Rational(1,1000)}
assert L0.subs(asym)==s.Rational(79,5625)
assert L2.subs(asym)==s.Rational(59,22500)
assert s.factor(p0.subs(asym))==s.Rational(73,118)
assert s.factor(p2.subs(asym))==s.Rational(587,632)
assert s.factor(Ppass.subs(asym))==s.Rational(2025,74576)

for case in (original,asym):
    assert s.diff(L0,d).subs(case)>0
    assert s.diff(L2,d).subs(case)>0
    assert s.diff(Ppass,d).subs(case)<0

print('FDIS dual thresholds, including all 3^4 Y/N/A ballot profiles: PASS')
print('Costly objection 2x2 stage: pure and mixed Nash equilibrium: PASS')
print('Documentation filing threshold: exact symbolic identities PASS')
print('Symmetric example d=3/8, approval probability:',Ppass.subs(original))
print('Asymmetric example d=4/5, approval probability:',Ppass.subs(asym))
print('Approval probability declines as network effect increases locally: PASS')
