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
                type_list = []
                data = response.json()
                print()
                print(f"Name   : {data["name"]}")
                print(f"ID     : {data["id"]}")
                print(f"Height : {data["height"]}")
                print(f"Weight : {data["weight"]}")
                for type_data in data["types"]:
                    type_list.append(type_data["type"]["name"])
                print(f"Types  : {", ".join(type_list)}")
            else:
                print()
                print(f"No info about pokemon {pokemon}")
                continue

