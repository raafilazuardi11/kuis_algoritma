nama = input("Nama mahasiswa : ")

if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Data mahasiswa tidak ditemukan.")
    exit()

print(f"Targetku {target}!")
percobaan = 0
lulus = False

while percobaan < 3:
    percobaan += 1
    nilai = int(input(f"Nilai {percobaan} : "))
    
    if nilai >= target:
        lulus = True
        break

if lulus:
    print(f"{nama.capitalize()} berhasil lulus setelah {percobaan} kali percobaan!")
else:
    print(f"{nama.capitalize()} tidak lulus setelah {percobaan} kali percobaan!")