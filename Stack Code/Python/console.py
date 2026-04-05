"""Program Konversi Suhu (Menu Interaktif)"""

# Utility

def safe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Input tidak valid. Masukkan angka.")


def from_celsius(C):
    return {
        "C": C,
        "R": (4/5) * C,
        "K": C + 273,
        "F": (9/5) * C + 32,
    }


def from_reamur(R):
    C = (5/4) * R
    return from_celsius(C)


def from_kelvin(K):
    C = K - 273
    return from_celsius(C)


def from_fahrenheit(F):
    C = 5/9 * (F - 32)
    return from_celsius(C)


def print_result(res):
    print(f"Konversi Celcius    --> {res['C']} C")
    print(f"Konversi Reamur     --> {res['R']} R")
    print(f"Konversi Kelvin     --> {res['K']} K")
    print(f"Konversi Fahrenheit --> {res['F']} F")
    print("      ----------Selesai----------")


# Menu loop

def main():
    while True:
        print("\n========== Program Konversi Suhu ==========")
        print("1. Dari Celcius")
        print("2. Dari Reamur")
        print("3. Dari Kelvin")
        print("4. Dari Fahrenheit")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-4): ")

        if pilihan == "1":
            C = safe_float("Nominal Derajat Celcius: ")
            print_result(from_celsius(C))
        elif pilihan == "2":
            R = safe_float("Nominal Derajat Reamur: ")
            print_result(from_reamur(R))
        elif pilihan == "3":
            K = safe_float("Nominal Derajat Kelvin: ")
            print_result(from_kelvin(K))
        elif pilihan == "4":
            F = safe_float("Nominal Derajat Fahrenheit: ")
            print_result(from_fahrenheit(F))
        elif pilihan == "0":
            print(">>>>>>>>>> Program Selesai <<<<<<<<<<")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
