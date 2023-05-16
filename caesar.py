pt = input("Enter plaintext: ")
k = int(input("Enter key: "))
ct = ''
for i in pt:
    ct = ct + chr(((ord(i)+k)-ord('a'))%26+ord('a'))
print("Cipher text: ",ct)
pt2 = ''
for i in ct:
    pt2 = pt2 + chr(((ord(i)-k)-ord('a'))%26+ord('a'))
print("Plaintext: ",pt2)
