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




    









    