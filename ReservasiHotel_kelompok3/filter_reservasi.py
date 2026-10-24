def filter_reservasi(daftar_reservasi):
    print("\n=== FILTER RESERVASI BERDASARKAN STATUS ===")
    print("1. Aktif")
    print("2. Selesai")
    print("3. Dibatalkan")

    pilihan = input("Pilih status (1-3): ").strip()

    pilihan_status = {
        "1": "Aktif",
        "2": "Selesai",
        "3": "Dibatalkan"
    }

    if pilihan not in pilihan_status:
        print("Pilihan status tidak valid.")
        return

    status_pilihan = pilihan_status[pilihan]

    hasil = [
        data for data in daftar_reservasi
        if data["status"].lower() == status_pilihan.lower()
    ]

    print(
        f"\nMenampilkan reservasi dengan status: "
        f"{status_pilihan} ({len(hasil)} data)"
    )

    if not hasil:
        print(
            f"Tidak ada reservasi dengan status "
            f"'{status_pilihan}'."
        )
        return

    print("-" * 100)
    print(
        f"{'Kode':<12} {'Nama Pemesan':<20} "
        f"{'Jenis':<10} {'Detail':<28} {'Tanggal':<12} {'Status'}"
    )
    print("-" * 100)

    for data in hasil:
        print(
            f"{data['kode_reservasi']:<12} "
            f"{data['nama_pemesan']:<20} "
            f"{data['jenis']:<10} "
            f"{data['detail']:<28} "
            f"{data['tanggal']:<12} "
            f"[{data['status'].upper()}]"
        )