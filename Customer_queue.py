class Customer:
    def __init__(self,name,transaction_time):
        self.name=name
        self.transaction = transaction

class Queue:
    def __init__(self):
        self.queue=[]

    def is_empty(self):
        return len(self.queue)==0
        
    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    
    def display_next_transaction(self):
        if self.is_empty():
            print("Antrian Kosong")
        else:
            customer = self.queue[0]
            print(f"Transaksi berikutnya: {customer.transaction} - {customer.name}")
            
    def remove_completed_transaction(self):
        if self.is_empty():
            print("Antrian Kosong")
        else:
            customer = self.queue.pop(0)
            print(f"Transaksi selesai: {customer.transaction} - {customer.name}")
            
while True:
    print("\nAntrian saat ini:")
    print("Menu:")
    print("1. Tambah Transaksi")
    print("2. Transaksi Berikutnya")
    print("3. Hapus Transaksi")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        name = input("Masukkan nama pelanggan: ")
        transaction = input("Masukkan jenis transaksi: ")
        customer = Customer(name, transaction)
        print("Transaksi berhasil ditambahkan")
    elif pilihan == "2":
        queue.display_next_transaction()
    elif pilihan == "3":
        queue.remove_completed_transaction()
    elif pilihan == "4":
        print("Terima kasih telah menggunakan program ini.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
        