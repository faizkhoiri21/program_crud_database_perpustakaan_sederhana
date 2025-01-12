from . import Operasi

DB_NAME = "database.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            file.read()
            #print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
        
            
            
    
