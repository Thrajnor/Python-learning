import os
import time

print("Dzien dobry, Natalio !")
time.sleep(2)
print("Zaraz naprawie te zdjecia, ukazujac zaszyfrowana wiadomosc")
time.sleep(4)
print("Pamietaj aby wlaczyc sortowanie alfabetyczne i widok kafelkowy w folderze, gdzie sa pliki na ktorych pracuje, abys mogla odczytac wiadomosc :)")
time.sleep(10)
print("Walcze z plikami !!!")

def rename_files():
    dire = os.getcwd()
    os.chdir(os.getcwd())
    file_list = os.listdir(dire)
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"0123456789"))

rename_files()

time.sleep(2)

print("Gotowe! juz masz naprawiona liste !!! teraz mozesz wejsc do odpowiednio skonfigurowanego folderu z zdjeciami i odczytac wiadomosc !!!")