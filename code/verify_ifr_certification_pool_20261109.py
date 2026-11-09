#!/usr/bin/env python3
"""Check new IFR demand-pooling lemma; not N3-original.
Stable root assumption: p*h(p)<1 where h=-q'/q.
"""
from math import exp,sqrt
from scipy.optimize import brentq
def price(M,F,q,peak):
    assert 0<F<M*peak*q(peak)
    return brentq(lambda x:M*x*q(x)-F,0,peak)
cases=[
 ("exponential",lambda z:exp(-z),1.0),
 ("Weibull IFR shape2",lambda z:exp(-z*z),1/sqrt(2)),
 ("uniform IFR",lambda z:1-z,.5),
 ("survival 1-sqrt(p), NON-IFR",lambda z:1-sqrt(z),(1/1.5)**2)
]
for name,q,peak in cases:
    b,c=.2,2.
    p_target=.2
    F=c*p_target*q(p_target)
    p_pre=price(b+c,F,q,peak)
    p_post=price(c,F,q,peak)
    pre=(b+c)*q(p_pre)
    post=b+c*q(p_post)
    print(name,"fees",p_pre,p_post,"before",pre,"after",post,"entry change",post-pre)
    if "NON-IFR" in name:
        assert post>pre
    else:
        assert post<pre
print("PASS. IFR is sufficient for this particular fee-pooling model, not a model-free trade result.")
