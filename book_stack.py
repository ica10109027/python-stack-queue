stack = []

def tambahan_buku(stack,nama_buku,nama_pengarang):
    buku_baru=[nama_buku,nama_pengarang]
    stack.append(buku_baru)
    print(f"{buku_baru}berhasil ditambah ke dalam stack")

def hapus_buku_terakhir(stack):
    if len(stack)==0:
        print("stack kosong,tidak ada buku yang dapat dihapus.")
    else:
        buku_terakhir=stack.pop()
        print(f"{buku_terakhir}berhasil dihapus dari stack")

def tampilan_buku_teratas(stack):
    if len(stack)==0:
        print("stack kosong, tidak ada buku yang ditampilkan.")
    else:
        buku_teratas = stack[-1]
        print(f"buku teratas di dalam stack adalah {buku_teratas}.")

while True:
    print("\nTumpukan buku sat ini :",stack)
    print("menu:")
    print("1. tambah buku")
    print("2. hapus buku terakhir")
    print("3. tampilkan buku teratas")
    print("4. keluar")

    pilihan = input("masukan pilihan anda (1/2/3/4) :")

    if pilihan =="1":
        nama_buku=input("masukan buku yang ditambahkan:")
        nama_pengarang=input("masukan nama pengarang yang akan ditambahkan:")
        tambahan_buku(stack,nama_buku,nama_pengarang)
    elif pilihan=="2":
        hapus_buku_terakhir(stack)
    elif pilihan=="3":
        tampilan_buku_teratas(stack)
    elif pilihan=="4":
        print("terima kasih telah menggunakan program ini.")
        break
    else:
        print("pilihan tidak valid. silahkan masukan pilihan")

        
