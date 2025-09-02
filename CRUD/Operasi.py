from . import Database
from .Util import random_string
import time


def create(tahun, judul, penulis):
    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun) 

    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data tidak ditemukan, silahkan membuat data baru")

def create_first_data():

    penulis = input("Masukkan penulis: ")
    judul = input("Masukkan judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
    

    data = Database.TEMPLATE.copy()
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun) 
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["judul"]},{data["penulis"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")

def read():
    try:
        with open(Database.DB_NAME, "r", encoding="utf-8") as file:
            content = file.readlines()
            return content
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        return False