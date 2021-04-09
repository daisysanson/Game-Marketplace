import sqlite3

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect('videogames.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT rating from Games"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        r = [x[0] for x in records]
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    # finally:
    #     if sqliteConnection:
    #         sqliteConnection.close()
    #         print("The SQLite connection is closed")

readSqliteTable()