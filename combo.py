q = [400, 530, 1]
w = [400, 500, 1]
e = [400, 440, 1]
r = [400, 400, 1]
t = [400, 370, 1]
y = [400, 330, 1]
u = [400, 290, 1]
i = [400, 250, 1]
o = [400, 210, 1]
p = [400, 160, 1]
a = [350, 500, 1]
s = [350, 470, 1]
d = [350, 410, 1]
f = [350, 370, 1]
g = [350, 330, 1]
h = [350, 290, 1] 
j = [350, 250, 1]
k = [350, 210, 1]
l = [350, 180, 1]
z = [330, 470, 1]
x = [330, 410, 1]
c = [330, 370, 1]
v = [330, 330, 1]
b = [330, 290, 1]
n = [330, 250, 1]
m = [330, 210, 1]

one = [400, 530, 3]
two = [400, 500, 3]
three = [400, 440, 3]
four = [400, 400, 3]
five = [400, 370, 3] 
six = [400, 330, 3]
seven = [400, 290, 3]
eight = [400, 250, 3]
nine = [400, 210, 3]
zero = [400, 160, 3]

Q = [400, 530, 2]
W = [400, 500, 2]
E = [400, 440, 2]
R = [400, 400, 2]
T = [400, 370, 2]
Y = [400, 330, 2]
U = [400, 290, 2]
I = [400, 250, 2]
O = [400, 210, 2]
P = [400, 160, 2]
A = [350, 500, 2]
S = [350, 470, 2]
D = [350, 410, 2]
F = [350, 370, 2]
G = [350, 330, 2]
H = [350, 290, 2] 
J = [350, 250, 2]
K = [350, 210, 2]
L = [350, 180, 2]
Z = [330, 470, 2]
X = [330, 410, 2]
C = [330, 370, 2]
V = [330, 330, 2]
B = [330, 290, 2]
N = [330, 250, 2]
M = [330, 210, 2]


keyboard = {'q': q,'w': w,'e': e,'r': r,'t': t,'y': y,'u': u,'i': i,'o': o,'p': p,'a': a,'s': s,'d': d,'f': f,'g': g,'h': h,'j': j,'k': k,'l': l,'z': z,'x': x,'c': c,'v': v,'b': b,'n': n,'m': m,'Q': Q,'W': W,'E': E,'R': R,'T': T,'Y': Y,'U': U,'I': I,'O': O,'P': P,'A': A,'S': S,'D': D,'F': F,'G': G,'H': H,'J': J,'K': K,'L': L,'Z': Z,'X': X,'C': C,'V': V,'B': B,'N': N,'M': M,'1': one,'2': two,'3': three,'4': four,'5': five,'6': six,'7': seven,'8': eight,'9': nine,'0': zero}


def input(crypt):
  stranged = str(crypt)
  print stranged
  output = keyboard[stranged]
  key(output)

def key(output):
  alpha = got[0]
  beta = got[1]
  delta = got[2]
  print alpha, beta, delta

input(a)
