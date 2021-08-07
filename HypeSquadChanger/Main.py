from controller.HypeSquadChanger import HypeSquadChanger
from colorama import init
from os import system

class Main:

    def __init__(self):
        init(autoreset = True)
        HypeSquadChanger()
        system("pause")

Main()