import mysql.connector
import pandas as pd
import sqlite3


class SQLServer():
    def __init__(self):
        self.conn = sqlite3.connect('nombre_basedatos.db')
        self.mydb = mysql.connector.connect(
            host="192.168.0.39",
            user="Greg",
            password="Meguiddo",
            database="compilado"
        )

    def insert_data(self):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO compilado_oee (Date, Folio, Event_code, Event_name, Machine, Fabric_code, Fabric_name, Mts, Star_time, End_time, Total_time, Quemador, Turbina, Operador, Supervisor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (
            "2023-10-07", 255856, 55, "Test", "Ingenieria", 75, "Aluminio", 55555, "12:03:29", "12:24:26", 1, True,
            False, "Alex", "Greg")
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")

    def read_from_lite(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM compilado_oee")
        rows = cursor.fetchall()
        print(rows)