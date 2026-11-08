"""P1 finite-game backward induction, with selected verified price continuations.
Run: python code/solve_p1_full_backward_20261108.py
For global-price deviation sufficient conditions also run:
python code/test_p1_population_generalization.py
This script classifies every adoption pure NE and all 16 ballot pure NE.
"""
from itertools import product
import sympy as S
Q=S.Rational
d,N,kL,kH=S.symbols("d N kL kH",positive=True)
w=S.symbols("w0:4",positive=True)
M=S.Matrix([[2 if i==j else -Q(1,2) if (i-j)%4 in (1,3) else 0
             for j in range(4)] for i in range(4)])
P=M.inv()
def quality(bits):
    names=['L' if bits[i] else 'X'+str(i) for i in range(3)]
    names+=['L' if bits[3] else 'M']
    return [d*(names.count(names[i])-1) for i in range(4)]
def prices(bits):
    a=quality(bits)
    v=S.Matrix([1+a[i]-(a[(i+1)%4]+a[(i-1)%4])/2 for i in range(4)])
    return [S.factor(x) for x in P*v]
states=list(product((0,1),repeat=4))
ps={s:prices(s) for s in states}
I,O,F=(0,0,0,0),(1,1,1,0),(1,1,1,1)
assert all(S.simplify(x-y)==0 for x,y in zip(ps[O],
             [1+d/3,1+d/6,1+d/3,1-5*d/6]))
assert ps[I]==[1]*4 and ps[F]==[1]*4
for bits in states:
    for i in range(4):
        if not bits[i]:
            other=list(bits);other[i]=1;other=tuple(other)
            adj=bits[(i-1)%4]+bits[(i+1)%4]
            opp=bits[(i+2)%4]
            assert S.simplify(ps[other][i]-ps[bits][i]
                       -d*(3*adj+4*opp)/12)==0
def CS(bits):
    a=quality(bits);p=ps[bits]
    r=[Q(1,2)+(a[i]-p[i]-a[(i+1)%4]+p[(i+1)%4])/2
       for i in range(4)]
    l=[1-r[(i-1)%4] for i in range(4)]
    assert all(S.simplify(r[i]+l[i]-p[i])==0 for i in range(4))
    return S.factor(sum((a[i]-p[i])*p[i]-(r[i]**3+l[i]**3)/3
                        for i in range(4)))
cI,cO,cF=CS(I),CS(O),CS(F)
assert cI==-Q(13,3)
assert S.simplify(cO-(-Q(13,3)+6*d+13*d*d/36))==0
assert S.simplify(cF-(-Q(13,3)+12*d))==0
def W(bits,fee):
    return [S.factor(N*(w[i]*CS(bits)+ps[bits][i]**2)/4
                     -(fee if i==3 and bits[3] else 0))
            for i in range(4)]
wi,wo,wf=W(I,0),W(O,0),W(F,kL)
dOF=[S.factor(wf[i]-wo[i]) for i in range(4)]
dIF=[S.factor(wf[i]-wi[i]) for i in range(4)]
dOI=[S.factor(wi[i]-wo[i]) for i in range(4)]
G=S.factor(N*(1-ps[O][3]**2)/4)
assert S.simplify(G-N*d*(60-25*d)/144)==0
assert S.simplify(sum(dOF).subs(w[3],1-w[0]-w[1]-w[2])-
    (N*d*(216-47*d)/144-kL))==0
def adoption_NE(dd,fee):
    prof={s:[S.factor(x.subs(d,dd)**2)/4 for x in ps[s]] for s in states}
    ans=[]
    for bits in states:
        ok=True
        for i in range(4):
            flip=list(bits);flip[i]=1-bits[i];flip=tuple(flip)
            here=prof[bits][i]-(fee if i==3 and bits[3] else 0)
            there=prof[flip][i]-(fee if i==3 and flip[3] else 0)
            if S.simplify(there-here)>0:ok=False;break
        if ok:ans.append(''.join(map(str,bits)))
    return ans
def ballot_NE(gains):
    ans=[]
    for ballot in states:
        accepted=sum(ballot)>=3
        if all((int(sum(ballot[:i]+(1-ballot[i],)+ballot[i+1:])>=3)
                -int(accepted))*gains[i]<=0 for i in range(4)):
            ans.append(''.join(map(str,ballot)))
    return ans
ww=[Q(3,25),Q(1,2),Q(3,25),Q(13,50)]
for dd in (Q(1,3),Q(3,8)):
    assert adoption_NE(dd,Q(1,5))==['0000','1110']
    assert adoption_NE(dd,Q(1,20))==['0000','1111']
    nums=[]
    for row in (dOF,dIF,dOI,[S.Integer(0)]*4):
        gains=[S.simplify(x.subs({d:dd,N:1,kL:Q(1,20),
               **{w[i]:ww[i] for i in range(4)}})) for x in row]
        eq=ballot_NE(gains)
        nums.append(len(eq))
    assert nums==([10,10,12,16] if dd==Q(1,3) else [7,10,12,16])
    print('d=',dd,'adoption after reject',adoption_NE(dd,Q(1,5)),
          'after accept',adoption_NE(dd,Q(1,20)),
          'ballot-NE counts per pair',nums,'total SPNE',sum(nums))
print('PASS: 16 technologies, exact price profit comparisons, three welfare states,')
print('all adoption pure NE and 16 ballots per each of four continuation pairs.')
