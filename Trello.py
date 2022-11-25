import requests
import json

url_list = "https://api.trello.com/1/boards/634d3e85e0a8d3012006aa79/lists"
url_card = "https://api.trello.com/1/lists/634d3e85e0a8d3012006aa80/cards"

headers = {
   "Accept": "application/json"
}

query = {
   'key': '303cf5e171ed248ed9616ca19a39935a',
   'token': '0687479fc81308eda4b62108cc0d0af7ee13959ccf5b660d0ec3adc8a9f0ee2d'
}

response_list = requests.request(
   "GET",
   url_list,
   headers=headers,
   params=query
)

sortie=json.loads(response_list.text)
print(sortie)
nom_listes=[]
id_listes=[]
for k in range(len(sortie)):
    nom_listes.append(sortie[k]["name"])
    id_listes.append(sortie[k]["id"])

nom_cards=[]
for i in range(len(id_listes)):
    response_card = requests.request(
        "GET",
        url_card,
        headers=headers,
        params=query
    )
    nom_cards.append(response_card.text)

print(nom_cards)
print(nom_listes)
print(id_listes)