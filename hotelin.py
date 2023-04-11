# Fungsi Garis
def garis():
    print("================")

# Input Tipe Kamar
def table():
    print("| Hari     | Superior      | Deluxe        | Premium       |")
    print("| 1-2 hari | 100.000/night | 150.000/night | 200.000/night |")
    print("| 3-4 hari | 90.000/night  | 135.000/night | 180.000/night |")
    print("| >=5 hari | 80.000/night  | 120.000/night | 160.000/night |")

def pilih():
    print("1. superior")
    print("2. deluxe")
    print("3. premium")

table()
pilih()
tipe_kamar = int(input("Masukkan Tipe Kamar        : "))
lama_inap = int(input("Masukkan Lama Menginap     : "))

# Superior, Deluxe, Premium
if tipe_kamar == 1:
    if lama_inap <= 2:
        harga_kamar = 100000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 90000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 80000*lama_inap
elif tipe_kamar == 2:
    if lama_inap <= 2:
        harga_kamar = 150000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 135000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 120000*lama_inap 
elif tipe_kamar == 3:
    if lama_inap <= 2:
        harga_kamar = 200000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 180000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 160000*lama_inap

# output
garis()
print("Kamar Yang Anda Pilih : ", tipe_kamar)
print("Lama Menginap : ", lama_inap, " Hari")
print("Total Harga Yang Dibayar   : Rp ", harga_kamar)

back = ("Program selesai")
home = input("apakah ingin memesan lagi? (Y/N)")

if home == ("Y") or ("y") :
    table()
    pilih()
    tipe_kamar = int(input("Masukkan Tipe Kamar        : "))
    lama_inap = int(input("Masukkan Lama Menginap     : "))
    if tipe_kamar == 1:
        if lama_inap <= 2:
         harga_kamar = 100000*lama_inap
        elif lama_inap <= 4:
            harga_kamar = 90000*lama_inap
        elif lama_inap >= 5:
            harga_kamar = 80000*lama_inap
    elif tipe_kamar == 2:
        if lama_inap <= 2:
            harga_kamar = 150000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 135000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 120000*lama_inap 
    elif tipe_kamar == 3:
        if lama_inap <= 2:
         harga_kamar = 200000*lama_inap
    elif lama_inap <= 4:
        harga_kamar = 180000*lama_inap
    elif lama_inap >= 5:
        harga_kamar = 160000*lama_inap
    garis()
    print("Kamar Yang Anda Pilih : ", tipe_kamar)
    print("Lama Menginap : ", lama_inap, " Hari")
    print("Total Harga Yang Dibayar   : Rp ", harga_kamar)
else:
    back