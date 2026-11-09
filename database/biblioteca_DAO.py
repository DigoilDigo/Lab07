from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def get_all_biblioteche(self) -> list[Biblioteca] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database.")
            return None

        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT id, nome, indirizzo
            FROM biblioteca
            ORDER BY nome ASC
        """
        cursor.execute(query)

        for row in cursor:
            result.append(Biblioteca(
                id=row["id"],
                nome=row["nome"],
                indirizzo=row["indirizzo"]
            ))

        cursor.close()
        cnx.close()
        return result