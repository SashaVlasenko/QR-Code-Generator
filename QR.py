import qrcode
import os

text = input("Введіть текст для QR-кода: ")
filename = input("Введіть ім'я файла для збереження QR-кода: ")

if not filename.lower().endswith(".png"):
    filename += ".png"

qr = qrcode.make(text)
qr.save(filename)
print(f"QR-код збережений в {filename}.")
os.startfile(filename) 