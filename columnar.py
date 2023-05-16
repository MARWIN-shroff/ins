import numpy as np
pt = input("Enter plaintext: ")
k = input("Enter key: ")
kn = np.argsort([ord(i) for i in k])
ct_b = []
t = 0
for i in range(int(np.ceil(len(pt)/len(k)))):
    ct_b.append(pt[t:(i+1)*len(k)])
    t = (i+1)*len(k)
if len(ct_b[-1])<len(ct_b[0]):
    ct_b[-1] = ct_b[-1] +'#'*(len(ct_b[0])-len(ct_b[-1]))
ct_b = np.array([list(i) for i in ct_b])
ct_b = ct_b.transpose()
ct_f = ct_b[kn]
ct=''
def red(ct,i):
    for c in i:
        ct+=c
    return ct
for i in ct_f:
    ct = red(ct,i)
print(ct)
def decrypt(ct, k):
    kn = np.argsort([ord(i) for i in k])
    ct_b = np.array([list(ct[i:i+len(k)]) for i in range(0, len(ct), len(k))])
    ct_f = ct_b.transpose()[kn]
    pt_b = ct_f.transpose()
    pt = ''.join(pt_b.flatten())
    pt = pt.rstrip('#')
    return pt
print(pt)
