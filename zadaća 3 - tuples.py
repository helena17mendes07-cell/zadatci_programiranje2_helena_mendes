#Iz podataka učitanih u prethodnom primjeru sortirati listu po prezimenima.
#Napraviti novi rječnik gdje će se po bodovnom rangu upisivati broj
#ostvarenih ocjena. 
#Nedovoljan 0-49%
#Dovoljan 50-65%
#Dobar 65-80%
#Vrlodobar 80-90%
#Izvrstan 90-100%

#pošto mi se nisu željeli učitat prethodni
#podaci iskoristila sam svoje kolege za primjer

studenti=[
    ("Natalija","Jovanović",55),
    ("Helena","Mendeš",78),
    ("Petar","Živković",92),
    ("Petar","Kopić",45),
    ("Sven","Filipović",85),
    ("Emanuel","Marković",67),
    ("Paul","Dominković",95)
]

ocjene={}

for ime,prezime,bodovi in studenti:

    if bodovi < 50:
        ocjena = "Nedovoljan"
    elif bodovi <= 65:
        ocjena = "Dovoljan"
    elif bodovi <= 80:
        ocjena = "Dobar"
    elif bodovi <=90:
        ocjena = "Vrlodobar"
    else:
        ocjena = "Izvrstan"

    if ocjena in ocjene:
        ocjene[ocjena]+=1
    else:
        ocjene[ocjena]=1

print(ocjene)
