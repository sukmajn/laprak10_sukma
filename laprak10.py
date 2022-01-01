# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 06:16:20 2022

@author: Sukma Julia Nada
"""

list_nama = []
list_nilai = []


def input_data():
    print("[1. INPUT DATA]")
    praktikum = []
    list_nama.append(input("Masukkan nama mahasiswa: "))

    for i in range(3):
        praktikum.append(int(input("Masukkan nilai praktikum {}: ".format(i + 1))))

    list_nilai.append(praktikum)
    print("")


def view_data():
    print("[2. VIEW DATA]\n NAMA | PRAK 1 | PRAK 2 | PRAK 3\n--------------------------------")
    for nama, nilai in zip(list_nama, list_nilai):
        prak1, prak2, prak3 = nilai
        print(nama, "\t", prak1, "\t", prak2, "\t", prak3)
    print("")


def hitung_rerata_mhs():
    print("[3. HITUNG RATA-RATA PRAK TIAP MAHASISWA]")
    nm = len(list_nilai)
    temp_rerata = [0] * nm
    for i in range(nm):
        nilai = list_nilai[i]
        hasil = 0
        np = len(nilai)
        for j in range(np):
            hasil += nilai[j]
        temp_rerata[i] = hasil / np

    for nama, rata2 in zip(list_nama, temp_rerata):
        print(nama, "=", rata2)
    print("")


def hitung_rerata_prak():
    print("[4. HITUNG RATA-RATA TIAP PRAK]")
    nm = len(list_nilai)
    nilai_prak = [0, 0, 0]

    for i in range(nm):
        nilai = list_nilai[i]
        np = len(nilai)
        for j in range(np):
            if j == 0:
                nilai_prak[0] += nilai[j]
            elif j == 1:
                nilai_prak[1] += nilai[j]
            else:
                nilai_prak[2] += nilai[j]

    for i in range(len(nilai_prak)):
        print("Rerata Prak {}=".format(i + 1), nilai_prak[i] / nm)
    print("")


def cari_rerata_prak_mhs():
    print("[5. MENCARI NILAI RATA-RATA PRAK TIAP MAHASISWA]")
    nama_mhs = input("Masukkan nama mahasiswa: ").capitalize()
    if nama_mhs in list_nama:
        indeks = list_nama.index(nama_mhs)
        print("Rerata nilai praktikum {} =".format(nama_mhs), sum(list_nilai[indeks]) / len(list_nilai[indeks]), "\n")


def update_nilai_prak():
    print("[6. UPDATE NILAI PRAK MAHASISWA]")
    nama_mhs = input("Masukkan nama mahasiswa: ").capitalize()
    if nama_mhs in list_nama:
        indeks = list_nama.index(nama_mhs)
        prak_ke = int(input("Ingin update nilai praktikum ke-: "))
        if 0 < prak_ke < 4:
            nilai_baru = int(input("Nilai baru: "))
            list_nilai[indeks][prak_ke - 1] = nilai_baru
            print("")


def mulai():
    while True:
        pilihan = input("PROGRAM LIST\n"
                        "1. Input Data\n"
                        "2. View Data\n"
                        "3. Hitung Nilai Rata-Rata Praktikum Tiap Mahasiswa\n"
                        "4. Hitung Nilai Rata-Rata Tiap Praktikum\n"
                        "5. Mencari Nilai Rata-Rata Praktikum Mahasiswa\n"
                        "6. Update Nilai Praktikum Mahasiswa\n"
                        "7. Exit\n"
                        "Pilih menu yang tersedia: ")
        print("")

        if pilihan == "1":
            input_data()

        elif pilihan == "2":
            view_data()

        elif pilihan == "3":
            hitung_rerata_mhs()

        elif pilihan == "4":
            hitung_rerata_prak()

        elif pilihan == "5":
            cari_rerata_prak_mhs()

        elif pilihan == "6":
            update_nilai_prak()

        elif pilihan == "7":
            print("[7. EXIT]\nTERIMA KASIH!")
            break
        else:
            print("Pilih 1, 2, 3, 4, 5, 6 atau 7 untuk keluar\n")


if __name__ == "__main__":
    mulai()