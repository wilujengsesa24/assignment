# SOAL NOMOR 1
print('==========SOAL NOMOR 1==========')
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

# Contohnya:
suhu_kelvin = 315.0
suhu_celsius = kelvin_to_celsius(suhu_kelvin)
print(f"{suhu_kelvin} Kelvin sama dengan {suhu_celsius:.2f} Celsius")

suhu_celsius = 45.0
suhu_kelvin = celsius_to_kelvin(suhu_celsius)
print(f"{suhu_celsius} Celsius sama dengan {suhu_kelvin} Kelvin")

#SOAL NOMOR 2
print('==========SOAL NOMOR 2==========')
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def suhu_to_fahrenheit(suhu, unit):
    if unit.lower() == 'celsius':
        # Jika suhu dalam Celcius
        kelvin = celsius_to_kelvin(suhu)
    elif unit.lower() == 'kelvin':
        # Jika suhu dalam Kelvin
        kelvin = suhu
    else:
        # Jika unit tidak valid
        raise ValueError("Unit tidak valid. Gunakan 'celsius' atau 'kelvin'.")

    # Konversi suhu dari Kelvin ke Fahrenheit
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

# Contohnya:
suhu_celsius = 45.0
fahrenheit_from_celsius = suhu_to_fahrenheit(suhu_celsius, 'celsius')
print(f"{suhu_celsius} Celsius sama dengan {fahrenheit_from_celsius:.2f} Fahrenheit")

suhu_kelvin = 315.0
fahrenheit_from_kelvin = suhu_to_fahrenheit(suhu_kelvin, 'kelvin')
print(f"{suhu_kelvin} Kelvin sama dengan {fahrenheit_from_kelvin:.2f} Fahrenheit")

#SOAL NOMOR 3
print('==========SOAL NOMOR 3==========')
def fahrenheit_to_suhu(fahrenheit, output_unit):
    """
    Mengkonversi suhu dari Fahrenheit ke Celsius atau Kelvin.

    Parameters:
    - fahrenheit (float): Nilai suhu dalam Fahrenheit.
    - output_unit (str): Satuan suhu keluaran, 'C' untuk Celsius, 'K' untuk Kelvin.

    Returns:
    - float: Nilai suhu dalam satuan yang diinginkan.
    """
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15

    if output_unit.upper() == 'C':
        return celsius
    elif output_unit.upper() == 'K':
        return kelvin
    else:
        print("Satuan suhu keluaran tidak valid. Gunakan 'C' untuk Celsius atau 'K' untuk Kelvin.")

# Contohnya:
fahrenheit_value = 79.0
celsius_output = fahrenheit_to_suhu(fahrenheit_value, 'C')
print(f"{fahrenheit_value} Fahrenheit sama dengan {celsius_output:.2f} Celsius")

kelvin_output = fahrenheit_to_suhu(fahrenheit_value, 'K')
print(f"{fahrenheit_value} Fahrenheit sama dengan {kelvin_output:.2f} Kelvin")
