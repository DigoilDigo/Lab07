import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata: int | None = None
        self.genere_selezionato: str | None = None

    # POPOLA DROPDOWN
    def popola_dropdown(self):
        # 1. Popola Dropdown Biblioteche
        self._view.dd_biblioteca.options.clear()
        self._view.dd_biblioteca.options.append(
            ft.dropdown.Option(key="None", text="Nessun filtro")
        )
        biblioteche = self._model.get_biblioteche()
        if biblioteche is None:
            self._view.show_alert("Errore di connessione al database.")
            return

        for b in biblioteche:
            self._view.dd_biblioteca.options.append(
                ft.dropdown.Option(key=str(b.id), text=b.nome)
            )
        self._view.dd_biblioteca.value = "None"

        # 2. Popola Dropdown Generi
        self._view.dd_genere.options.clear()
        self._view.dd_genere.options.append(
            ft.dropdown.Option(key="None", text="Nessun filtro")
        )
        generi = self._model.get_generi()
        if generi is None:
            self._view.show_alert("Errore di connessione al database.")
            return

        for g in generi:
            self._view.dd_genere.options.append(
                ft.dropdown.Option(key=g, text=g)
            )
        self._view.dd_genere.value = "None"

        self._view.update()

    # CALLBACKS DROPDOWN
    def on_select_biblioteca(self, e):
        valore = e.control.value
        if valore is None or valore == "None":
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = int(valore)

    def on_select_genere(self, e):
        valore = e.control.value
        if valore is None or valore == "None":
            self.genere_selezionato = None
        else:
            self.genere_selezionato = valore

    # AZIONE: MOSTRA LIBRI
    def handle_mostra_libri(self, e):
        self._view.lv_libri.controls.clear()

        libri = self._model.get_libri_filtrati(
            self.biblioteca_selezionata,
            self.genere_selezionato
        )

        if libri is None:
            self._view.show_alert("Errore nella lettura dei libri dal database.")
            self._view.update()
            return

        if len(libri) == 0:
            self._view.show_alert("Nessun libro trovato con i criteri di filtraggio selezionati.")
            self._view.update()
            return

        for libro in libri:
            self._view.lv_libri.controls.append(ft.Text(str(libro)))

        self._view.update()