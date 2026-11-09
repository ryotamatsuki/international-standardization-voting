#!/usr/bin/env python3
"""Conditional reference-vs-peer interoperability equilibrium check; no novelty certificate."""
import sympy as s

A,c,b,H,v=s.symbols('A c b H v',positive=True)
r,e=s.symbols('r e',real=True)
D=A*(A-b)-c*c
sol=s.solve([A*r+c*e-H,c*r+(A-b)*e-v],[r,e])
assert s.factor(sol[r]-((A-b)*H-c*v)/D)==0
assert s.factor(sol[e]-(A*v-c*H)/D)==0
assert s.factor(s.diff(sol[r],H)-(A-b)/D)==0
assert s.factor(s.diff(sol[e],H)+c/D)==0
assert s.factor(s.diff(-s.diff(sol[e],H),b)-A*c/D**2)==0
print("PASS: FOCs, equilibrium levels, reference and pairwise derivatives, network amplification")
for h in [s.Rational(1,2),s.Rational(13,10)]:
    prm={A:2,c:s.Rational(4,5),b:s.Rational(2,5),v:s.Rational(3,5),H:h}
    re=s.factor(sol[r].subs(prm)); ee=s.factor(sol[e].subs(prm))
    assert 0<re<1 and 0<ee<1
    print("H:",h,"r:",re,"e:",ee,"pair_quality:",ee**2)
print("No downstream prices, adoption/entry, or ISO national vote are claimed.")
