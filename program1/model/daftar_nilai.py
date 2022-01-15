# data awal
d_nim = []
d_nama = []
d_kelas = []
d_jurusan = []
d_hadir = []
d_tugas = []
d_uts = []
d_uas = []
d_akhir = []

def judul():
    print("=============================================")
    print("|       Program Nilai Data Mahasiswa        |")
    print("=============================================")

def menu():
    judul()
    print("=============================================")
    print("|1. Tambah Data Mahasiswa                   |")
    print("|2. Tampilkan Data Mahasiswa                |")
    print("|3. Hapus Data Mahasiswa                    |")
    print("|4. Ubah Data Mahasiswa                     |")
    print("|5. selesai                                 |")
    print("=============================================")
    pilih = input("pilih menu : ")
    if pilih == "1":
        tambah()
    elif pilih == "2":
        tampilkan()
    elif pilih == "3":
        hapus()
    elif pilih == "4":
        ubah()
    elif pilih == "5":
        selesai ()
    else:
        tidak = input('menu tidak ada ')
        menu()

def tampilkan():
    global i
    judul()

    for i in range(len(d_nim)):

        print("%d. nama          :%s" % (i + 1, d_nama[i]))
        print("   nim            :%s" % d_nim[i])
        print("   nama           :%s" % d_nama[i])
        print("   kelas          :%s" % d_kelas[i])
        print("   jurusan        :%s" % d_jurusan[i])
        print("   hadir          :%s" % d_hadir[i])
        print("   nilai tugas    :%s.2f" % d_tugas[i])
        print("   nilai uts      :%s.2f" % d_uts[i])
        print("   nilai uas      :%s.2f" % d_uas[i])
        print("   nilai akhir    :%s.f" % d_akhir[i])
        print("=====================================================")
    kembali = input("kembali tekan [ENTER]")
    menu()

def tambah():
    judul()
    print("Tambahkan Data Mahasiswa".center(40))
    print("========================================")
    jurusan = input ("prodi [TI/SI] : ")
    if jurusan == "TI" or jurusan == "TI":
         j = "teknik informatika"
        d_jurusan.append(j)
    elif jurusan == "SI" or jurusan == "SI":
         j = "sistem informasi"
         d_jurusan.append(j)
    else:
        kembali = input ("pilihan tidak ada")
        tambah()
    nama = input
    d_nama.append(nama)
    nim = input("nim : ")
    d_nim.append(nim)
    kelas = input("kelas : ")
    d_kelas.append(kelas)

    system("cls")
    judul()
    print("tambah data".center(40))
    print("=================================")
    hadir = float(input("jumlah hadir : "))
    d_hadir = ((hadir/16)*20/100)*100
    d_hadir.append(d_hadir)

    tugas = float(input("nilai tugas : "))
    d_tugas = tugas * (30 / 100)
    d_tugas.append(d_tugas)

    uts = float (input("nilai uts : "))
    d_uts = uts*(35 / 100)
    d_uts.append(d_uts)

    uas = float (input("nilai uas : "))
    d_uas = uas(35 / 100)
    d_uas.append(d_uas)

    total = d_tugas + d_uts + d_uas
    d_akhir.append(total)
    print("simpan data".center(40))
    kembali = input("kembali [enter]")
    menu()

def hapus():
    judul()
    print("Hapus Data".center(40))
    print("========================================")
    i = int(input("masukkan id : "))

    if (i > len(d_nim[i])):
        tidak = input("nim tidak ada")
        hapus()

    else:
        d_nama.remove(d_nama[i])
        d_nim.remove(d_nim[i])
        d_kelas.remove(d_kelas[i])
        d-jurusan.remove(d_jurusan[i])
        d_hadir.remove(d_hadir[i])
        d_tugas.remove(d_tugas[i])
        d_uts.remove(d_uts[i])
        d_uas.remove(d_uas[i])
        d_akhir.remove(d_akhir[i])

        print("data berhasil dihapus")
        kembali = input("kembali tekan [enter]")
        menu()

def ubah():
    ubah = input("ubah biodata / nilai [B/N] : ")
    if ubah == "B" or ubah == "b":
        i = int(input("masukan id : "))
        if (i > len(d_nim[i])):
            print("id salah")
        else:
            nimbaru = input("nim : ")
            d_nim[i] = nimbaru

            namabaru = input("nama : ")
            d_nama[i] = namabaru

    else:
        i = int(input("masukkan id : "))
        if (i > len(d_nim[i])):
            print("id salah")
        else:
            tugas = float(input("nilai tugas : "))
            d_tugas = tugas * (30 / 100)
            d_tugas[i] = d_tugas

            uts = float(input("nilai uts : "))
            d_uts = uts * (35 / 100)
            d_uts[i] = d_uts

            uas = float(input("nilai uas : "))
            d_uas = uas * (35 / 100)
            d_uas[i] = d_uas

            nilaiakhir = d_tugas + d_uts + d_uas
            d_akhir[i] = d_akhir
        kembali = input("kembali tekan [enter]")
        menu()


def selesai():
    menu()


# tampilkan
# tambah
# hapus
# ubah
# keluar
def mahasiswa():
    judul()
    d_nim = input("masukkan nim : ")
    for i in range(len(d_nim)):
        if d_nim == d_nim[i]:
            print("_____________________________")
            print("no           : ", d_no[i])
            print("Nim          : ", d_nim[i])
            print("Nama         : ", d_nama[i])
            print("Tugas        : ", d_tugas[i])
            print("UTS          : ", d_uts[i])
            print("UAS          : ", d_uas[i])
            print("_____________________________")
            print("Nilai Akhir  : ", d_akhir[i])
            break

    else:
        tidak = input("Data Tidak ada")
        mahasiswa()

    kembali = input("kembali tekan [enter]")
    menu()


menu()