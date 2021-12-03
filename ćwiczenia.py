# Codenga.pl - Python developer

print('PYTHON - DATA SCIENTIST')

print('Opis:'
      '-dostępny dla wszystkich popularnych platform systemowych,'
      '-prosta składnia,'
      '-stale rozwijany,'
      'ogólnego przeznaczenie (aplikacje web, desktop, AI automatyzacja, programy obliczeniowe.')

print('Zmienne') #wyswietla dowolny tekst
a = 'Pan ' #zmienne tekstowe
b = 'Baran '
c = 123 #zmienne liczbowe
d = True #zmienne typu prawda/fałsz
print(a + b) # przykład

print('Dane tekstowe = String') # ' = "
print('Operacje na stringach')
print(b[2]) #zwraca daną na podanej pozycji(indeksie) w zmiennej - zawsze zaczyna się od 0
print(b[2:4]) #zwraca dane z pozycji dalej niż 2, aż do 5
print('p' in a) #zwraca true/false jeśli dany znak znajduje się w zmiennej WIELKOŚĆ LITER MA ZNACZENIE
print(b.find('ara')) #zwraca indeks danych w zmiennej, jeśli nie ma zwraca wartość -1

print('Dane liczbowe')
print('Liczby calkowite = 1; 4; -15; 300 - Integer')
print('Liczby zmiennoprzecinkowe = 3.3; 14.11; -21.1 - Float') #UWAGA zamiast ',' dajemy '.'
print('Operatory matematyczne')
f = 3 + 4 #dodawanie
f = f - 8 #odejmowanie
f = f * 3 #mnożenie
f = f / 3 #dzielenie
f = f // 3 #dzielenie Integer (do l. całkowitych)
f = f ** 3 #potęgowanie
f = f % 3 #modulo - reszta z dzielenia

print('Operowanie na zmiennych')

e = 2
e += 3
e -= 3
e *= 3
e /= 3

print('Nie można łączyć wartości różnych typów, wymaga to konwersji')
#polecenia konwersji
type(a) #sprawdzanie typu danych
str(a) #konwersja do string
int(c) #konwersja do integer
float(c) #konwersja do float

print('Operatory logiczne')
print(c == 3) #czy jest równe
print(e != 1) #czy jest różne
print(e < c) #czy jest mniejsze lub większe < , >
print(c <= 200) #czy jest większe równe, mniejsze równe <= , >=
print(c == 3 and e < 1) #oraz - oba warunki muszą być spełnione
print(c < 3 or e == 0) #lub - jeden warunek musi być spełniony
print(not c == 3) #czy wartość zaprzecza

print('Instrukcje')
if c == 123: #jeżeli spełniony zostanie warunek, wykona się kod
      print(f)
else: #jeżeli warunek nie zostanie spełniony wykona się kod
      print(a)
#lub inaczej
g = 123
if g <= 100: #jeżeli spełniony zostanie warunek, wykona się kod
      print(f + c)
elif g <= 150: #jeżeli spełniony zostanie dodatkowy warunek, wykona się kod - elif dodaje kolejne warunki
      print(c - f)
else: #jeżeli nie zostanie spełniony warunek, wykona się kod
      print(f)

print('Pętla while')
counter = 1 #indeks pętli
while counter <= 10: #warunek zakończenia pętli
      print(counter) #wykonanie pętli
      counter += 1 #podniesienie indeksu
#komplikacja pętli
id_a = 1
while id_a <= 10:
      if id_a == 7: #jeśli spełniony jest warunek to:
            break #break - pętla jest przerwywana, continue - wartość jest 'pomijana'
      print(id_a)
      id_a += 1

print('Pętla for')
#schemat:
#for zmienna in sekwencja
    #wykonaj jakąś akcję
h = ['ux/ui','frontend','backend'] #w nawiasach [] tworzymy listę
for i in h: #pętla dla listy
      print(i)
#generowanie wartości
for j in range(2,10,5): #funkcja range() generuje wartości, w nawiasie zawieramy warunek:
      print(j)          #(5) generujemy 5 kolejnych liczb od 0, (2,5) generujemy od do,
                        # (2,5,2) generujemy od do co którąś liczbę

print('Funkcje')
def sum(a, b): #def pozwala ustalanie własnej funkcji
      return a + b #określa działanie funkcji - zwracaną wartość
result = sum(15, 3)
print(result)

def hello(name):
      print('Witaj ' + name) #określa działanie funkcji
print(hello('Piotrek'))