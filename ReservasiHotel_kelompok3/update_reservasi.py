def update_reservasi(daftar_reservasi):
    print("\n=== UPDATE STATUS RESERVASI ===")

    kode = input("Masukkan kode reservasi: ").strip()

    data_ditemukan = None

    for data in daftar_reservasi:
        if data["kode_reservasi"].lower() == kode.lower():
            data_ditemukan = data
            break

    if data_ditemukan is None:
        print(f"Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    if data_ditemukan["status"] != "Aktif":
        print("Status reservasi ini sudah final dan tidak dapat diubah.")
        return

    print(f"Nama pemesan: {data_ditemukan['nama_pemesan']}")
    print(f"Status lama : {data_ditemukan['status']}")
    print("\nPilih status baru:")
    print("1. Selesai")
    print("2. Dibatalkan")

    pilihan = input("Pilihan (1/2): ").strip()

    if pilihan == "1":
        status_baru = "Selesai"
    elif pilihan == "2":
        status_baru = "Dibatalkan"
    else:
        print("Pilihan status tidak valid.")
        return

    status_lama = data_ditemukan["status"]
    data_ditemukan["status"] = status_baru

    print(
        f"Status reservasi {kode} atas nama "
        f"{data_ditemukan['nama_pemesan']} berhasil diperbarui: "
        f"{status_lama} menjadi {status_baru}."
    )