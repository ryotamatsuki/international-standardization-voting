"""Closed-form Gate 1 and Gate 2 checks for International Standardization Voting.

The global-price proof is supplied in proofs/gate1_closed_form_global_bertrand.md.
Here exact rational symbolic inequalities certify its finite set of sufficient
conditions for all relevant standard-adoption profiles on d in [1/3, 3/8].

This is not a formal proof assistant; see the written economic proof.
"""
from itertools import product
import sympy as S

d = S.symbols("d", real=True, positive=True)
N = S.symbols("N", positive=True)
DLOW, DHIGH = S.Rational(1, 3), S.Rational(3, 8)
dstar = S.Rational(48, 139)
PL = S.Matrix([[S.Integer(2) if i == j else
                (-S.Rational(1, 2) if (i-j) % 4 in (1, 3)
                 else S.Integer(0)) for j in range(4)] for i in range(4)])
assert PL.det() != 0
w = [S.Rational(3, 25), S.Rational(1, 2),
     S.Rational(3, 25), S.Rational(13, 50)]


def quality(bits):
    """Each incumbent remains on L (1) or moves to its unique X_i (0).
    Entrant 3 chooses L (1) or M (0).
    """
    names = [("L" if bits[i] else f"X{i}") for i in range(3)]
    names += ["L" if bits[3] else "M"]
    return [d * (names.count(names[i]) - 1) for i in range(4)]


def prices(a):
    rhs = S.Matrix([1 + a[i] - (a[(i-1) % 4] + a[(i+1) % 4])/2
                   for i in range(4)])
    return list(PL.inv() * rhs)


def proof_margins(a, p, i):
    """Margins which imply global best-response inequality q_i(z)<=(2p_i-z)+."""
    b = [S.factor(p[k] - a[k]) for k in range(4)]
    R0 = S.factor((1 + b[(i+1) % 4] + a[i]) / 2)
    L0 = S.factor((1 + b[(i-1) % 4] + a[i]) / 2)
    Rstar, Lstar = R0 - p[i]/2, L0 - p[i]/2
    Bopp = b[(i+2) % 4] + a[i]
    return [
        S.factor(p[i]), R0, L0, S.Rational(3, 2)-R0,
        S.Rational(3, 2)-L0, S.factor(2 - Bopp),
        S.factor(Rstar), S.factor(Lstar),
        S.factor(1-Rstar), S.factor(1-Lstar),
        S.factor(1 - S.Abs(R0-L0)),
        S.factor(Bopp - p[i] + 4 - 4*S.Max(Rstar,Lstar))
    ]


def pos_at_endpoints(expr):
    """All expressions are affine, concave min-of-affine or 1-|affine|.
    Positive endpoints thus imply positivity throughout the interval.
    """
    return all(bool(S.simplify(expr.subs(d, x)) > 0)
               for x in (DLOW, DHIGH))


# Check all 16 possible standard-adoption continuations.
for bits in product((0, 1), repeat=4):
    a = quality(bits)
    p = prices(a)
    for i in range(4):
        for expr in proof_margins(a, p, i):
            assert pos_at_endpoints(expr), (bits, i, expr)
print("Gate 1: All 16 adoption-market price profiles meet the closed-form")
print("        global-best-response sufficient conditions on [1/3, 3/8].")

p0 = prices(quality((1, 1, 1, 0)))
p1 = prices(quality((1, 1, 1, 1)))
assert p0 == [1+d/3, 1+d/6, 1+d/3, 1-5*d/6]
assert p1 == [1]*4

# With q_i=p_i, global operating profit in all segmented national
# markets equals (N/4) * p_i^2.
private_join_gain = S.factor(N*(p1[3]**2 - p0[3]**2)/4)
assert S.simplify(private_join_gain-N*d*(60-25*d)/144) == 0

