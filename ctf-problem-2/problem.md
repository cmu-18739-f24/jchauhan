# Chinese Remainder Theorem

- Namespace: picoctf/18739f24
- ID: chinese-remainder-theorem
- Type: custom
- Category: Cryptography
- Points: 200
- Templatable: yes
- MaxUsers: 1

## Running

This problem should be able to run with cmgr.

## Chinese Remainder Theorem Problem - Description

This problems uses a vulnerable encryption method, can you crack it?
Also note this problem follows a slightly unconventional flag format: it should be pico{<8 characters>}.
I had to use an abbreviated flag format because otheriwse the solution may run into precision issues.

This problem generates and prints 3 different N values (public keys), all of which are coprime, which is a necessary condition for the Chinese Remainder Theorem. Then the flag is encrypted with each of these public keys and all three cipher texts are displayed to the user.

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The program's source code can be downloaded {{url_for("crt.py", "here")}}

## Hints

- Look up the chinese remainder theorem

- IMPORTANT: Be sure to use the Decimal package when taking the cube root of a number. Otherwise you will run into precision errors

## Solution Overview

The vulnerability in this program lies in the fact that the e value for the RSA program was set to e=3, this value is too low.
We can use the Chinese remainder theorem to solve for M^3, (the message cubed). Then we take the cube root of this value to get the final message.

Here is the general outline for using the Chinese remainder theorem:

1. Multiply all Ni values together, store them in a value say, N_product

2. For each cipher text message:
  - 2.1 Calcuate NN_i  = N_product / Ni
  - 2.2. Calculate the modular inverse using Fermat's Little Theorem:
        xi = NN_i ^ (Ni - 2) mod Ni
  - 2.3 Calculate and store the final term, ti.
        ti = (NN_i) * (cipher_texts_i) * (xi) 

3. Sum all terms t = t0 + t1 + t3

4. Then M^3 = t mod N_product

5. Then M = cube_root(M^3)

See the references section that explain the details of the Chinese remainder in greater detail.
Below is an example solution script:

```
import sys
import math
from Crypto.Util.number import getPrime, isPrime, bytes_to_long, inverse
from decimal import Decimal, getcontext

e = 3

prime_length = 128 #specifies the length of the primes, in bits

#Copy N Values from output here
N_values = [280567471590744086516746092254981142493,253599520238393514016194415122672455521,288187072495672378636343367080601689743 ]

#Copy C Values from output here
cipher_texts = [235334360188684979822727060182449410792, 155066959103102407738464600070397962450,31291090348728409332539432286844414133 ]

#Copy from problem out here
length_m = 14


#Solution Script Shown Below
N_product = 1
for i in range(0,3) :
    N_product *= N_values[i]


inverse_sum = 0
for i in range(0,3):
    #NN_i = N_product // N_values[i]
    if(i == 0) :
        NN_i = N_values[1] * N_values[2]
    elif(i == 1):
        NN_i = N_values[0] * N_values[2]
    else:
        NN_i = N_values[0] * N_values[1]

    inverse_i = pow(NN_i, N_values[i] - 2, N_values[i])
    inverse_sum += ((NN_i) * (cipher_texts[i]) * (inverse_i))

cubed = inverse_sum % N_product


getcontext().prec = 55
cube_root = Decimal(cubed) ** (Decimal('1') / Decimal('3'))
final_message = int(cube_root.to_integral_value())
flag = final_message.to_bytes(length_m, byteorder='big').decode('utf')
print(flag)
```

In the solution source code note that

References:
[1]: https://crypto.stackexchange.com/questions/2575/chinese-remainder-theorem-and-rsa

[2]: https://math.stackexchange.com/questions/4020034/using-fermats-little-theorem-and-the-chinese-remainder-theorem

[3] https://www.youtube.com/watch?v=MdePzlQtnCc


## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Examining source code to identify functionality

## Tags

- python

## Attributes

- author: Jai Chauhan (jchauhan)
- organization: picoCTF
- event: Hacking 101
