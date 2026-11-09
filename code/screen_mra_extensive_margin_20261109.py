#!/usr/bin/env python3
"""Sanity check for MRA extensive-margin separability; NOT A NEW N3 THEOREM."""
import sympy as s
F, D, sig, k, m=s.symbols('F D sig k m',positive=True)
# Productivity Pareto(m,k), sigma=sig>1, in the interior with F>D*m**(sig-1).
S=(D*m**(sig-1)/F)**(k/(sig-1))
check=s.simplify(F*s.diff(S,F)/S)
assert check== -k/(sig-1)
print("log derivative exporter fraction with respect to fixed export cost:",check)
for f in (4,3,5):
    value=s.factor(S.subs({D:1,m:1,sig:3,k:4,F:f}))
    print("illustrative F =",f,"export share =",value)
assert s.factor(S.subs({D:1,m:1,sig:3,k:4,F:3})-S.subs({D:1,m:1,sig:3,k:4,F:4}))>0
# An unrelated destination has its own independent entry cost:
F_ik, F_ij, D_ik =s.symbols("F_ik F_ij D_ik",positive=True)
S_ik=(D_ik*m**(sig-1)/F_ik)**(k/(sig-1))
assert s.diff(S_ik,F_ij)==0
print("Cross-destination derivative =",s.diff(S_ik,F_ij))
print("PASS; this basic separability observation is known logic, not academic novelty.")
