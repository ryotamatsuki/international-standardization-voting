#!/usr/bin/env python3
"""N3 negative-screen code: genuine conditional theorem and robustness counterexamples.
Requires sympy numpy scipy. Math run independently in Python during the research turn.
The result is NOT a novel economic theorem.
"""
import sympy as s
import numpy as np
from scipy.optimize import brentq
M,F=s.symbols("M F",positive=True)
p=(1-s.sqrt(1-4*F/M))/2
E=s.factor(M*(1-p))
Ed=s.diff(E,M)
assert s.factor((M-2*F)**2-M*(M-4*F))==4*F**2
print("p:",p,"E:",E,"E'(M)-1:",s.simplify(Ed-1))
def smooth_entry(m,f):
    assert m>4*f>0
    return (m+(m*(m-4*f))**.5)/2
def cab_p(m,f):
    assert m>4*f>0
    return (1-(1-4*f/m)**.5)/2
b,c,f=1,2,.45
pre=smooth_entry(b+c,f)
post=b+smooth_entry(c,f)
assert post<pre
print("Example:",{"fee_pre":cab_p(b+c,f),"fee_post":cab_p(c,f),"entry_pre":pre,"entry_post":post,"change":post-pre})
rng=np.random.default_rng(9)
for _ in range(10000):
    cc=rng.uniform(.1,3)
    bb=rng.uniform(.01,2)
    ff=rng.uniform(.00001,cc*.24975)
    assert bb+smooth_entry(cc,ff)<smooth_entry(cc+bb,ff)
print("PASS: 10000 random draws in the interior for uniform firm profitability")
def q(x,a): return 1-x**a
def lowprice(mass,fixed,a):
    peak=(1/(a+1))**(1/a)
    assert fixed<mass*peak*q(peak,a)
    return brentq(lambda x:mass*x*q(x,a)-fixed,0,peak)
for a in [.4,.5,.75,1,2,3]:
    bb,cc=.1,1
    ff=cc*.1*q(.1,a)
    before=(cc+bb)*q(lowprice(cc+bb,ff,a),a)
    after=bb+cc*q(lowprice(cc,ff,a),a)
    print("survival exponent:",a,"total change:",after-before)
    assert (after>before) if a<=.75 else (after<before)
# Profit-maximizing nonprofit policy ablation: monopoly with q=1-p has p*=0.5
# Post-recognition c/4=0.5 covers fixed F=0.45 so the CAB still operates.
old=(b+c)*.5
new=b+c*.5
assert f<c/4 and new>old
print("monopoly alternative:",{"entry_pre":old,"entry_post":new,"change":new-old})
print("PASS all; the model's sign is NOT robust to firm distribution or CAB pricing objective")
