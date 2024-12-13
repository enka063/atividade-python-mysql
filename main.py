import mysql.connector
from pymongo import MongoClient
#
def connect_mysql():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root!123",
        database="restaurante"
    )
def connect_mongo():
    return MongoClient("mongodb://localhost:27017/")
#
#-------------------------------------------------------------
#
def create_mysql():
    conn = connect_mysql()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pedidos (nome_cliente, prato, quantidade, preco_total, data_pedido) VALUES (%s, %s, %s, %s, %s)",
                   ("João", "Pizza", 2, 30.00, "2024-12-13"))
    conn.commit()
    conn.close()
#
def read_mysql():
    conn = connect_mysql()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pedidos")
    for row in cursor.fetchall():
        print(row)
    conn.close()
#
def update_mysql():
    conn = connect_mysql()
    cursor = conn.cursor()
    cursor.execute("UPDATE pedidos SET preco_total = %s WHERE id_pedido = %s", (35.00, 1))
    conn.commit()
    conn.close()
#
def delete_mysql():
    conn = connect_mysql()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pedidos WHERE id_pedido = %s", (1,))
    conn.commit()
    conn.close()
#
#-------------------------------------------------------------
#
def create_mongo():
    client = connect_mongo()
    db = client["meu_banco_mongo"]
    collection = db["pedidos"]
    data = {"nome_cliente": "Ana", "prato": "Macarrão", "quantidade": 1, "preco_total": 15.00, "data_pedido": "2024-12-13"}
    collection.insert_one(data)
#
def read_mongo():
    client = connect_mongo()
    db = client["meu_banco_mongo"]
    collection = db["pedidos"]
    for doc in collection.find():
        print(doc)
#
def update_mongo():
    client = connect_mongo()
    db = client["meu_banco_mongo"]
    collection = db["pedidos"]
    collection.update_one({"nome_cliente": "Ana"}, {"$set": {"preco_total": 18.00}})
#
def delete_mongo():
    client = connect_mongo()
    db = client["meu_banco_mongo"]
    collection = db["pedidos"]
    collection.delete_one({"nome_cliente": "Ana"})
#
#-------------------------------------------------------------
#
if __name__ == "__main__":
    create_mysql()
    read_mysql()
    update_mysql()
    delete_mysql()
#
    create_mongo()
    read_mongo()
    update_mongo()
    delete_mongo()
#