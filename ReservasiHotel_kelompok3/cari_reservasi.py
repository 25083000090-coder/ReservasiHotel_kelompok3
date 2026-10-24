def cari_reservasi(daftar_reservasi):
    print("\n=== CARI RESERVASI ===")
    print("1. Cari berdasarkan kode reservasi")
    print("2. Cari berdasarkan nama pemesan")

    pilihan = input("Pilih pencarian (1/2): ").strip()

    if pilihan not in ["1", "2"]:
        print("Pilihan pencarian tidak valid.")
        return

    kata_kunci = input("Masukkan kata kunci: ").strip()

    if not kata_kunci:
        print("Kata kunci tidak boleh kosong.")
        return

    if pilihan == "1":
        hasil = [
            data for data in daftar_reservasi
            if data["kode_reservasi"].lower() == kata_kunci.lower()
        ]
    else:
        hasil = [
            data for data in daftar_reservasi
            if kata_kunci.lower() in data["nama_pemesan"].lower()
        ]

    if not hasil:
        print(
            f"Reservasi dengan kata kunci "
            f"'{kata_kunci}' tidak ditemukan."
        )
        return

    print(f"\nDitemukan {len(hasil)} reservasi:")

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