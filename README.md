# shellcode-of-legends

Je m'ennuiais du coup j'ai fait ça, largement inspiré de https://codepen.io/cshaver/pen/AbMmqv

Encode et décode des shellcodes en utilisant une liste de mots liés à League of Legends. Chaque byte est mappé à un mot de la wordlist.

## Utilisation

- `encoder.py` : Transforme un shellcode (bytes) en une suite de mots
- `decoder.py` : Transforme une suite de mots en shellcode (bytes)
- `decoder.c` : Transforme une suite de mots en shellcode mais en c (directement prêt à l'emploi dans un malware)