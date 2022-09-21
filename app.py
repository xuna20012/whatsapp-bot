from wa_automate_socket_client import SocketClient
from wati_api import client
from pymongo import MongoClient
from datetime import datetime
import mysql.connector


cluster = MongoClient("mongodb+srv://ouna:7815@cluster0.sq0kuyg.mongodb.net/?retryWrites=true&w=majority")
db = cluster["dbase"]
users = db["users"]
orders = db["orders"]

client = SocketClient('http://localhost:5000/', '778042525cC.')

def reply(message):
    data = message["data"]
    text = data["text"]
    number = data["from"]
    id = data["id"]

    user = users.find_one({"number": number})

    if bool(user) == False:    #verifir si l'utilisateur existe dans la bd
        #si l'utilisateur n'est pas dans la bd alors dit lui ce-ci
        client.sendText(number, "Bienvenu Chez nous \n\n Tapez \n\n1: Contacter \n2: Commander \n3: Heures \n4: Adresse ")
        users.insert_one({"number": number, "status": "main", "messages": []})  #enreigistrer cet utlisateur dans la bd
    elif user["status"] == "main":   #si l'utilisateur existe deja dans la bd
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(message)
        if option == 1:
            client.sendText(number, "Phone: 78 174 58 98\nMail: cheikhounafall20012@gmail.com")
        elif option == 2:
            client.sendText(number, "Vous etes sur la page des commandes")
            users.update_one({"number": number}, {"$set": {"status": "ordering"}})    #update status to ordering
            client.sendText(number, "Vous pouvez choisir parmis les produits suivants:\n\n Tapez \n\n1: Pizza \n2: burger \n"
                                    "3: Tacos \n4: Chandwitch \n5: Fataya \n6: Chawarma\n7: Poulet \n8: Frites \n9: Bolonaise"
                                    " \n0: Retourner au menu principal")
        elif option == 3:
            client.sendText(number, "Nous travaillons de 8H a 19h")

        elif option == 4:
            client.sendText(number, "Nous sommes aux HLM G-Y")
        else:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
    elif user["status"] == "ordering":
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(text)
        if option == 0:
            users.update_one({"number": number}, {"$set": {"status": "main"}})
            client.sendText(number, "Tapez \n\n1: Contacter \n2: Commander \n3: Heures \n4: Adresse")
        elif 1 <= option <= 9:
            cakes = ["Pizza", "Burger", "Tacos", "Chandwitch", "Fataya", "Chawarma", "Poulet", "Frites", "Bolonaise"]
            selected = cakes[option - 1]
            users.update_one(
                {"number": number}, {"$set": {"status": "address"}})
            users.update_one(
                {"number": number}, {"$set": {"item": selected}})
            client.sendText(number, "Excellente choix 😉")
            client.sendText(number, "Pour *Confirmer* votre commande, merci de nous donner votre *adresse*")
        else:
            client.sendText(number,"SVP veuiller entrer une reponse valide")
    elif user["status"] == "address":
        selected = user["item"]
        client.sendText(number, f"Votre commande pour *{selected}* a été reçu et sera livré dans l'heure")
        client.sendText(number, "Merci d'avoir utiliser notre service 😉")
        orders.insert_one({"number": number, "item": selected, "address": text, "order_time": datetime.now()})
        users.update_one({"number": number}, {"$set": {"status": "ordered"}})
    elif user["status"] == "ordered":
        client.sendText(number, "Salut, merci de nous avoir contacter de nouveau !\nVous pouvez choisir parmi l'une des options ci-dessous: "
                                "\n\n*Tapez*\n\n 1: Contacter \n2: Commander \n3: Heures \n4: Adresse")
        users.update_one({"number": number}, {"$set": {"status": "main"}})
    


    users.update_one({"number":number},{"$push": {"messages": {"text": text, "date": datetime.now()}}})
    #ajoute les messages que l'utilisateur a entrer

client.onMessage(reply)
