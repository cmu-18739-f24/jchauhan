import sys
import math
import time
from Crypto.Util.number import getPrime, isPrime, bytes_to_long, inverse

e = 3

prime_length = 128 #specifies the length of the primes, in bits
N_values = []
cipher_texts = []

m = open("./flag.txt").read()
#m = "picoCTF"


print("I am sending the same message to my 3 friends with my super secure RSA algorithm", flush=True)
time.sleep(1)
print("I will give you the public key (N) and the ciphertext for each of these messages", flush=True)
time.sleep(2)
print("Even then you won't be able to crack the message, or will you?")
print(f"The length of the message is {len(m)}", flush=True)


# #In CRT, all N values must be coprimes
def get_N():
    found = 0
    while not found:
        N = getPrime(prime_length)
        if(len(N_values) == 0):
            return N
        elif(len(N_values) == 1):
            if(math.gcd(N, N_values[0]) == 1):
                return N
        else:
            if(math.gcd(N, N_values[0]) == 1 and math.gcd(N, N_values[1]) == 1):
               return N

for i in range (0,3):
    N = get_N()
    N_values.append(N)
    c = pow(bytes_to_long(m.encode('utf-8')), e, N)
    cipher_texts.append(c)
    print(f"N{i} : {N} ", flush=True)
    print(f"C{i} : {c}", flush=True)

print("Try to guess the flag here")
flag_guess = input()
if(flag_guess == m):
    print("You got it!", flush=True)
else:
    print("Wrong")



    









    