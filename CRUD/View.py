from . import Operasi


def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang hendak di delete")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            # data yang ingin didelete
            print("\n"+"="*100)
            print("Data Buku")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Apakah anda yakin ingin menghapus data ini?(y/n): ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
            
        else:
            print("nomor tidak valid, silahkan masukkan lagi")

    print("Data berhasil dihapus")

    
def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor buku yang hendak di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index=no_buku)

        data_break = data_buku.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4][:-1]

        if data_buku:
            break
        else:
            print("nomor tidak valid, silahkan masukkan lagi")

    

    while True:
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("Silahkan pilih yang mau di update")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        user_option = input("Pilih data[1,2,3]: ")
        print("\n"+"="*100)
        match user_option:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun\t:  "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Masukkan tahun dengan benar (yyyy)")
                    except:
                        print("tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
            case _ : print("index tidak cocok")

        print("data berhasil diupdate")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        is_done = input("Apakah data sudah sesuai?(y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_buku,pk,date_add,tahun,judul,penulis)

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t:  ")
    judul = input("Judul\t:  ")
    while True:
        try:
            tahun = int(input("Tahun\t:  "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Masukkan tahun dengan benar (yyyy)")
        except:
            print("tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    Operasi.create(tahun,judul,penulis)
    print("data berhasil ditambahkan")
    Operasi.read()

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
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:5}",end="")
        

    # Footer
    print("="*100+"\n")

    

    
