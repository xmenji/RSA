#RSA Assignment for Discrete Mathematics Class

print("Enter 2 PRIME numbers for 'p' and 'q'.")
#USER INPUTS NUMBER 
p = input("p: ") 

q = input("q: ") 

n = int(p) * int(q)

print("\nn = " + str(n))

#Public Key is made of n and e : (n,e)
tempE = 2
#e cannot be a factor of n
e = 0
#phi = (p-1)*(q-1)
phi = (int(p)-1) * (int(q)-1)
print("phi = " + str(phi))

#ENCRYPTION
#CALCULATE PUBLIC KEY : e 
# 1 < e < phi(n)
# e != a factor of n
for x in range(0, phi):
  if n % tempE == 0 or phi % tempE == 0:
    tempE += 1
    if tempE % 2 == 0:
      tempE += 1
  else:
    e = tempE
    
print("e = " + str(e))
print("ENCRYPTION KEY= (" + str(e) + ", " + str(n) + ")")

#DECRYPTION 
#CALCULATE PRIVATE KEY : d 
#d = d * e (mod phi(n)) = 1 

d = 10
while True:
  if (d * e) % phi == 1 :
    break
  else:
    d += 1 
    
print("d = " + str(d))
print("DECRYPTION KEY= (" + str(d) + ", " + str(n) + ")")

#create letters array for simple word messages
alphabet = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)

#ENCRYPTING THE MESSAGE
# c = (m^e) % n 
# c = ciphertext; m = letter to be encrypted
encryptedMsg = []

#GET MESSAGE
msg = input("\nEnter simple message (letters only): ")

msgArray = list(msg)
print(msgArray)

#encrypt 
for x in msgArray:
	encryptedMsg.append( ( letters.index(x)**e) % n )
	
#FINAL ENCRYPTED MESSAGE 
print("\nEncrypted message: ")
print(encryptedMsg)

#DECRYPTING THE MESSAGE
# m = (c^d) % n
# m = decrypted letter; c = ciphertext
decryptedMsg = []

for x in encryptedMsg:
	decryptedMsg.append( letters[(x**d) % n] )

print("\nDecrypted Message: ")	
print(decryptedMsg)
