import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
skull = r"""
       ______
     .-"      "-.
    /            \
   |,  .-.  .-.  ,|
   | )(_o/  \o_)( |
   |/     /\     \|
   (_     ^^     _)
    \__|IIIIII|__/
     | \IIIIII/ |
     \          /
      `--------`
"""
RED = '\033[91m'
WHITE = '\033[97m'
RESET = '\033[0m'
clear()
print(WHITE + skull + RESET)
print(RED + "        Eska" + RESET)
time.sleep(1)
print("\nТаңдауыңызды енгізіңіз:")
print("1. Email")
print("2. Номер")
choice = input("1 немесе 2 енгізіңіз: ")
if choice == "1":
    email = input("Дұрыс email-ді енгізіңіз: ")
    print(f"\nСіз Email таңдадыңыз: {email}")
elif choice == "2":
    number = input("Номерді енгізіңіз: ")
    print(f"\nСіз Number таңдадыңыз: {number}")
else:
    print("\nҚате таңдау!")
print("\nБағдарлама аяқталды (бұл тек демонстрация).")

