from . import Operasi

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
    Operasi.create(tahun, judul, penulis)
    print("\n Berikut adalah data baru anda")
    read_console()

def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]
        print(f"{index:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
    
    # Footer
    print("="*100+"=")


def update_console():
    read_console()
    while (True):
        print("Silahkan Pilih nomor buku yang akan diupdate")
        no_buku = int(input("Masukkan Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        data_break = data_buku.split(",")
        pk = data_break[0]
        data_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4][:-1]
        if data_buku:
            
            break
        else:
            print("Nomor buku tidak ditemukan")
            
    while(True):
        # data yang ingin di update
        print("\n\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:40}")

        # memilih mode untuk update
        user_option = input("Pilih data [1,2,3] : ")
        print("\n\n"+"="*100)
        match user_option:
            case "1":
                judul = input("Judul\t: ")
            case "2":
                penulis = input("Penulis\t: ")
            case "3":
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
                    except:
                        print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
            case _:
                print("Pilihan tidak valid")
        print("Data Baru Anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:40}")
        is_done = input("Apakah data sudah sesuai? (y/n): ")
        if is_done == "y" or is_done == "Y":
            break
    Operasi.update(pk, no_buku, data_add, judul, penulis, tahun)
    read_console()


def delete_console():
    read_console()
    while (True):
        print("Silahkan Pilih nomor buku yang akan dihapus")
        no_buku = int(input("Masukkan Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            data_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin di update
            print("\n\n"+"="*100)
            print("Data yang ingin anda hapus?")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:40}")
            is_done = input("Apakah data yakin data dihapus? (y/n): ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor buku tidak ditemukan")
    print("Data berhasil dihapus")
        