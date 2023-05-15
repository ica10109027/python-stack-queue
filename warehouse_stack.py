
stack = []
def tambah_barang(stack,barang_baru):
    stack.append(barang_baru)
    print(f"{barang_baru} berhasil ditambahkan ke dalam stack.")

def hapus_barang_terakhir(stack):
    if len(stack) == 0:
        print("stack kosong, tidak ada barang yang dapat dihapus.")
    else:
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir} berhasil dihapus dari stack.")

def tampilkan_barang_teratas(stack):
    if len(stack) == 0:
        print("stack kosong,tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print(f"barang teratas di dalam stack adalah {barang_teratas}.")

while True:
    print("\nGudang saat ini:",stack)
    print("menu:")
    print("1. Tambah barang")
    print("2. Hapus barang terakhir")
    print("3. Tampilkan barang teratas")
    print("4. keluar")

    pilihan = input("masukan pilihan anda (1/2/3/4)")
    if pilihan == "1":
        barang_baru =input("masukan nama barang yang akan  ditambahkan:")
        tambah_barang(stack,barang_baru)
    elif pilihan == "2":
        hapus_barang_terakhir(stack)
    elif pilihan == "3":
        tampilkan_barang_teratas(stack)
    elif pilihan == "4":
        print("terima kasih telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid. silahkan masukkan pilihan yang benar")