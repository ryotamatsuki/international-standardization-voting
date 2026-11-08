"""Extra exact sign/spectrum/adoption-voting inventory checks for P1-KS.
Run from code directory after verify_ks_userbase_vote_reversal_20261109.py
"""
from itertools import product
from sympy import (Rational as R, Matrix, symbols, eye, diag, ones,
                   factor, diff, sqrt, simplify)
from verify_ks_userbase_vote_reversal_20261109 import (
    evaluate, bernstein_positive, b, O, F, I, STATES, W, KL)

cache={s:evaluate(s,b) for s in STATES}
strict=equal=0
for s in STATES:
    for i in range(3):
        if s[i]==0:
            alt=list(s);alt[i]=1;alt=tuple(alt)
            gain=factor(cache[alt]['pi'][i]-cache[s]['pi'][i])
            if gain==0:equal+=1
            else:
                assert bernstein_positive(gain),(s,i,gain)
                strict+=1
assert (strict,equal)==(21,3)

L=Matrix([[1 if i==j else -R(1,2) if (i-j)%4 in (1,3) else 0
           for j in range(4)] for i in range(4)])
for s in STATES:
    name=['L' if s[i] else f'X{i}' for i in range(4)]
    H=Matrix([[int(name[i]==name[j]) for j in range(4)] for i in range(4)])
    es=(L*H).eigenvals()
    assert max(float(k) for k in es)<=3
    for beta in [R(1,10),R(1,2)]:
        assert (eye(4)-beta*L*H/4).det()!=0

old=cache[O];full=cache[F]
dcs=factor(full['cs']-old['cs'])
dpi=[factor(full['pi'][i]-old['pi'][i]) for i in range(4)]
assert bernstein_positive(dcs/4+sum(dpi)-dpi[3])
assert bernstein_positive(diff(dcs/4+sum(dpi),b))
assert bernstein_positive(diff(-4*dpi[1]/dcs,b))
assert bernstein_positive(dpi[1]-dpi[0])

for beta,target in [(R(1,10),45),(R(1,2),45)]:
    data={s:evaluate(s,beta) for s in STATES}
    def v(s,published):
        z=data[s]
        return [factor(W[i]*z['cs']/4+z['pi'][i]
                       -(KL if published and s==F and i==3 else 0))
                for i in range(4)]
    WI,WO,WF=v(I,False),v(O,False),v(F,True)
    counts=[]
    for rejected,approved in ((WO,WF),(WI,WF),(WO,WI),(WI,WI)):
        delta=[approved[i]-rejected[i] for i in range(4)]
        count=0
        for ballot in product([0,1],repeat=4):
            passes=sum(ballot)>=3
            if all((int(sum(ballot[:i]+(1-ballot[i],)+ballot[i+1:])>=3)
                    -int(passes))*delta[i]<=0 for i in range(4)):
                count+=1
        counts.append(count)
    assert sum(counts)==target
    assert counts==([10,10,9,16] if beta==R(1,10) else [7,10,12,16])

h=symbols('h',real=True)
g=['L','L','L','M']
H=Matrix([[int(g[i]==g[j]) for j in range(4)] for i in range(4)])
C=eye(4)-b*L*H/4
T=C.inv()*L
v=ones(4,1)+b*L*H*Matrix([h]*4)
p=(T+diag(*[T[i,i] for i in range(4)])).inv()*C.inv()*v
q=C.inv()*(v-L*p)
hcrit=(8*(3-b)*sqrt((2-b)/(8-3*b))-12+5*b)/(4*b)
assert simplify(p[0]-(12-5*b+4*b*h)/(4*(3-b)))==0
assert simplify(p[1]-(24-9*b+4*b*h)/(8*(3-b)))==0
assert simplify((p[0]*q[0]).subs(h,hcrit)-1)==0
assert abs(float(hcrit.subs(b,R(1,10)))-0.06107290744171641)<1e-12
assert abs(float(hcrit.subs(b,R(1,2)))-0.053844614152614004)<1e-12
print('PASS: 21 positive/3 equal incumbent deviations; 16 spectra;')
print('world benefit, support-threshold derivative, 45 pure reduced-SPNE per endpoint;')
print('common historic installed-base individual profit switching threshold.')
