# control.py #

import ui
import requests

def start():
    run = True
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    while run:
        pokemon = ui.main_menu()
        if pokemon is None:
            continue
        else:
            response = requests.get(url)
            print(response.status_code)
