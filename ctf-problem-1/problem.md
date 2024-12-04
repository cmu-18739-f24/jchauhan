# Format Strings Fun

- Namespace: picoctf/18739f24
- ID: format-strings-fun
- Type: custom
- Category: Binary Exploitation
- Points: 100
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

- C

## Attributes

- author: Jai Chauhan (jchauhan)
- organization: picoCTF
- event: 18739 CTF
