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
- event: 18739 CTF
