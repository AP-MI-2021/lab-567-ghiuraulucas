from Tests.test_all import run_all_tests
from UI.consola2 import menu2
from UI.console import run_menu


def main():
    run_all_tests()
    meniu = input("Va rugam sa alegeti meniul: meniu1 sau meniu2: tastati '1' pentru meniu1 sau '2' pentru meniu2. ")
    if meniu == "1":
        run_menu([])
    if meniu == "2":
        menu2()
main()