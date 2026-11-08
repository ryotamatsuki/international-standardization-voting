"""Gate 4 prior-art audit: exact strategic-form identity to Diekmann's
two-player volunteer's dilemma and equilibrium-selection limitation.

No claim of a novel underlying volunteer's-dilemma theorem.
"""
from itertools import product
import sympy as s
L0,L2,c0,c2=s.symbols('L0 L2 c0 c2',positive=True)

def gate4(a0,a2):
    # Both abstain => standard passes; otherwise one objection defeats it.
    return (-(L0 if not(a0 or a2) else 0)-(c0 if a0 else 0),
            -(L2 if not(a0 or a2) else 0)-(c2 if a2 else 0))

def standard_volunteer(a0,a2):
    # Volunteer provides common "no-standard" good of value L_i.
    return ((L0 if a0 or a2 else 0)-(c0 if a0 else 0),
            (L2 if a0 or a2 else 0)-(c2 if a2 else 0))

for a0,a2 in product((0,1),repeat=2):
    gate=gate4(a0,a2)
    std=standard_volunteer(a0,a2)
    assert all(s.simplify(std[i]-gate[i]-[L0,L2][i])==0 for i in range(2))

# Verify two distinct pure Nash equilibria, and mixed best-response cutoff.
example={a: tuple(s.sympify(x).subs({L0:5,L2:7,c0:1,c2:2})
                  for x in gate4(*a)) for a in product((0,1),repeat=2)}
equilibria=[]
for (a,b),u in example.items():
    if u[0]>=example[(1-a,b)][0] and u[1]>=example[(a,1-b)][1]:
        equilibria.append((a,b))
assert set(equilibria)=={(1,0),(0,1)}

# Asymmetric mixed Nash opponent-indifference identities:
p0=1-c2/L2
p2=1-c0/L0
assert s.simplify((1-p2)*L0-c0)==0
assert s.simplify((1-p0)*L2-c2)==0
P_mixed=s.factor((1-p0)*(1-p2))
assert s.simplify(P_mixed-c0*c2/(L0*L2))==0
# Pure equilibrium approval probability = 0; mixed is positive.
assert P_mixed.subs({L0:5,L2:7,c0:1,c2:2})>0
print("PASS: Gate 4 payoff = classic volunteer's dilemma payoff - constant L_i.")
print("PASS: Two pure equilibria reject, mixed equilibrium has positive acceptance.")
print("STATUS: Mixed approval formula is NOT unique across Nash equilibria.")
