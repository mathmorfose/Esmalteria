#-*- coding: utf-8 -*-
import mysql.connector
from mysql.connector import errorcode
from PySimpleGUI import PySimpleGUI as ig

# Create your own mySQL Connection

con = mysql.connector.connect(host='localhost', user='root', password='yourpassword', database='yourdatabase')
print("Sucessfull Connection!")

c = con.cursor(dictionary=True) #cursor retorna um dicionario

class BANCO_DADOS():
    
    def select(fields, tables, order=None, where=None):
        
        global c
        query = "SELECT " + fields + " FROM " + tables
        if(order):
            query = query + " ORDER BY " + order

        if(where):
            query = query + " WHERE " + where

        try:
            c.execute(query)
        except:
            print("Deu erro no select")

        return c.fetchall()

    def insert(values, table, fields=None):

            global c, con

            query = "INSERT INTO " + table
            if(fields):
                query = query + " (" + fields + ")"

            if(table == 'date'):
                query = query + " VALUES ('" + values + "')"
                print(query)
            elif(table == 'schedule'):
                query = query + " VALUES (default, '" + values +"')"
                print(query)
            else:
                #cada conjunto de dados de values vai ser posto em v, cada v dentro de () e uma , após
                query = query + " VALUES (null," + ",".join(["'" + v + "'" for v in values]) + ")" 

            
            try:
                c.execute(query)
                con.commit()
                return False
            except:
                return True
    
    def insert_foreign_key(date_value, id_time, table):

        global c, con
        query = "INSERT INTO " + table + " VALUES (default, '" + date_value + "'," + str(id_time) + ")"

        try:
            c.execute(query)
            con.commit()
        except:
            print(query)


    def update(sets, table, where=None): 

        global c, con
        query = "UPDATE " + table
        query = query + " SET " + ",".join([field + " = '" + value + "'" for field, value in sets.items()])
        if where:
            query = query + " WHERE " + where

        try:
            c.execute(query)
            con.commit()
        except:
            print(query)

    def delete(table, where):

        global c, con
        query = "DELETE FROM " + table
        query = query + " WHERE " + where
        
        c.execute(query)
        con.commit()

    def add_estoque(item,qntd):

        #ALTER TABLE `lojinha`.`estoque` ADD COLUMN `esmalte` INT NOT NULL AFTER `id_item`;
        global c, con
        query = "ALTER TABLE `lojinha`.`estoque` ADD COLUMN `" + item[0] + "` INT NOT NULL AFTER `id_item`"

        tam = len(BANCO_DADOS.select("*", "estoque"))
        query2 = "INSERT INTO `lojinha`.`estoque` (`id_item`, `" + item[0] + "`) VALUES ('" + str(tam+1) + "', '" + qntd[0] + "')"

        c.execute(query)
        c.execute(query2)
        con.commit()
