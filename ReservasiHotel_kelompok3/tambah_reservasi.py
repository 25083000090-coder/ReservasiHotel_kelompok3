from datetime import datetime

def tambah_reservasi(daftar_reservasi):
    print("\n=== TAMBAH RESERVASI KAMAR HOTEL ===")

    kode = input("Masukkan kode reservasi: ").strip()

    if len(kode) < 3:
        print("Kode reservasi minimal 3 karakter.")
        return

    for data in daftar_reservasi:
        if data["kode_reservasi"].lower() == kode.lower():
            print("Kode reservasi sudah digunakan.")
            return

    nama = input("Masukkan nama pemesan: ").strip()

    if not nama:
        print("Nama pemesan tidak boleh kosong.")
        return

    jenis_kamar = input(
        "Jenis kamar (Standard/Deluxe/Suite): "
    ).strip().title()

    if jenis_kamar not in ["Standard", "Deluxe", "Suite"]:
        print("Jenis kamar tidak valid.")
        return

    nomor_kamar = input("Masukkan nomor kamar: ").strip()

    if not nomor_kamar:
        print("Nomor kamar tidak boleh kosong.")
        return

    tanggal = input(
        "Masukkan tanggal reservasi (YYYY-MM-DD): "
    ).strip()

    try:
        datetime.strptime(tanggal, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan YYYY-MM-DD.")
        return

    reservasi = {
        "kode_reservasi": kode,
        "nama_pemesan": nama,
        "jenis": "Ruangan",
        "detail": f"Kamar {jenis_kamar} nomor {nomor_kamar}",
        "tanggal": tanggal,
        "status": "Aktif"
    }

    daftar_reservasi.append(reservasi)

    print(
        f"Reservasi {kode} atas nama {nama} "
        "berhasil ditambahkan."
    )