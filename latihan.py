#Nama:Razzan Ilman Anwar
#Kelas:1C
#Nim:2605982

def fibonachi(x):
    a = 0
    b = 1
    hasil = []
    for i in range(x):
        hasil.append(a)
        a, b = b, a + b
    return hasil
print(fibonachi(10))

#Soal 2 Latihan1
def tabung(phi,r,t):
    volume = phi*r**2*t
    return volume
# print(tabung(22/7,7,10))

#Soal 3 Latihan 1
nilai_masuk = int(input("Berapa nilai yang ingin dimasukkan: "))
angka = []
for i in range(nilai_masuk):
    x = int(input("Angka -"))
    angka.append(x)
def ratarata():
    total = sum(angka)
    rata = print(total / nilai_masuk)
    print(f"Rata-rata: {total}/{nilai_masuk} = {rata}")
    return rata
# print(ratarata())

#Latihan 2
username = "Razzan-Ganteng" 
password = "Ganteng-Banget"
# def login():
    kesempatan = 3
    while kesempatan != 0:
       us = input("Masukkan Ussername: ")
       pw = input("Masukkan Password: ")
       kesempatan -=1
       if pw != password:
        print(f"Kesempatan anda sisa {kesempatan }")
       else:
        print("Selamat Anda berhasil login")
        break
    else:
        print("Kesempatan anda habis")

# login()
# Latihan 3
def konversi(jam,menit,detik):
    return jam*3600 + menit*60 + detik

def baliklagi(total_detik):
    jam = total_detik // 3600
    sisa = total_detik % 3600
    menit = sisa // 60
    detik = sisa % 60
    return jam,menit,detik


def selisih():
    print("===Waktu Mulai===")  
    jam_mulai = int(input("Jam:"))
    menit_mulai = int(input("Menit:"))
    detik_mulai = int(input("Detik:"))

    print("===Waktu Selesai===")
    jam_selesai = int(input("Jam:"))
    menit_selesai = int(input("Menit:"))
    detik_selesai = int(input("Detik:"))

    mulai = konversi(jam_mulai,menit_mulai,detik_mulai)
    selesai = konversi(jam_selesai,menit_selesai,detik_selesai)
    hasil = selesai - mulai
    jam,menit,detik = baliklagi(hasil)
    print("Hitung selisih")
    print(f"{jam}-jam {menit}-menit {detik}-detik")

# selisih()

