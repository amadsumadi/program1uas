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