import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
            case "nt":
                os.system("cls")
            case "posix":
                os.system("clear")
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print(40*"=")

    # check database itu ada atau tidak
    CRUD.init_console()


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
        print("4. Delete Buku \n")

        user_option = input("Masukkan Opsi: ")
        match user_option:
            case "1":
                CRUD.read_console()
            case "2":
                CRUD.create_console()
            case "3":
                CRUD.update_console()
            case "4":
                CRUD.delete_console()
            case _:
                print("Opsi Tidak Ditemukan")
        is_done = input("Apakah Selesai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break
    print("Program Selesai, Terimakasih")

