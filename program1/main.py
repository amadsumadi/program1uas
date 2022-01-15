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
