from database.DB_connect import DBConnect
from model.sighting import Sighting
from model.state import State

class DAO:
    @staticmethod
    def load_years ():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select s.s_datetime   
                    from sighting s  """

        cursor.execute(query)

        for row in cursor:
            anno = str (row ["s_datetime"])
            result.append(anno [0:4])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def load_sightings ():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *   
                    from sighting s
                    where s.shape != "" """

        cursor.execute(query,)

        for row in cursor:
            result.append (Sighting (**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def load_states ():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select *   
                    from state s """

        cursor.execute(query,)

        for row in cursor:
            result.append (State (**row))

        cursor.close()
        conn.close()
        return result

