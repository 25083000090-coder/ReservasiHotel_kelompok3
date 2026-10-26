def tampilkan_reservasi(daftar_reservasi):
    print("\n=== DAFTAR SEMUA RESERVASI ===")

    if not daftar_reservasi:
        print("Belum ada data reservasi yang tersimpan.")
        return

    print("-" * 110)
    print(
        f"{'No':<4} {'Kode':<12} {'Nama Pemesan':<20} "
        f"{'Jenis':<10} {'Detail':<28} {'Tanggal':<12} {'Status'}"
    )
    print("-" * 110)

    for nomor, data in enumerate(daftar_reservasi, start=1):
        print(
            f"{nomor:<4} "
            f"{data['kode_reservasi']:<12} "
            f"{data['nama_pemesan']:<20} "
            f"{data['jenis']:<10} "
            f"{data['detail']:<28} "
            f"{data['tanggal']:<12} "
            f"[{data['status'].upper()}]"
        )

    print("-" * 110)
    print(f"Jumlah reservasi: {len(daftar_reservasi)}")