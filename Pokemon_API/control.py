# control.py #

import ui
import requests

def start():
    run = True
    main_url = "https://pokeapi.co/api/v2/pokemon/"
    while run:
        pokemon = ui.main_menu()
        if pokemon is None:
            continue
        else:
            url = main_url + pokemon
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print()
                print(f"Name   : {data["name"]}")
                print(f"ID     : {data["id"]}")
                print(f"Height : {data["height"]}")
                print(f"Weight : {data["weight"]}")
            else:
                print(f"No info about pokemon {pokemon}")
                continue

