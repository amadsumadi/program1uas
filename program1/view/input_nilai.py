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
