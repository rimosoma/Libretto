import math
import operator
from dataclasses import dataclass
import flet
cfuTot = 180

#order = true significa che una lista di voti sarebbe ordinabile
@dataclass(order=True)
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

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)

    #definisco il metodo equals che controlla solo voto e materia
    def ugualeMateriaAndPunteggio(self, other):
        return (self.materia == other.materia and
                self.punteggio == other.punteggio and
                self.lode == other.lode)


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

    #questa è una deep copy
    def copy(self):
        """
        crea una nuova copia del libretto
        :return:
        """
        nuovo = Libretto(self.proprietario, [])
        for v in self.voti:
            nuovo.append(v.copy())
        return nuovo

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
        """
        verifica se il libretto contiene gia il voto, l'uguaglianza si ha in base al campo materia e punteggio
        :param votoCercato:
        :return:
        """
        presente = False
        for v in self.voti:
            if v.ugualeMateriaAndPunteggio(votoCercato):
                presente = True
        #if presente:
           # print(f"Voto presente nel libretto : {votoCercato}")
        #else:
            #print(f"il voto di {votoCercato.materia} in cui avrebbe preso {votoCercato.punteggio} non è presente nel libretto ")

        return presente

    def hasConflitto(self, votoConfronto):
        """
        controlla che la coppia di voti non sia in conflitto cioe stessa materia, diversa tupla punti lode
        :param votoConfronto: oggetto voto
        :return: true se il voto in input è in conflitto, senno false
        """

        for v in self.voti:
            if(v.materia == votoConfronto.materia
            and not(v.punteggio == votoConfronto.punteggio and
            v.lode == votoConfronto.lode)):
                return True
        return False


    def creaMigliorato(self):
        """
        Crea un nuovo oggetto libretto in cui i voti sono migliorsti secondo lo schema:
        se è >=18 e <24 aggiungo 1
        se è >=24 e <29 aggiungo 2
        se è 29 aggiungo 1
        se è 30 rimane 30
        :return: nuovo oggetto libretto
        """

        #se creassi un nuovo libretto senza copy, lavorerei sulle stesse istanze
        #nuovo = Libretto(self.proprietario, [])
        #creo dei nuovi oggetti voto per ogni voto nel libretto normale.
        #se facessi una lista copiata non otterrei lo stesso effetto perche lavorerei sulle stesse istanze
        #for v in self.voti:
            #non è bello che questo metodo dipenda da tutti gli attributi di Voto,
            #perche se li cambio sto metodo non funziona piu
            #quindi creo il metodo copy nella classe voto e libretto
            #nuovo.append(Voto(v.materia, v.punteggio,v.data, v.lode))

        nuovo = self.copy()
        #modifico i voti nel nuovo
        for v in nuovo.voti:
            if 18 <= v.punteggio <24:
                v.punteggio += 1
            elif 24<= v.punteggio <29:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30

        return nuovo

    def sortByMateria(self):
        #sfrutto il metodo estraiMateria, è un metodo stand alone(non è un getter)
        #self.voti.sort(key=estraiMateria)
        self.voti.sort(key = operator.attrgetter("materia"))

        #per printare:
        #creo due metodi che si fanno una copia autonoma della lista, la ordinano e la restituiscono
        #poi un altro metodo che stamperà le nuove liste


    def creaLibrOrdinatoPermateria(self):
        """
        crea un nuovo oggetto libretto ordinato per materia
        :return: nuova istanza del libretto
        """
        nuovo = self.copy()
        nuovo.sortByMateria()
        return nuovo

    def creaLibrOrdinatoPerVoto(self):
        """
                crea un nuovo oggetto libretto ordinato per voto
                :return: nuova istanza del libretto
        """
        nuovo = self.copy()
        nuovo.voti.sort(key = lambda v:(v.punteggio,v.lode), reverse=True)
        return nuovo

    def cancellaInferiori(self,punteggio):
        """
        Agisce sul libretto corrente, eliminando tutti i voti inferiori al parametro punteggio
        :param punteggio: intero indicante il lower bound
        :return: oggetto libretto modificato
        """
        #modo 1
        #for i in range(len(self.voti)):
            #if self.voti[i].punteggio < punteggio:
                #self.voti.pop(i)
        #modo 2
        #for v in self.voti:
            #if v.punteggio < punteggio:
                #self.voti.remove(v)
        #modo 3 ---> devo ciclare ma non posso modificare la lista su cui ciclo
        nuovo = []
        for v in self.voti:
            if v.punteggio >= punteggio:
                nuovo.append(v)
        self.voti = nuovo

def estraiMateria(voto):
    """
    questo metodo restituisce il campo materia dell'argomento voto
    :param voto: oggetto voto in input
    :return: stringa rappresentante il nome
    """
    return voto.materia


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
