#import os
import CRUD as CRUD

if __name__ == "__main__":
    #sistem_operasi = os.name

    #match sistem_operasi:
        #case "posix": os.system("clear")
        #case "nt": os.system("cls")

    #print("\nSELAMAT DATANG DI PROGRAM")
    #print("DATABASE PERPUSTAKAAN")
    #print("=========================")

    # check database itu ada atau tidak
    CRUD.init_console()
    
    while(True):
        #match sistem_operasi:
            #case "posix": os.system("clear")
            #case "nt": os.system("cls")

        print("\nSELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")

        user_option = input("Masukkan opsi: ")

        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
            case _ : print("index tidak cocok")

        is_done = input("Apakah ingin keluar dari program?(y/n): ")
        if is_done == "y" or is_done == "Y":
            break

    print("Akhir dari program, terima kasiiiiih kakakk")
