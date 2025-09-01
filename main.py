import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    while(True):
        match sistem_operasi:
            case "nt":
                os.system("cls")
            case "posix":
                os.system("clear")
        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print(40*"=")
        print("1. Lihat Buku")
        print("2. Buat Buku")
        print("3. Update Buku")
        print("4. Delte Buku \n")

        user_option = input("Masukkan Opsi: ")

        print(40*"=")

        match user_option:
            case "1":
                print("Lihat Buku")
            case "2":
                print("Buat Buku")
            case "3":
                print("Update Buku")
            case "4":
                print("Delete Buku")
            case _:
                print("Opsi Tidak Ditemukan")
        print(40*"=")
        is_done = input("Apakah Selesai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break
    print("Program Selesai, Terimakasih")

