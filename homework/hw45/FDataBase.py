import sqlite3
import math


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из базы данных")
        return []

    def add_curse(self, title, cost, text):
        try:
            self.__cur.execute("INSERT INTO curses VALUES(NULL, ?, ?, ?)", (title, cost, text))
            self.__db.commit()
            return True
        except sqlite3.Error as e:
            print("Ошибка добавления курса в базу данных" + str(e))
            return False

    def get_curse(self, curse_id):
        try:
            self.__cur.execute(f"SELECT title, text, cost FROM curses WHERE id={curse_id}")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из базы данных" + str(e))
        return False, False, False

    def get_curse_announce(self):
        try:
            self.__cur.execute("SELECT id, title, text, cost FROM curses")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курсов из базы данных" + str(e))
        return []
