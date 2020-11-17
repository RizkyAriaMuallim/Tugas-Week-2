arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    Minimum = min(arrBerat)
    Maximum = max(arrBerat)
    mi = print("Berat balita minimum: {:.2f} kg" .format(Minimum))
    ma = print("Berat balita maksimum: {:.2f} kg" .format(Maximum))

    return mi, ma


def rerata(arrBerat):
    total = 0
    panjang = 0
    for j in arrBerat:
        if isinstance(j, float):
            total += j
            panjang += 1

    # Definisikan Proses Mencari Rerata Dari Total Berat
    rata_rata = total / panjang

    # Return Hasil Rerata
    return rata_rata


print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=" ")
    # Inisialisasi Input Data Berat
    berat = float(input())
    
    # Masukkan Data Berat Ke Array (arrBerat)
    arrBerat.append(berat)


# Panggil procedur hitungMinMax(arrBerat)



# Print Data Minimum, Maximum, dan Rerata Berat
hitungMinMax(arrBerat)
print("Rerata berat balita: {:.2f} kg".format(rerata(arrBerat)))