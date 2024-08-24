print('Hello! \n To jest program, który generuje spersonalizowaną kartkę urodzinową')
print("Jak masz na imie?")

my_name = input()
print("Hello, {}".format(my_name))
print("Napisać, proszę, imię osoby, którą chcesz pozdrowić.")
person_name = input()
print("Bardzo dziękuję.")
print("Napisać, w którym roku urodziła się ta osoba.")
birth_year = int(input())
import datetime
current_year = datetime.datetime.now().year
print("Rozumiem. A teraz proszę uprzejmie napisać szczere życzenia dla tej osoby.")
wish = input()
print("Super! Oto wygenerowane życzenia:\n \n")
result = current_year - birth_year
age = result
print(person_name + ", wszystkiego najlepszego z okazji "+ str(age) +" urodzin!\n" +
wish + "\n" + my_name)
