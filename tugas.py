def hitung_bonus(performa):
    if performa == "sangat baik":
        bonus = 100000
    elif performa == "baik":
        bonus = 50000
    elif performa == "cukup":
        bonus = 20000
    else:
        performa == "jelek"
        bonus = 0
    return bonus

performa_karyawan = input("Masukkan performa karyawan (sangat baik, baik, cukup, jelek): ")
bonus_karyawan = hitung_bonus(performa_karyawan)
print("Bonus karyawan adalah: ", bonus_karyawan)