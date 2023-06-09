import sqlite3


class Database:
    def __init__(self, file_name):
        self.name = file_name

    def conect(self, movies_tb = 'movies_data', user_tb = 'users_data'):
        self.movies = movies_tb
        self.users = user_tb

        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('message_id' INTEGER, 'file_id', 'caption', 'file_size' INTEGER, 'id' INTEGER PRIMARY KEY);")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('user_id' INTEGER, 'user_name');")

        conection.commit()
        conection.close()
        print(f"database sucsesfuly conected...")

    def add_movi(self, caption, message_id = None, size = 0, file_id = None):
        """
            caption : str
            message_id : int
            size : int
            file_id : str
        """
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        try:
            caption = caption.replace('"', "\'")
            cursor.execute(f"INSERT INTO {self.movies} ('message_id', 'file_id', 'caption', 'file_size') VALUES ({message_id}, '{file_id}', \"{caption}\", {size});")
            print("New movi added ...")
        except:
            print("Datbase Error ...")
        
        conection.commit()
        conection.close()


if __name__ == '__main__':
    database = Database('database.db')
    database.conect()
    database.add_movi('kino"', message_id = 1, size = 0, file_id = 'btenvu2g556ivn')