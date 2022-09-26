import ssl
from flask import Flask, request
from wa_automate_socket_client import SocketClient
from wati_api import client
from pymongo import MongoClient
from datetime import datetime
from time import sleep
import pywhatkit

import mysql.connector


cluster = MongoClient("mongodb+srv://xunafall:7815@cluster0.aeskmp9.mongodb.net/?retryWrites=true&w=majority",tls=True, tlsAllowInvalidCertificates=True)
db = cluster["mybot"]
users = db["users"]
orders = db["orders"]

client = SocketClient('http://localhost:5000/', '778042525cC.')

app = Flask(__name__)
@app.route("/", methods=["get", "post"])

def reply(message, true=None):
    data = message["data"]
    text = data["text"]
    number = data["from"]


    user = users.find_one({"number": number})

    if bool(user) == False:    #verifir si l'utilisateur existe dans la bd
        #si l'utilisateur n'est pas dans la bd alors dit lui ce-ci
        client.sendText(number, "Bienvenu Chez nous !\nCe-ci est un repondeur automatique\nVeuilleur choisir parmis les options "
                                "ci-dessous: \n\n *Tapez* \n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse ")
        users.insert_one({"number": number, "status": "main", "messages": []})  #enreigistrer cet utlisateur dans la bd
    elif user["status"] == "main":   #si l'utilisateur existe deja dans la bd
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(message)
        if option == 1:
            client.sendText(number, "Phone: 78 174 58 98\nMail: cheikhounafall20012@gmail.com")
            client.sendPaymentRequest(number, 10000, "Fcfa", "Payement")

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
            client.sendText(number, "Tapez \n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse")
        elif 1 <= option <= 9:
            cakes = ["Pizza", "Burger", "Tacos", "Chandwitch", "Fataya", "Chawarma", "Poulet", "Frites", "Bolonaise"]
            selected = cakes[option - 1]
            #users.update_one({"number": number}, {"$set": {"status": "address"}})
            users.update_one({"number": number}, {"$set": {"status": "validation"}})
            users.update_one({"number": number}, {"$set": {"item": selected}})
            #client.sendText(number, "Excellente choix 😉")
            #client.sendText(number, "Pour *Confirmer* votre commande, merci de nous donner votre *adresse*")
            client.sendText(number, "*Excellente choix 😉*")
            sleep(1)
            client.sendText(number, f"Vous venez de choisir *{selected}* ! \n\n*Taper*\n\n1: Pour *Confirmer* votre commande\n2: Pour *Annuler* la commande")
        else:
            client.sendText(number,"SVP veuiller entrer une reponse valide")
    elif user["status"] == "validation":
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(text)
        if option == 1:
            client.sendText(number, "Merci de nous donner votre *adresse*:")
            users.update_one({"number": number}, {"$set": {"status": "address"}})
        elif option == 2:
            client.sendText(number, "Votre commade a ete annuler")
            sleep(2)
            users.update_one({"number": number}, {"$set": {"status": "main"}})
            client.sendText(number,"Vous pouvez choisir parmi l'une des options ci-dessous: "
                            "\n\n*Tapez*\n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse")
        else:
            client.sendText(number, "SVP veuiller entrer une reponse valide "
                                    "\n\n*Taper*\n\n1: Pour *Confirmer* votre commande\n2: Pour *Annuler* votre commande ")
    elif user["status"] == "address":
        selected = user["item"]
        client.sendText(number, f"Votre commande pour *{selected}* a été reçu et sera livré dans l'heure")
        sleep(1)
        client.sendText(number, "Merci d'avoir utiliser notre service 😉")
        orders.insert_one({"number": number, "item": selected, "address": text, "order_time": datetime.now()})
        users.update_one({"number": number}, {"$set": {"status": "ordered"}})
    elif user["status"] == "ordered":
        client.sendText(number, "Salut, merci de nous avoir contacter de nouveau!\nVous pouvez choisir parmi l'une des options ci-dessous: "
                                "\n\n*Tapez*\n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse")
        users.update_one({"number": number}, {"$set": {"status": "main"}})


    # ajoute les messages que l'utilisateur entre
    users.update_one({"number":number},{"$push": {"messages": {"text": text, "date": datetime.now()}}})



client.onMessage(reply)
