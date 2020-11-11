import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import sqlite3
import sys


def creat_bd(self):
    connection = sqlite3.connect("dataBase.db")
    cursor = connection.cursor()
# соединение с базой данных, если ее не существует, то создает бд с таким же именем:

con = sqlite3.connect("dataBase.db")

# создание объекта курсора:

cur = con.cursor()

# создание таблицы:

cur.execute ('CREAT TABLE IF NOT EXISTS name_tab (FIO TEXT, '

'Specialnost TEXT, '

'Rost FLOAT) ' )

#заполнение таблицы данными:

cur.execute ('INSERT INTO name_tab VALUES ("Иванов И.И.", "ПКС", 182.5)' )

#подтверждение внесения данных:

con.commit()

#удаляение курсора:

cur.close()

#разрывание соединения с базой:

con.close()
