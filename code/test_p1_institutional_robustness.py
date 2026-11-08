"""P1 national-stakeholder welfare weighting and validity-of-negative-ballot checks.

Run: python code/test_p1_institutional_robustness.py
Tests closed-form national support and the asymmetry/symmetry robustness
examples with SymPy's exact rational arithmetic.
"""
import sympy as S

d = S.symbols("d", positive=True)
ratio = S.symbols("ratio", positive=True)
theta = S.factor(4*(d+6)/(216-13*d))
assert S.simplify(S.diff(theta,d)-1176/(216-13*d)**2)==0
private_join = d*(60-25*d)/144
gross_world=d*(216-47*d)/144
k_low,k_high=S.Rational(1,20),S.Rational(3,10)

def votes(shares, intensity, profit_weight):
    dc = intensity*(216-13*intensity)/36
    profits = [
        -intensity*(intensity+6)/9,
        -intensity*(intensity+12)/36,
        -intensity*(intensity+6)/9,
        intensity*(60-25*intensity)/36
    ]
    delta_u = [S.factor(shares[i]*dc/4+
                profit_weight*profits[i]/4) for i in range(4)]
    delta_u[3] -= profit_weight*k_low
    return tuple(bool(x>0) for x in delta_u),delta_u

# Unequal market sizes and preference weighting both admit an open range
w_hetero=(S.Rational(3,25),S.Rational(21,50),
          S.Rational(13,100),S.Rational(33,100))
low, high =S.Rational(1,5),S.Rational(4,5)
min_ratio=S.factor(w_hetero[2]/theta.subs(d,high))
max_ratio=S.factor(w_hetero[0]/theta.subs(d,low))
assert min_ratio==S.Rational(3341,3400)
assert max_ratio==S.Rational(3201,3100)
assert min_ratio < 1 < max_ratio
assert votes(w_hetero,low,S.Integer(1))[0] == (1,1,1,1)
assert votes(w_hetero,high,S.Integer(1))[0] == (0,1,0,1)

# Symmetric populations, industry-weighted national positions
w_sym=(S.Rational(1,4),)*4
min_ratio_sym=S.factor(w_sym[0]/theta.subs(d,high))
max_ratio_sym=S.factor(w_sym[0]/theta.subs(d,low))
assert min_ratio_sym==S.Rational(257,136)
assert max_ratio_sym==S.Rational(1067,496)
assert min_ratio_sym < 2 < max_ratio_sym
for x, expected in [(low,(1,1,1,1)),
                    (S.Rational(2,5),(1,1,1,1)),
                    (high,(0,1,0,1))]:
    vote, deltas=votes(w_sym,x,S.Integer(2))
    assert vote==expected,(x,vote,deltas)
    assert k_low < private_join.subs(d,x) < k_high
    assert gross_world.subs(d,x)-k_low>0
    print("d",x,"symmetric vote",vote,
          "world actual gain if implemented", gross_world.subs(d,x)-k_low)

# Actual 2026 ISO dual rule: negative ballots without technical comments excluded.
# Two Yes ballots + m technically supported No ballots, m in {0,1,2}.
for m, accepted in [(0,True),(1,False),(2,False)]:
    p_yes=S.Rational(2,2+m)
    p_no=S.Rational(m,2+m)
    result=bool((p_yes>=S.Rational(2,3)) and
                (p_no<=S.Rational(1,4)))
    assert result==accepted
    print("technically valid negatives:",m,
          "approval under double rule:",result)
print("PASS: stakeholder objectives, two open sets of preference weights,"
      " and formal qualified-negative-ballot outcomes.")
