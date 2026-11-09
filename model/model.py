from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO
from model.biblioteca_DTO import Biblioteca
from model.libro_DTO import Libro

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()
        self._id_map_biblioteche: dict[int, Biblioteca] = {}

    # --- LIBRI ---
    def get_libri_filtrati(self, id_biblioteca: int | None, genere: str | None) -> list[Libro] | None:
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        return self._libro_dao.get_libri_filtrati(id_biblioteca, genere)

    def get_generi(self) -> list[str] | None:
        """Restituisce la lista di tutti i generi."""
        return self._libro_dao.get_all_generi()

    # --- BIBLIOTECHE ---
    def get_biblioteche(self) -> list[Biblioteca] | None:
        """Restituisce la lista di tutte le biblioteche."""
        biblioteche = self._biblioteca_dao.get_all_biblioteche()
        if biblioteche is not None:
            self._id_map_biblioteche = {b.id: b for b in biblioteche}
        return biblioteche

    def get_biblioteca_by_id(self, id_biblioteca: int) -> Biblioteca | None:
        return self._id_map_biblioteche.get(id_biblioteca)