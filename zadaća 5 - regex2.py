#Napisati regex za provjeru validnosti unosa e-maila.
#E-Mail mora biti formata ime.prezime@fpmoz.sum.ba
#Nakon toga napisati regex za provjeru eduId koji mora biti formata
#ime.prezimeX@sum.ba 
#X predstavlja bilo koji broj (moze ici u beskonacnost),
#a taj broj ne mora postojati (može biti samo ime.prezime@sum.ba).
#Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
#Istražiti greedy i non-greedy quantifiers.

import re

mail=input("Unesi email:")
eduid=input("Unesi eduId:")

if re.search("^[a-z]+.[a-z]+@fpmoz.sum.ba$",mail):
    print("Email je ispravan")
else:
    print("Email nije ispravan")

if re.search("^[a-z]+.[a-z]+[0-9]*@sum.ba$",eduid):
    print("eduId je ispravan")
else:
    print("eduId nije ispravan")
