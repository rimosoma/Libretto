from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student("Harry","Potter",11,"castani", "azzurri","Grifondoro",
                "civetta", "Expecto Patronum")
mylib = Libretto(Harry, [])
v1 = Voto("Difesa contro le arti oscure", 25, "2022-01-30", False)
v2 = Voto("Babbanologia", 30, "2022-02-12", False)
mylib.append(v1)
mylib.append(v2)

mylib.append(Voto("Pozioni", 21, "2022-03-4", False))

media = mylib.calcolaMedia()
print(f"la tua media attuale è {media}")

votiFiltrati = mylib.getVotiByPunti(21, False)
print(votiFiltrati)

votoCercato = mylib.getVotoByName("Pozioni")
if votoCercato is None:
    print("Voto non trovato")
else:
    print(votoCercato)