# All-new profile is a strict adoption NE when entrant cost is below G3.
for i in range(4):
    bits = [1, 1, 1, 1]
    bits[i] = 0
    dev_prices = prices(quality(tuple(bits)))
    lost_profit = S.factor(N*(p1[i]**2 - dev_prices[i]**2)/4)
    assert S.simplify(lost_profit-private_join_gain) == 0

# Status quo is also a strict adoption NE after rejection with high cost.
for i in range(3):
    bits = [1, 1, 1, 0]
    bits[i] = 0
    deviating_prices = prices(quality(tuple(bits)))
    change = S.factor(N*(deviating_prices[i]**2-p0[i]**2)/4)
    expected = (-7*N*d*(d+24)/576 if i in (0,2)
                else N*d*(d-12)/48)
    assert S.simplify(change-expected) == 0
    for dd in (DLOW, DHIGH):
        assert change.subs({d:dd, N:1}) < 0

kL, kH = S.Rational(1,20), S.Rational(1,5)
gain_low = S.factor(private_join_gain.subs({d:DLOW,N:1}))
gain_high = S.factor(private_join_gain.subs({d:DHIGH,N:1}))
assert kL < gain_low < gain_high < kH
assert DLOW < dstar < DHIGH

# Consumer surplus: calculate using analytical left/right Hotelling boundaries.
def consumer_surplus(a, p):
    right=[S.factor(S.Rational(1,2) + (a[i]-p[i]-
           a[(i+1)%4]+p[(i+1)%4])/2) for i in range(4)]
    left=[S.factor(1-right[(i-1)%4]) for i in range(4)]
    q=[S.factor(left[i]+right[i]) for i in range(4)]
    assert all(S.simplify(q[i]-p[i])==0 for i in range(4))
    return S.factor(sum((a[i]-p[i])*q[i] -
                        (left[i]**3+right[i]**3)/3 for i in range(4)))

cs0=consumer_surplus(quality((1,1,1,0)),p0)
cs1=consumer_surplus(quality((1,1,1,1)),p1)
cs_gain=S.factor(cs1-cs0)
assert S.simplify(cs_gain-d*(216-13*d)/36)==0
gov_gain=[S.factor(N*(w[i]*cs_gain+p1[i]**2-p0[i]**2)/4)
          for i in range(4)]
assert S.simplify(gov_gain[0]-N*d*(48-139*d)/3600)==0
assert S.simplify(gov_gain[1]-N*d*(64-5*d)/96)==0
assert S.simplify(gov_gain[2]-gov_gain[0])==0
assert S.simplify(gov_gain[3]-11*N*d*(176-43*d)/2400)==0
gov_gain[3] -= kL
world_gain=S.factor(sum(gov_gain))
assert S.simplify(world_gain - (N*d*(216-47*d)/144-kL))==0

for dd,yes_count in [(DLOW,4),(DHIGH,2)]:
    votes=[bool(x.subs({d:dd,N:1})>0) for x in gov_gain]
    assert sum(votes)==yes_count
    assert world_gain.subs({d:dd,N:1})>0
    print(f"Gate 2: d={dd}, yes votes={sum(votes)}, "
          f"gross private joining gain={private_join_gain.subs({d:dd,N:1})}, "
          f"net world welfare gain={world_gain.subs({d:dd,N:1})}")

# Population-share thresholds
tau=4*(d+6)/(216-13*d)
assert S.simplify(tau.subs(d,DLOW)-S.Rational(76,635))==0
assert S.simplify(tau.subs(d,DHIGH)-S.Rational(68,563))==0
assert S.simplify(S.diff(tau,d)-1176/(216-13*d)**2)==0
print("P1 threshold:", dstar, "=", float(dstar))
print("Population thresholds:",tau.subs(d,DLOW),tau.subs(d,DHIGH))
print("PASS: exact algebra, global-price sufficient conditions, continuation NE,")
print("      welfare identities, and vote reversal. Selection/novelty are separate.")
