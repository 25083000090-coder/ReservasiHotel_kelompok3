def hapus_reservasi(daftar_reservasi):
    print("\n=== HAPUS RESERVASI ===")

    kode = input("Masukkan kode reservasi: ").strip()

    indeks_ditemukan = None

    for indeks, data in enumerate(daftar_reservasi):
        if data["kode_reservasi"].lower() == kode.lower():
            indeks_ditemukan = indeks
            break

    if indeks_ditemukan is None:
        print(f"Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    data = daftar_reservasi[indeks_ditemukan]

    print("\nDetail reservasi yang akan dihapus:")
    print(f"Kode         : {data['kode_reservasi']}")
    print(f"Nama pemesan : {data['nama_pemesan']}")
    print(f"Jenis        : {data['jenis']}")
    print(f"Detail       : {data['detail']}")
    print(f"Tanggal      : {data['tanggal']}")
    print(f"Status       : {data['status']}")

    konfirmasi = input(
        "\nYakin ingin menghapus reservasi ini? (y/n): "
    ).strip().lower()

    if konfirmasi == "y":
        daftar_reservasi.pop(indeks_ditemukan)

        print(
            f"Reservasi {data['kode_reservasi']} atas nama "
            f"{data['nama_pemesan']} berhasil dihapus dari sistem."
        )
    else:
        print("Penghapusan dibatalkan.")