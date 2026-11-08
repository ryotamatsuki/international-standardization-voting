"""P1: endogenous voluntary adoption of an interoperability standard.

Reproduces the candidate Salop continuation equations, establishes a
nonempty cost interval in which approval changes the entrant's private
best response, and verifies voting reversal and net welfare.

This is a symbolic/illustrative verification of the economic theorem.
It is NOT a mechanized proof of every global best-response inequality
in the underlying continuous-price game, nor an empirical estimate of
whether ISO publication decreases implementation costs.
"""
from __future__ import annotations
import sympy as s

D=s.symbols('d', positive=True, real=True)
N=s.symbols('N', positive=True, real=True)
w=s.Matrix([s.Rational(3,25),s.Rational(1,2),s.Rational(3,25),s.Rational(13,50)])
assert sum(w)==1

P=s.Matrix([[2 if i==j else (-s.Rational(1,2) if (i-j)%4 in (1,3) else 0)
             for j in range(4)] for i in range(4)])

def salop_equilibrium(quality):
    a=s.Matrix(quality)
    rhs=s.Matrix([1+a[i]-(a[(i-1)%4]+a[(i+1)%4])/2 for i in range(4)])
    p=P.inv()*rhs
    r=[s.factor(s.Rational(1,2)+(a[i]-p[i]-a[(i+1)%4]+p[(i+1)%4])/2) for i in range(4)]
    l=[s.factor(1-r[(i-1)%4]) for i in range(4)]
    q=[s.factor(l[i]+r[i]) for i in range(4)]
    cs=s.factor(sum((a[i]-p[i])*q[i]-(l[i]**3+r[i]**3)/3 for i in range(4)))
    pi=[s.factor(p[i]*q[i]) for i in range(4)]
    return list(p),q,cs,pi

legacy=salop_equilibrium([2*D,2*D,2*D,0])
all_L=salop_equilibrium([3*D]*4)
assert all(s.simplify(x-y)==0 for x,y in zip(legacy[0],[1+D/3,1+D/6,1+D/3,1-5*D/6]))
assert all(x==1 for x in all_L[0])

private_gain=s.factor((all_L[3][3]-legacy[3][3])*N/4)
assert s.simplify(private_gain - N*D*(60-25*D)/144)==0
country_changes=[s.factor(N*(w[i]*(all_L[2]-legacy[2])
                      +(all_L[3][i]-legacy[3][i]))/4) for i in range(4)]
assert s.simplify(country_changes[0]-N*D*(48-139*D)/3600)==0
assert s.simplify(country_changes[2]-country_changes[0])==0
assert s.simplify(sum(country_changes)-N*D*(216-47*D)/144)==0

k_after=s.Rational(1,20)
k_before=s.Rational(1,5)
interval=(s.Rational(1,3),s.Rational(3,8))
assert interval[0] < s.Rational(48,139) < interval[1]
min_g=s.factor(private_gain.subs({D:interval[0],N:1}))
max_g=s.factor(private_gain.subs({D:interval[1],N:1}))
assert k_after < min_g < max_g < k_before

net_country_changes=country_changes.copy()
net_country_changes[3]=s.factor(net_country_changes[3]-k_after)
world_gain_net=s.factor(sum(net_country_changes).subs(N,1))
assert s.simplify(world_gain_net-(D*(216-47*D)/144-k_after))==0

for dd,expected_yes in [(interval[0],4),(interval[1],2)]:
    gov_deltas=[s.factor(x.subs({D:dd,N:1})) for x in net_country_changes]
    votes=[bool(x>0) for x in gov_deltas]
    assert sum(votes)==expected_yes
    assert world_gain_net.subs(D,dd)>0
    assert k_after < private_gain.subs({D:dd,N:1}) < k_before
    print('d:',str(dd),'~',float(dd),'private gain:',private_gain.subs({D:dd,N:1}),
          'votes:',votes,'world gain after real implementation cost:',world_gain_net.subs(D,dd))

for i in range(4):
    standards=['L']*4
    standards[i]='other'
    q=[D*(standards.count(standards[j])-1) for j in range(4)]
    st=salop_equilibrium(q)
    gain_from_staying=s.factor(N*(all_L[3][i]-st[3][i])/4)
    assert s.simplify(gain_from_staying-private_gain)==0

print('Private joining gain:',private_gain)
print('Low/high private-gain bounds with N=1:',min_g,max_g)
print('Net government votes - relevant countries:',net_country_changes)
print('Net world gain:',world_gain_net)
print('Voting reversal:',s.Rational(48,139),float(s.Rational(48,139)))

f = k_after
bargaining_share=s.Rational(1,2)
for dd in interval:
    g=s.factor(private_gain.subs({D:dd,N:1}))
    license_fee=s.factor(f+bargaining_share*(g-f))
    producer_profit=s.factor(license_fee-f)
    adopter_profit=s.factor(g-license_fee)
    assert producer_profit>0 and adopter_profit>0
    assert producer_profit+adopter_profit==g-f
    print('Approved toolkit bargaining at d=',dd,
          'provider profit=',producer_profit,'adopter incremental profit=',adopter_profit)
print('PASS: nonempty strict implementation-cost window, positive bilateral implementation surplus, and voting reversal.')
