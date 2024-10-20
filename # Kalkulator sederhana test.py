# Kalkulator sederhana
while True:
    a = int(input("Masukkan Nilai 1: "))
    b = int(input("Masukkan Nilai 2: "))
# Operasi dalam dictionary   
    operasi = {
    "+": a + b,     # Penjumlahan
    "-": a - b,     # Pengurangan
    "*": a * b,     # Perkalian
    "/": a / b}     # Pembagian

# Tampilkan pilihan operasi
    print("Operasi apa yang ingin dilakukan: +, -, *, /")
    op = input("Masukkan pilihan operasi: ")
# Menampilkan hasil operasi yang dipilih
    print("Hasil: ", operasi.get(op, "Pilihan tidak valid."))
    restart = input("Apakah Anda ingin menggunakannya kembali? (ya/tidak): ").lower()
    if restart != "ya":
        print("Terima kasih telah menggunakan kalkulator sederhana!")
    break



