"""P1 population-share generalization: exact symbolic tests.

Run from repository root:
    python code/test_p1_population_generalization.py

Verifies arbitrary shares, median-pivotal thresholds, asymmetric
vote sequence, welfare, implementation-cost interval, and global
price-best-response sufficient conditions for all 16 adoption profiles.
The written proof is in proofs/p1_population_generalization.md.
"""
from itertools import product
from sympy import symbols, Rational as R, Matrix, factor, simplify, diff, Abs, Max

d,N=symbols("d N",positive=True,real=True)
w=symbols("w0:4",positive=True,real=True)
P=Matrix([[2 if i==j else (-R(1,2) if (i-j)%4 in (1,3) else 0)
           for j in range(4)] for i in range(4)])
p0=[1+d/3, 1+d/6,1+d/3,1-5*d/6]
p1=[1,1,1,1]
delta_cs=d*(216-13*d)/36
dW=[factor(N*(w[i]*delta_cs+p1[i]**2-p0[i]**2)/4) for i in range(4)]
assert simplify(dW[0]-N*d*(w[0]*(216-13*d)-4*(d+6))/144)==0
assert simplify(dW[1]-N*d*(w[1]*(216-13*d)-(d+12))/144)==0
assert simplify(dW[2]-N*d*(w[2]*(216-13*d)-4*(d+6))/144)==0
assert simplify(dW[3]-N*d*(w[3]*(216-13*d)+60-25*d)/144)==0

theta_outer=4*(d+6)/(216-13*d)
theta_center=(d+12)/(216-13*d)
assert simplify(diff(theta_outer,d)-1176/(216-13*d)**2)==0
assert simplify(diff(theta_center,d)-372/(216-13*d)**2)==0
crit=[(216*w[0]-24)/(13*w[0]+4),
      (216*w[1]-12)/(13*w[1]+1),
      (216*w[2]-24)/(13*w[2]+4)]
assert all(simplify(dW[i].subs(d,crit[i]))==0 for i in range(3))

shares=[R(3,25),R(21,50),R(13,100),R(33,100)]
assert sum(shares)==1 and shares[0]!=shares[2]
values={w[i]:shares[i] for i in range(4)}
crit_exact=[factor(x.subs(values)) for x in crit]
assert crit_exact==[R(48,139),R(3936,323),R(408,569)]
assert sorted(crit_exact)[1]==R(408,569)
kL,kH=R(1,20),R(3,10)
G3=N*d*(60-25*d)/144
for dd,expected_votes,expected_world in [
        (R(1,5),(1,1,1,1),R(853,3600)),
        (R(2,5),(0,1,1,1),R(112,225)),
        (R(4,5),(0,1,0,1),R(847,900))]:
    W=[factor(x.subs(values).subs({d:dd,N:1})) for x in dW]
    W[3]-=kL
    assert tuple(1 if q>0 else 0 for q in W)==expected_votes,(dd,W)
    assert sum(W)==expected_world, (dd,sum(W),expected_world)
    assert kL<G3.subs({d:dd,N:1})<kH
    print('d=',dd,'voting=',expected_votes,'world_gain_if_implemented=',sum(W))
assert theta_outer.subs(d,0)==R(1,9)
assert simplify(theta_outer.subs(d,R(6,7))-R(32,239))==0
assert theta_center.subs(d,0)==R(1,18)
assert simplify(theta_center.subs(d,R(6,7))-R(15,239))==0

def qualities(bits):
    names=['L' if bits[i] else f'X{i}' for i in range(3)]+['L' if bits[3] else 'M']
    return [d*(names.count(names[i])-1) for i in range(4)]

def eq_prices(a):
    rhs=Matrix([1+a[i]-(a[(i-1)%4]+a[(i+1)%4])/2 for i in range(4)])
    return list(P.inv()*rhs)

def bounds(a,p,i):
    b=[factor(p[j]-a[j]) for j in range(4)]
    r0=(1+b[(i+1)%4]+a[i])/2
    l0=(1+b[(i-1)%4]+a[i])/2
    rs,ls=r0-p[i]/2,l0-p[i]/2
    opp=b[(i+2)%4]+a[i]
    return [p[i],r0,l0,R(3,2)-r0,R(3,2)-l0,2-opp,rs,ls,
            1-rs,1-ls,1-Abs(r0-l0),opp-p[i]+4-4*Max(rs,ls)]

all_margins=[]
for bits in product((0,1),repeat=4):
    a=qualities(bits); p=eq_prices(a)
    for i in range(4):
        for expression in bounds(a,p,i):
            for val in (R(1,5),R(4,5)):
                margin=simplify(expression.subs(d,val))
                assert margin>0,(bits,i,val,expression,margin)
                all_margins.append(margin)
assert len(all_margins)==1536
assert min(all_margins)==R(1,30)
print('All 16 admission profiles: 1,536 sufficient-condition inequalities PASS.')
print('Smallest exact margin:',min(all_margins))
print('Population-share-free P1 theorem and asymmetric example: PASS.')
