
from tambah_reservasi import tambah_reservasi
from tampilkan_reservasi import tampilkan_reservasi
from cari_reservasi import cari_reservasi
from update_reservasi import update_reservasi
from filter_reservasi import filter_reservasi
from hapus_reservasi import hapus_reservasi


def menu_uji_coba():
    daftar_reservasi = []

    while True:
        print("\n" + "=" * 45)
        print("          SISTEM RESERVASI HOTEL")
        print("=" * 45)
        print("1. Tambah Reservasi")
        print("2. Tampilkan Reservasi")
        print("3. Cari Reservasi")
        print("4. Update Reservasi")
        print("5. Filter Reservasi")
        print("6. Hapus Reservasi")
        print("0. Keluar")
        print("=" * 45)

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_reservasi(daftar_reservasi)

        elif pilihan == "2":
            tampilkan_reservasi(daftar_reservasi)

        elif pilihan == "3":
            cari_reservasi(daftar_reservasi)

        elif pilihan == "4":
            update_reservasi(daftar_reservasi)

        elif pilihan == "5":
            filter_reservasi(daftar_reservasi)

        elif pilihan == "6":
            hapus_reservasi(daftar_reservasi)

        elif pilihan == "0":
            print("Uji coba selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    menu_uji_coba()
