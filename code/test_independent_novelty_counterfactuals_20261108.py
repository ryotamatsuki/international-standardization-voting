"""Independent P1 adversarial counterfactual and symbolic validation.
Source as independently inspected: research/p1-proof-novelty-gate-20261108
initial HEAD b50f6596c36689f97a6b7a9f8fb40f7cfae67d6f.
Checks equilibrium sufficient-condition inequalities, not equilibrium uniqueness
or peer-reviewed publication novelty.
Run: python code/test_independent_novelty_counterfactuals_20261108.py
"""
import itertools
import sympy as S
Q=S.Rational
d,N=S.symbols('d N',positive=True)
w=S.symbols('w0:4',real=True)
P=S.Matrix([[2 if i==j else -Q(1,2) if (i-j)%4 in (1,3) else 0
             for j in range(4)] for i in range(4)])
def quality(bits):
    standards=['L' if bits[i] else f'X{i}' for i in range(3)]
    standards+=['L' if bits[3] else 'M']
    return [d*(standards.count(standards[i])-1) for i in range(4)]
def prices(a):
    return list(P.inv()*S.Matrix([1+a[i]-(a[(i-1)%4]+a[(i+1)%4])/2
                                   for i in range(4)]))
def cs(a,p):
    rr=[Q(1,2)+(a[i]-p[i]-a[(i+1)%4]+p[(i+1)%4])/2 for i in range(4)]
    ll=[1-rr[(i-1)%4] for i in range(4)]
    assert all(S.simplify(rr[i]+ll[i]-p[i])==0 for i in range(4))
    return S.factor(sum((a[i]-p[i])*p[i]-(rr[i]**3+ll[i]**3)/3
                        for i in range(4)))
a0=quality((1,1,1,0))
a1=quality((1,1,1,1))
p0=prices(a0);p1=prices(a1)
assert all(S.simplify(x-y)==0 for x,y in zip(p0,
   [1+d/3,1+d/6,1+d/3,1-5*d/6]))
assert p1==[1]*4
c=S.factor(cs(a1,p1)-cs(a0,p0))
assert S.simplify(c-d*(216-13*d)/36)==0
delta_pi=[S.factor(1-p0[i]**2) for i in range(4)]
g=[S.factor(N*(w[i]*c+delta_pi[i])/4) for i in range(4)]
assert S.simplify(g[0]-N*d*(w[0]*(216-13*d)-4*(d+6))/144)==0
assert S.simplify(g[1]-N*d*(w[1]*(216-13*d)-(d+12))/144)==0
assert S.simplify(g[2]-N*d*(w[2]*(216-13*d)-4*(d+6))/144)==0
assert S.simplify(g[3]-N*d*(w[3]*(216-13*d)+60-25*d)/144)==0
assert S.simplify((sum(g)-N*d*(216-47*d)/144).subs(
    {w[3]:1-w[0]-w[1]-w[2]}))==0
outer=4*(d+6)/(216-13*d)
center=(d+12)/(216-13*d)
assert S.simplify(S.diff(outer,d)-1176/(216-13*d)**2)==0
assert S.simplify(S.diff(center,d)-372/(216-13*d)**2)==0
# Price best-response *sufficient* margins in all 16 technology states
margins=[]
for bits in itertools.product((0,1),repeat=4):
    a=quality(bits);p=prices(a)
    b=[S.factor(p[i]-a[i]) for i in range(4)]
    for i in range(4):
        r=(1+b[(i+1)%4]+a[i])/2
        l=(1+b[(i-1)%4]+a[i])/2
        rs=r-p[i]/2;ls=l-p[i]/2
        opp=b[(i+2)%4]+a[i]
        m=[p[i],r,l,Q(3,2)-r,Q(3,2)-l,2-opp,rs,ls,
           1-rs,1-ls,1-S.Abs(r-l),opp-p[i]+4-4*S.Max(rs,ls)]
        for expr in m:
            for dd in (Q(1,5),Q(4,5)):
                val=S.simplify(expr.subs(d,dd))
                assert not val.free_symbols and val>0,(bits,i,expr,dd,val)
                margins.append(val)
assert len(margins)==1536 and min(margins)==Q(1,30)
shares=[Q(3,25),Q(21,50),Q(13,100),Q(33,100)]
mapping={w[i]:shares[i] for i in range(4)}
critical=[(216*w[0]-24)/(13*w[0]+4),
          (216*w[1]-12)/(13*w[1]+1),
          (216*w[2]-24)/(13*w[2]+4)]
cc=[S.simplify(x.subs(mapping)) for x in critical]
assert cc==[Q(48,139),Q(3936,323),Q(408,569)]
assert sorted(cc)[1]==Q(408,569)
gain3=N*delta_pi[3]/4
for dd,votes_target,net_w_target in [
    (Q(1,5),(True,True,True,True),Q(853,3600)),
    (Q(2,5),(False,True,True,True),Q(112,225)),
    (Q(4,5),(False,True,False,True),Q(847,900))]:
    nat=[S.simplify(x.subs(mapping).subs({N:1,d:dd})) for x in g]
    nat[3]-=Q(1,20)
    assert all(not x.free_symbols for x in nat)
    votes=tuple(bool(x>0) for x in nat)
    assert votes==votes_target and S.simplify(sum(nat)-net_w_target)==0
    assert Q(1,20)<gain3.subs({N:1,d:dd})<Q(3,10)
    print('d',dd,'votes',votes,'2/4',sum(votes)>=2,
          '3/4',sum(votes)>=3,'unanimity',sum(votes)>=4,
          'world welfare gain if implemented',S.factor(sum(nat)))
assert S.simplify(g[0].subs(w[0],Q(1,4))-N*d*(120-29*d)/576)==0
print('PASS: 1536 exact sufficient-condition inequalities, min 1/30;')
print('P1 symbolic identities, generalized voting and quota counterfactuals.')
