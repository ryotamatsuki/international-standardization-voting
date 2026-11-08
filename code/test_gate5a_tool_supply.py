"""Gate 5A: exact symbolic supply investment and bargaining calculations.
SymPy regression tests, not a formal machine proof.
"""
import sympy as s

N,d,F,R,K,Vc=s.symbols('N d F R K Vc',positive=True)
G=s.factor(N*d*(60-25*d)/144)
S=s.factor(G+R-F)
fee=s.factor((G+F-R)/2)
assert s.simplify(G-fee-S/2)==0
assert s.simplify(fee+R-F-S/2)==0
W=s.factor(N*d*(216-47*d)/144+Vc-F)
assert s.simplify(W.subs(Vc,R)-
                  (N*d*(216-47*d)/144+R-F))==0

base={N:1,F:s.Rational(1,5),R:s.Rational(1,10),K:s.Rational(1,4)}
cases=[
    (s.Rational(1,3),s.Rational(155,1296),s.Rational(127,6480),
     s.Rational(1423,12960),s.Rational(2357,6480)),
    (s.Rational(3,8),s.Rational(135,1024),s.Rational(163,5120),
     s.Rational(1187,10240),s.Rational(2133,5120)),
]
for dd,g,surplus,license_fee,world_lower in cases:
    state={**base,d:dd}
    assert G.subs(state)==g
    assert S.subs(state)==surplus
    assert fee.subs(state)==license_fee
    assert W.subs({**state,Vc:base[R]})==world_lower
    assert 0<base[R]<base[F] and g<base[F]<g+base[R]
    assert base[K]>g
    assert 0<license_fee<g and license_fee+base[R]>base[F]
    print('d=',dd,'gross joining gain=',g,'joint surplus=',surplus,
          'contract fee=',license_fee,'net global gain lower bound=',world_lower)

# Derivative is affine in d; positive at both endpoints implies positive in between.
assert s.diff(G,d).subs({N:1,d:s.Rational(1,3)})>0
assert s.diff(G,d).subs({N:1,d:s.Rational(3,8)})>0
print('Gate 5A: complementor investment and bargaining checks PASS.')
