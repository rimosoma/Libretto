import math
from dataclasses import dataclass
import flet
cfuTot = 180

@dataclass
class Voto:
    materia: str
    punteggio: int
    data: str
    lode: bool


    #definisco il metodo toString
    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

    #definisco il metodo equals tra voti
    def __eq__(self, other):
        if self.materia == other.materia and self.punteggio == other.punteggio and self.lode == other.lode and self.data == other.data:
            return True

    #definisco il metodo equals che controlla solo voto e materia
    def ugualeMateriaAndPunteggio(self, other):
        if self.materia == other.materia and self.punteggio == other.punteggio:
            return True
        else:
            return False

class Libretto:
    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto): # duck!
        if self.votoGiaPresente(voto) == False:
            self.voti.append(voto)
        else:
            print(f"il voto di {voto.materia} in cui ha preso {voto.punteggio} è gia registrato")


    def __str__(self):
        mystr = f"Libretto voti di {self.proprietario} \n"
        for v in self.voti:
            mystr += f"{v} \n"
        return mystr

    def __len__(self):
        return len(self.voti)

    def calcolaMedia(self):
        """
        restituisce la media dei voti presenti nel punteggio
        :return: valore numerico della media oppure ValueError se la lista è vuota
        """
        if len(self.voti) == 0:
            raise ValueError("Attenzione, lista esami vuota")
        voti = [v.punteggio for v in self.voti]    #crea una nuova lista fatta dai punteggi(voti interi)
        return sum(voti) / len(voti)                #potrei fare math.mean(voti)


    def getVotiByPunti(self, punti, lode):
        """
        Filtra i voti in base al punteggio in input
        :param punti: variabile di tipo intero che rappresenta il puntrggio
        :param lode: variabile booleana che indica la presenza della lode
        :return:lista di voti corrispondenti ai parametri
        """
        votiFiltrati = []
        for v in self.voti:
            if v.punteggio == punti and v.lode == lode:
                votiFiltrati.append(v)                  #posso fare l'opzione append con il voto perche è un dataclass
        return votiFiltrati                                #altrimenti dovrei fare il metodo __

    def getVotoByName(self, nome):
        """
        restituisce oggetto voto con campo materia uguale al nome in input
        :param nome: nome della materia
        :return: oggetto di tipo voto
        """
        for v in self.voti:
            if v.materia == nome:
                return v

    def votoGiaPresente(self, votoCercato):
        presente = False
        for v in self.voti:
            if v.ugualeMateriaAndPunteggio(votoCercato):
                presente = True
        if presente:
            print(f"Voto presente nel libretto : {votoCercato}")
        else:
            print(f"il voto di {votoCercato.materia} in cui avrebbe preso {votoCercato.punteggio} non è presente nel libretto ")

        return presente



def testVoto():
    print("Ho usato Voto in maniera standalone")
    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
    print(v1)

    mylib = Libretto(None, [v1, v2])
    print(mylib)
    mylib.append(v3)
    print(mylib)



if __name__ == "__main__":
    testVoto()


# class Voto:
#     def __init__(self, materia, punteggio, data, lode):
#         if  punteggio == 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = lode
#         elif punteggio < 30:
#             self.materia = materia
#             self.punteggio = punteggio
#             self.data = data
#             self.lode = False
#         else:
#             raise ValueError(f"Attenzione, non posso creare un voto con punteggio {punteggio}")
#     def __str__(self):
#         if self.lode:
#             return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
#         else:
#             return f"In {self.materia} hai preso {self.punteggio} il {self.data}"
