import string
import random

#INCRYPT
char=string.whitespace+string.punctuation+string.digits+string.ascii_letters
print(char)
char=list(char)
key=char.copy()

random.shuffle(key)
print(f"Chars:{char}")
print(f"Keys:{key}")


plain_text=input("Enter A message To encrypt:")
cipher_text=""

for letter in plain_text:
    index=char.index(letter)
    cipher_text+=key[index]
print(f"Original Message {plain_text }")
print(f"Encrypted Message {cipher_text }")

#Decrypt


cipher_text=input("Enter A message To Encrypt:")
plain_text=""

for letter in cipher_text :
    index=key.index(letter)
    plain_text +=char[index]

print(f"encrypted Message: {cipher_text }")
print(f"Decrypted Message: {plain_text }")