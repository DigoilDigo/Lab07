from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def get_all_generi(self) -> list[str] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database.")
            return None

        result = []
        cursor = cnx.cursor()
        query = """
            SELECT DISTINCT genere
            FROM libro
            WHERE genere IS NOT NULL
            ORDER BY genere ASC
        """
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])

        cursor.close()
        cnx.close()
        return result

    def get_libri_filtrati(self, id_biblioteca: int | None, genere: str | None) -> list[Libro] | None:
        cnx = DBConnect.get_connection()
        if cnx is None:
            print("Errore di connessione al database.")
            return None

        result = []
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT id, titolo, autore, genere, anno_pubblicazione, id_biblioteca
            FROM libro
            WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
              AND genere = COALESCE(%s, genere)
            ORDER BY titolo ASC
        """
        cursor.execute(query, (id_biblioteca, genere))

        for row in cursor:
            result.append(Libro(
                id=row["id"],
                titolo=row["titolo"],
                autore=row["autore"],
                genere=row["genere"],
                anno_pubblicazione=row["anno_pubblicazione"],
                id_biblioteca=row["id_biblioteca"]
            ))

        cursor.close()
        cnx.close()
        return result