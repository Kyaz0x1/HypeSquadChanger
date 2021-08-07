from type.HypeSquad import HypeSquad
from view.View import View
from colorama import Fore
import requests
import json

class HypeSquadChanger:

    API_ENDPOINT = "https://discord.com/api/v9/hypesquad/online"

    def __init__(self):
        self.get_token()

    def get_token(self):
        self.token = input("Informe o token: ")
        self.get_hypesquad_options(self)

    @staticmethod
    def get_hypesquad_options(self):
        View.show_menu("HypeSquadChanger\n\tEscolha abaixo o tipo de HypeSquad", *HypeSquad.keys(), "Sair")
        
        try:
            option = int(input("* Escolha uma opção: "))

            if option in (1, 2, 3, 4):
                if option == 4:
                    print(Fore.RED + "Encerrando aplicação...");
                    return;
                hypesquad = HypeSquad.get_by_value(option)
                self.change(self.token, hypesquad)
            else:
                print(Fore.RED + "A opção escolhida é inválida, tente novamente!")
                self.get_hypesquad_options(self)
        except ValueError:
            print(Fore.RED + "A opção escolhida deve ser um número, tente novamente!")
            self.get_hypesquad_options(self)

    @staticmethod
    def change(token: str, hypesquad: HypeSquad):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }
        data = {
            "house_id": hypesquad.value
        }

        response = requests.post(HypeSquadChanger.API_ENDPOINT, headers = headers, data = json.dumps(data))
        
        if response.status_code == 204:
            print(f'{Fore.GREEN}Seu hypesquad foi alterado para {hypesquad.name}!')
        else:
            print(f'{Fore.RED}Ocorreu um erro ao alterar o Hypesquad! Erro: {response.content}')