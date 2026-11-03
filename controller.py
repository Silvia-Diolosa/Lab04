import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def conferma_selezione_lingua(self, e):
        if self._view.lingua.value == "":
        # meglio fare:
        # if not self._lingua.value:
            self._view.lv.controls.append(ft.Text("Lingua non selezionata, riprovare"))
        else:
            self._view.lv.controls.append(ft.Text("Lingua selezionata con successo: " + self._view.lingua.value))
        self._view.update()

    def conferma_metodo_ricerca(self, e):
        if self._view.metodoRicerca.value == "":
            self._view.lv.controls.append(ft.Text("Lingua non selezionata, riprovare"))
        else:
            self._view.lv.controls.append(ft.Text("Lingua selezionata con successo: " + self._view.metodoRicerca.value))
        self._view.update()

    def handleSpellCheck(self, e):
        self._view.lv.controls.clear()
        if (self._view.lingua.value == ""
          or self._view.metodoRicerca.value == ""
          or self._view.testoInput.value == ""):

            self._view.lv.controls.append(ft.Text("Errore, completare tutti i campi"))
            self._view.update()
            return



        self._view.lv.controls.clear()
        (paroleErrate, tempo) = self.handleSentence(self._view.testoInput.value, self._view.lingua.value, self._view.metodoRicerca.value)
        stampaRiga1 = ft.Text("Frase inserita: " + self._view.testoInput.value)
        stampaRiga2 = ft.Text("Parole errate: " + paroleErrate)
        stampaRiga3 = ft.Text("Tempo richiesto dalla ricerca: " + str(tempo))


        self._view.lv.controls.append(stampaRiga1)
        self._view.lv.controls.append(stampaRiga2)
        self._view.lv.controls.append(stampaRiga3)

        self._view.testoInput.value = ""
        self._view.update()






    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text