import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def poczatek_print():
    print("[1.] Średnia")
    print("[2.] Liczba osób na statku")
    print("[3.] Klasy biletów")
    print("[4.] Ilość osób, które przetrwały i zginęły")
    print("[5.] Histogram")
    print("[6.] Wykresy")
    print("[7.] Wnioski")
    print("[0.] wyjście")

#Funkcja do liczenia średniej podając kolumnę i nazwe pliku
def oblicz_srednia(data, kolumna):
    df = pd.read_csv(data)
    srednia = df[kolumna].mean()
    
    return round(srednia, 2)

def segment_srednie():
    print("--- Wybierz 1 / 2 ---")
    print("1. Średnia wieku")
    print("2. Średnia opłaty")
    
    user_choice = input("Podaj liczbę: ")
    
    if user_choice == "1":
        print("Średnia wieku wynosi: ", oblicz_srednia(nazwa_pliku, "Age"))
    elif user_choice == "2":
        print("Średnia opłat wynosi: ", oblicz_srednia(nazwa_pliku, "Fare"))

def segment_osoby(data):
    print("--- Wybierz 1 / 2 / 3 ---")
    print("[1.] Liczba osób")
    print("[2.] Liczba kobiet")
    print("[3.] Liczba mężczyzn")
    
    user_choice = input("Podaj liczbę: ")
    
    df = pd.read_csv(data)
    
   
    count_men = count = df[df['Sex'] == 'male'].shape[0]
    count_female = count = df[df['Sex'] == 'female'].shape[0]
    all_people = count_men + count_female

def segment_klasa_biletow(data):
    df = pd.read_csv(data)
    
    first_class = df[df['Pclass'] == 1].shape[0]
    second_class = df[df['Pclass'] == 2].shape[0]
    third_class = df[df['Pclass'] == 3].shape[0]
    
    print("---------------------------------------------")
    print("Ilość biletów pierwszej klasy: ", first_class)
    print("Ilość biletów drugiej klasy: ", second_class)
    print("Ilość biletów trzeciej klasy: ", third_class)
    print("---------------------------------------------")

def segment_zycie_smierc(data):
    df = pd.read_csv(data)
    d1 = df['Survived']
    
    survived = df[d1 == 1].shape[0]
    died = df[df['Survived'] == 0].shape[0]
    
    woman_alive = df[df["Sex"] == "female"]["Survived"].value_counts()[1]
    men_alive = df[df["Sex"] == "male"]["Survived"].value_counts()[1]
    
    print("--------------------------")
    print("Ilość przetrwałych osób: ", survived)
    print("Ilość osób, które zginęły: ", died)
    print("Ilość kobiet, które przeżyły: ", woman_alive)
    print("Ilość mężczyzn, którzy przeżyli: ", men_alive)
    print("--------------------------")

def segment_wykresy(data):
    df = pd.read_csv(data)

    print("[1.] Wykres między [płeć, wiek, klasa biletu]")
    print("[2.] Wykres między klasą biletów a ilością zgonów")

    user_choice = input("Podaj liczbę: ")

    if user_choice == "1":
        df.groupby('Sex')['Age', 'Pclass'].mean().plot.bar()
        plt.show()
    if user_choice == "2":
        grouped_data = df.groupby('Pclass')['Survived'].agg('count')
        grouped_data.plot(kind='bar', color='blue', edgecolor='black')
        plt.title('Number of Deaths by Ticket Class')
        plt.xlabel('Ticket Class')
        plt.ylabel('Number of Deaths')
        plt.show() 


def segment_histogram(data):
    df = pd.read_csv(data)

    print("[1.] Histogram wieku")
    print("[2.] Histogram wieku ofiar")
    print("[3.] Histogram opłat")
    
    user_choice = input("Podaj liczbę: ")
    
    if user_choice == "1":
        n, bins, patches = plt.hist(df["Age"], bins=20, color='blue', alpha=0.7)
        plt.title('Histogram')
        plt.show()
    if user_choice == "2":
        wiek_ofiar = df[df["Survived"] == 0]["Age"]
        n, bins, patches = plt.hist(wiek_ofiar, bins=20, color='blue', alpha=0.7)
        plt.title('Histogram')
        plt.show()
    elif user_choice == "3":
        n, bins, patches = plt.hist(df["Fare"], bins=20, color='blue', alpha=0.7)
        plt.title('Histogram')
        plt.show()

def wnioski():
    print("Płeć: Statystyki wskazują, że mężczyźni mieli niższą szansę na przeżycie niż kobiety.")
    print("Klasa biletu: Pasażerowie pierwszej klasy mieli wyższą szansę na przeżycie niż pasażerowie niższych klas.")
    print("Miejsce w kabinie: Miejsce w kabinie, w którym pasażerowie się znajdowali, może również wpłynąć na ich szansę na przeżycie.")

nazwa_pliku = "train.csv"
while(True):
    poczatek_print()
    user_input = input("Wybierz liczbę: ")
    
    if user_input == "0":
        break

    elif user_input == "1":
        segment_srednie()
    elif user_input == "2":
        segment_osoby(nazwa_pliku)
    elif user_input == "3":
        segment_klasa_biletow(nazwa_pliku)
    elif user_input == "4":
        segment_zycie_smierc(nazwa_pliku)
    elif user_input == "5":
        segment_histogram(nazwa_pliku)
    elif user_input == "6":
        segment_wykresy(nazwa_pliku)
    elif user_input == "7":
          wnioski()
