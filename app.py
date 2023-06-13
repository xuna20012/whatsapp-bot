from wa_automate_socket_client import SocketClient
from pymongo import MongoClient
from datetime import datetime
from time import sleep
from time import time

cluster = MongoClient("mongodb+srv://xuna20012:7815@cluster0.fbwsx7o.mongodb.net/?retryWrites=true&w=majority")
db = cluster["restau"]
clients = db["clients"]
commandes = db["commandes"]

client = SocketClient('http://localhost:27017/')

def reply(message):
    data = message["data"]
    text = data["text"]
    number = data["from"]

    user = clients.find_one({"number": number})

    if bool(user) == False:    #verifir si l'utilisateur existe dans la bd
        #si l'utilisateur n'est pas dans la bd alors dit lui ceci
        client.sendText(number, "Bienvenu Chez *Xuna TECH* !\nCeci est un repondeur automatique\nVeuilleur choisir parmis les options "
                                "ci-dessous: \n\n *Tapez* \n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures "
                                "\n4: Pour connaitre notre Adresse ")
        clients.insert_one({"number": number, "status": "main", "messages": []})  #enreigistrer cet utlisateur dans la bd

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
            #clients.update_one({"number": number}, {"$set": {"status": "ordering"}})      #update status to ordering
            clients.update_one({"number": number}, {"$set": {"status": "choixproduit"}})    #update status to choix de produits
            client.sendText(number, "Vous pouvez choisir parmis les produits suivants:\n\n Tapez \n\n1: Pizza \n2: burger \n"
                                    "3: Tacos \n4: Chandwitch \n5: Fataya\n0: Retourner au menu principal")

        elif option == 3:
            client.sendText(number, "Nous travaillons de 8H a 19h")

        elif option == 4:
            client.sendText(number, "Nous sommes aux HLM G-Y")
        else:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")

    #elif user["status"] == "ordering":
    elif user["status"] == "choixproduit":
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(text)
        if option == 0:
            clients.update_one({"number": number}, {"$set": {"status": "main"}})
            client.sendText(number, "Tapez \n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse")
        elif option == 1:
            clients.update_one({"number": number}, {"$set": {"status": "ordering pizza"}})
            client.sendText(number, "*Le menu Pizza disponible*")
            client.sendImage(number, "img/pizzareine.jpg", "image", "  *Tapez*\n*1:* Pour Mini Pizza Reine\n       *PRIX*: *3500 Fcfa*")
            sleep(1)
            client.sendImage(number, "img/pizzareine1.jpg", "image", "  *Tapez*\n*2:* Pour Big Pizza Reine\n       *PRIX*: *4500 Fcfa*")
            client.sendText(number, "*0*: Pour retourner ↩")

        elif option == 2:
            client.sendText(number, "Oops ! 😔 le Burger n'est pas encore dispo")
        elif option == 3:
            client.sendText(number, "Oops ! 😔 le Tacos n'est pas encore dispo")
        elif option == 4:
            client.sendText(number, "Oops !😔 le Chandwitch n'est pas encore dispo")
        elif option == 5:
            client.sendText(number, "Oops ! 😔 le Fataya n'est pas encore dispo")
        else:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
    #ordering Pizza
    elif user["status"] == "ordering pizza":
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(text)
        if option == 0:
            clients.update_one({"number": number}, {"$set": {"status": "choixproduit"}})
            client.sendText(number, "Vous pouvez choisir parmis les produits suivants:\n\n Tapez \n\n1: Pizza \n2: burger \n"
                            "3: Tacos \n4: Chandwitch \n5: Fataya\n0: Retourner au menu principal")
        #Les Pizza disponibles
        elif 1 <= option <= 2:
            pizza = ["Mini Pizza Reine a 3500 Fcfa","Big Pizza Reine a 4500 Fcfa"]
            selected = pizza[option - 1]
            clients.update_one({"number": number}, {"$set": {"status": "validation"}})
            clients.update_one({"number": number}, {"$set": {"produit": selected}})
            client.sendText(number, "*Excellente choix 😉*")
            sleep(1)
            client.sendText(number, f"Vous venez de choisir *{selected}* ! \n\n*Taper*\n\n1: Pour *Confirmer* votre commande\n2: Pour *Annuler* la commande")
        else:
            client.sendText(number, "SVP veuiller entrer une reponse valide")

    #validation
    elif user["status"] == "validation":
        try:
            option = int(text)
        except:
            client.sendText(number, "SVP veuiller entrer une reponse valide ")
            return str(text)
        if option == 1:
            client.sendText(number, "Merci de nous donner votre *adresse*:")
            clients.update_one({"number": number}, {"$set": {"status": "address"}})
        elif option == 2:
            client.sendText(number, "Votre commade a ete annuler")
            sleep(2)
            clients.update_one({"number": number}, {"$set": {"status": "main"}})
            client.sendText(number,"Vous pouvez choisir parmi l'une des options ci-dessous: "
                            "\n\n*Tapez*\n\n1: Pour nous Contacter \n2: Pour Commander \n3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse")
        else:
            client.sendText(number, "SVP veuiller entrer une reponse valide "
                                    "\n\n*Taper*\n\n1: Pour *Confirmer* votre commande\n2: Pour *Annuler* votre commande ")
    #address
    elif user["status"] == "address":
        selected = user["produit"]
        client.sendText(number, f"Votre commande pour *{selected}* a été reçu et sera livré dans l'heure")
        sleep(1)
        client.sendText(number, "Merci d'avoir utiliser notre service 😉")
        commandes.insert_one({"number": number, "produit": selected, "address": text, "order_time": datetime.now()})
        clients.update_one({"number": number}, {"$set": {"status": "ordered"}})
    elif user["status"] == "ordered":
        client.sendText(number, "Salut, merci de nous avoir contacter de nouveau!\nVous pouvez choisir parmi l'une des options ci-dessous: "
                                "\n\n*Tapez*\n\n1: Pour nous Contacter \n2: Pour Commander \n"
                                "3: Pour connaitre nos Heures \n4: Pour connaitre notre Adresse")
        clients.update_one({"number": number}, {"$set": {"status": "main"}})


    # ajoute les messages que l'utilisateur entre
    clients.update_one({"number": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})
    print("Connection Reussie !")



client.onMessage(reply)
