from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry","Potter",11,"castani", "azzurri","Grifondoro",
                "civetta", "Expecto Patronum")
mylib = Libretto(Harry, [])
v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 30, "2022-02-12", False)
v3 = Voto("Analisi", 22, "2022-02-30", False)
v4 = Voto("Chimica", 30, "2022-02-10", True)
v5 = Voto("Algebra", 24, "2022-02-15", False)
v6 = Voto("Fisica", 18, "2022-01-20", False)
v7 = Voto("Informatica", 30, "2022-01-23", True)
v8 = Voto("Geografia", 22, "2021-01-24", False)
v9 = Voto("Freschezza", 30, "2021-01-25", True)
v10 = Voto("Pozioni", 21, "2022-03-4", False)
mylib.append(v1)
mylib.append(v2)
mylib.append(v3)
mylib.append(v4)
mylib.append(v5)
mylib.append(v6)
mylib.append(v7)
mylib.append(v8)
mylib.append(v9)
mylib.append(v10)

media = mylib.calcolaMedia()
print(f"la tua media attuale è {media}")

votiFiltrati = mylib.getVotiByPunti(22, False)
print(votiFiltrati)

votoCercato = mylib.getVotoByName("Pozioni")
if votoCercato is None:
    print("Voto non trovato")
else:
    print(votoCercato)

#creo un voto gia esistente nel libretto
v10doppio = Voto("Pozioni", 21, "2022-03-4", False)
#controllo se lo trova nel libretto
mylib.votoGiaPresente(v10doppio)

#creo un nuovo voto non presente nel libretto
vNonPres = Voto("Pozioni", 22, "2022-03-10", False)
#controllo se lo trova
mylib.votoGiaPresente(vNonPres)

#provo a inserire un voto duplicato nel libretto
mylib.append(v10doppio)

#provo a inserire un voto con stesso nome ma punteggio diverso
print(mylib.hasConflitto(Voto("Difesa contro le arti oscure", 21, "2022-01-30", False)))

#provo il nuovo libretto migliorato
print("---------------------------------------------------------------------------")
print("LIBRETTO ORIGINARIO")
print(mylib)
print("")
print("LIBRETTO MIGLIORATO")
nuovoLibretto = mylib.creaMigliorato()
print(nuovoLibretto)


#testo l'ordinamento
print("-------------------------------------------------------------------------------")
print("LIBRETTO ORDINATO PER MATERIA")
ordinato = mylib.creaLibrOrdinatoPermateria()
print(ordinato)

print("-------------------------------------------------------------------------------")
print("LIBRETTO ORDINATO PER VOTO")
ordinato2 = mylib.creaLibrOrdinatoPerVoto()
print(ordinato2)

print("------------------------------------------------------------------------------")
print("LIBRETTO A CUI ELIMINO I VOTI INFERIORI DI 24")
ordinato2.cancellaInferiori(24)
print(ordinato2)

