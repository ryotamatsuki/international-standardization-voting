#!/usr/bin/env python3
"""Verify exact reduced-form CAP-regime-switch propositions (not journal novelty).
Run: python code/verify_cap_policy_switch_20261109.py
Needs: sympy, numpy
"""
from __future__ import annotations
from dataclasses import dataclass
import sympy as sp
import numpy as np

@dataclass(frozen=True)
class Params:
    a: float
    b: float
    A: float
    T: float
    K: float

def u(n: float, p: Params) -> float:
    return p.a*n - p.b*n*n/2

def threshold(p: Params) -> float:
    return p.a/p.b + p.T/2 + p.K/(p.b*p.T) - p.A

def equilibrium(p: Params, h: float):
    x=p.A+h
    assert 0 < x-p.T < x < 1, "Only interior results considered"
    accept=u(x,p)
    verify=u(x-p.T,p)-p.K
    if abs(accept-verify)<1e-12:
        return "tie", x, accept, verify
    return ("verify",x-p.T,accept,verify) if verify>accept else ("accept",x,accept,verify)

def symbolic_checks():
    a,b,A,T,K,h,k=sp.symbols('a b A T K h k',positive=True,real=True)
    x=A+h
    W=lambda n:a*n-b*n*n/2
    diff=sp.factor(W(x-T)-K-W(x))
    h_star=sp.solve(diff,h)[0]
    assert sp.simplify(diff-b*T*(h-h_star))==0
    assert sp.simplify(h_star-(a/b+T/2+K/(b*T)-A))==0
    t=sp.symbols('t',real=True)
    FOC=sp.diff(W(x-t)-k*t*t/2,t)
    tstar=sp.solve(FOC,t)[0]
    nstar=sp.simplify(x-tstar)
    assert sp.simplify(tstar-(b*x-a)/(b+k))==0
    assert sp.simplify(sp.diff(nstar,h)-k/(b+k))==0
    assert sp.simplify(sp.diff(FOC,t)+(b+k))==0
    return str(diff),str(h_star),str(tstar)

def numeric_checks():
    p=Params(.3,1,.35,.2,.005)
    hstar=threshold(p)
    below=equilibrium(p,hstar-.01)
    above=equilibrium(p,hstar+.01)
    assert below[0]=="accept" and above[0]=="verify"
    assert abs(below[1]-.415)<1e-12
    assert abs(above[1]-.235)<1e-12
    assert above[1]<below[1]
    assert abs(below[2]-.0383875)<1e-12
    assert abs(above[3]-.0378875)<1e-12
    return hstar,below,above

def interior_stress_test(trials=20000):
    rng=np.random.default_rng(20261109)
    valid=0
    for _ in range(trials):
        p=Params(float(rng.uniform(.25,.35)),
                 float(rng.uniform(.85,1.15)),
                 float(rng.uniform(.32,.38)),
                 float(rng.uniform(.17,.23)),
                 float(rng.uniform(.003,.007)))
        hstar=threshold(p)
        eps=.004
        if hstar-eps>=0 and p.A+hstar+eps<1 and p.A+hstar-eps-p.T>0 and 2*eps<p.T:
            below=equilibrium(p,hstar-eps)
            above=equilibrium(p,hstar+eps)
            assert below[0]=="accept" and above[0]=="verify"
            assert above[1]<below[1]
            valid+=1
    return valid

if __name__=="__main__":
    print("Symbolic:",symbolic_checks())
    print("Example:",numeric_checks())
    print("Interior scenarios passing:",interior_stress_test(),"out of 20000 random parameter draws")
    print("PASS. Numerical parameter variations do not establish global uniqueness or academic novelty.")
