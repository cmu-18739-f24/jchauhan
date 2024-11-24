# jchauhan

- Namespace: picoctf/18739c
- ID: jchauhan
- Type: custom
- Category: Binary Exploitation
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Running

This problem should be able to run with cmgr.

## Description

This problem has a vulnerable string, can you exploit it?

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

The program's source code can be downloaded {{url_for("format_vuln.c", "here")}} and the binary can be downloaded {{url_for("format_vuln", "here")}}.

## Hints

- Look up format string vulnerablilities in C

- There is a certain formatting parameter within printf that can be used to modify values.

## Solution Overview

The vulnerability in this program is at the following line: 

`printf(user_input);`

which prints the user input without specifying the %s format parameter.

Note that since printf is a variable parameter function and parameters are read from the stack. In normal usage, the number of format parametes should equal the number of parameters. However, when there are more format parameters than parameters, printf may begin to read variables outside of its stack frame.

First note that by default the first 6 parameters to printf are paseed through registes, so we will need at least 6 format parameters, before printf can start reading from the stack.

`%x.%x.%x.%x.%x.%x.%x.%x`

Next view the source code and note how there are there are 3 local variables on the stack:

1. ` int not_important`

2. `int value`

3. `int *ptr`

It turns out that `ptr` can be accessed with three more `%x` format parameters.

Printf actually contains a `%n` format parameter which will write the current number of bytes printed into a given pointer. It is interesting to find string format parameters that actually modify values. 

This leads to the full payload:
`%x.%x.%x.%x.%x.%x.%x.%x.%n`

Now `*ptr = <number of bytes written>` will be different than 13, leading to the flag.



References:
[1]: https://web.ecs.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf

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

- author: jchauhan
- organization: picoCTF
- event: picoCTF Problem Developer Training
