from wa_automate_socket_client import SocketClient
from pymongo import MongoClient
from datetime import datetime
from time import sleep
from time import time
import json

cluster = MongoClient("mongodb+srv://xunapro:7815@cluster0.wtllgul.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
db = cluster["xunafall"]
clients = db["users"]
commandes = db["services"]

client = SocketClient('http://localhost:27017/')


# Chargement des messages à partir du fichier config.json
with open('config.json', encoding='utf-8') as config_file:
    config_data = json.load(config_file)

# Messages du chatbot via le fichier json
welcome_message = config_data["welcome_message"]
return_to_welcome_message = config_data["return_to_welcome_message"]
invalid_option_message = config_data["invalid_option_message"]
menu_des_packs = config_data["menu_des_packs"]
retour_au_menu_des_packs = config_data["retour_au_menu_des_packs"]
menu_indsponible = config_data["menu_indsponible"]
Renouveler_votre_assurance = config_data["Renouveler_votre_assurance"]
Trouver_une_agence = config_data["Trouver_une_agence"]
menu_du_pack_ganale = config_data["menu_du_pack_ganale"]
retour_au_menu_du_pack_ganale = config_data["retour_au_menu_du_pack_ganale"]
pack_ganale_ete_choisi = config_data["pack_ganale_ete_choisi"]
menu_du_pack_sope = config_data["menu_du_pack_sope"]
retour_au_menu_du_pack_sope = config_data["retour_au_menu_du_pack_sope"]
pack_sope_a_ete_choisit = config_data["pack_sope_a_ete_choisit"]
menu_du_pack_vip = config_data["menu_du_pack_vip"]
retour_au_menu_du_pack_vip = config_data["retour_au_menu_du_pack_vip"]
pack_vip_a_ete_choisit = config_data["pack_vip_a_ete_choisit"]
menu_a_la_carte = config_data["menu_a_la_carte"]
prenom_et_nom = config_data["prenom_et_nom"]
adresse_mail = config_data["adresse_mail"]
matricule_de_la_voiture = config_data["matricule_de_la_voiture"]
Type_de_vehicule = config_data["Type_de_vehicule"]
marque_de_voiture = config_data["marque_de_voiture"]
Type_energie = config_data["Type_energie"]
puissance_du_vehicule = config_data["puissance_du_vehicule"]
menu_de_paiement = config_data["menu_de_paiement"]
menu_de_choix_de_paiement = config_data["menu_de_choix_de_paiement"]
paiement_en_espece = config_data["paiement_en_espece"]
Paiment_wave = config_data["Paiment_wave"]
Paiment_orange_money = config_data["Paiment_orange_money"]
Paiment_free_money = config_data["Paiment_free_money"]


def reply(message):
    data = message["data"]
    text = data["text"].encode('latin-1').decode('utf-8')
    number = data["from"]
    user = clients.find_one({"numero": number})

    if bool(user) == False:
        client.sendText(number, welcome_message)
        clients.insert_one({"numero": number, "status": "main", "messages": []})

    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, return_to_welcome_message)
            return str(text)

        if option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "Decouvrez les packs"}})
            client.sendText(number, menu_des_packs)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Renouveler votre assurance"}})
            client.sendText(number, Renouveler_votre_assurance)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "Trouver une agence"}})
            client.sendText(number, Trouver_une_agence)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, return_to_welcome_message)

    ############## Les packs  #################################################################################################################
    elif user["status"] == "Decouvrez les packs":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_des_packs)
            return str(text)
        if option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "pack ganale"}})
            client.sendText(number, menu_du_pack_ganale)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "pack sope"}})
            client.sendText(number, menu_du_pack_sope)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "pack vip"}})
            client.sendText(number, menu_du_pack_vip)
        elif option == 4:
            clients.update_one({"numero": number}, {"$set": {"status": "pack a la carte"}})
            client.sendText(number, menu_a_la_carte)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_des_packs)

    ############## PACK GANALE  #################################################################################################################
    ############## PACK GANALE  #################################################################################################################
    ############## PACK GANALE  #################################################################################################################

    elif user["status"] == "pack ganale":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_du_pack_ganale)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Decouvrez les packs"}})
            client.sendText(number, retour_au_menu_des_packs)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "remplissage de informations pack ganale"}})
            clients.update_one({"numero": number}, {"$set": {"produit": "PACK GANALE"}})
            client.sendText(number, pack_ganale_ete_choisi)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_du_pack_ganale)

    elif user["status"] == "remplissage de informations pack ganale":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, pack_ganale_ete_choisi)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "pack ganale"}})
            client.sendText(number, retour_au_menu_du_pack_ganale)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "prenom et nom"}})
            client.sendText(number, prenom_et_nom)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, pack_ganale_ete_choisi)

    elif user["status"] == "prenom et nom":
        client.sendText(number, adresse_mail)
        clients.update_one({"numero": number}, {"$set": {"status": "adresse mail"}})

    elif user["status"] == "adresse mail":
        clients.update_one({"numero": number}, {"$set": {"status": "matricule_de_la_voiture"}})
        client.sendText(number, matricule_de_la_voiture)

    elif user["status"] == "matricule_de_la_voiture":
        clients.update_one({"numero": number}, {"$set": {"status": "Type de vehicule"}})
        client.sendText(number, Type_de_vehicule)

    elif user["status"] == "Type de vehicule":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_de_vehicule)
            return str(text)
        if option == 5:
            client.sendText(number, retour_au_menu_du_pack_ganale)
            clients.update_one({"numero": number}, {"$set": {"status": "remplissage de informations pack ganale"}})
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Voiture touristique"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Voiture particuliere"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Camionnette"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_de_vehicule)

    elif user["status"] == "marque_de_voiture":
        clients.update_one({"numero": number}, {"$set": {"status": "Type energie"}})
        client.sendText(number, Type_energie)

    elif user["status"] == "Type energie":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_energie)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "Type de vehicule"}})
            client.sendText(number, Type_de_vehicule)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"Type_energie": "diesel"}})
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"Type_energie": "super"}})
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_energie)

    elif user["status"] == "puissance du vehicule":
        clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
        client.sendText(number, menu_de_paiement)

    elif user["status"] == "menu de paiement":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_paiement)
            return str(text)
        if option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "paiement en espece"}})
            client.sendText(number, paiement_en_espece)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_paiement)

    elif user["status"] == "menu de choix de paiement":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_choix_de_paiement)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
            client.sendText(number, menu_de_paiement)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment wave"}})
            client.sendText(number, Paiment_wave)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment orange money"}})
            client.sendText(number, Paiment_orange_money)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment free money"}})
            client.sendText(number, Paiment_free_money)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_choix_de_paiement)

    elif user["status"] == "paiement en espece":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, paiement_en_espece)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
            client.sendText(number, menu_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, paiement_en_espece)

    elif user["status"] == "Paiment wave":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_wave)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_wave)

    elif user["status"] == "Paiment orange money":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_orange_money)

    elif user["status"] == "Paiment free money":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_free_money)



    ############## PACK SOPE  #################################################################################################################
    ############## PACK SOPE  #################################################################################################################
    ############## PACK SOPE  #################################################################################################################

    elif user["status"] == "pack sope":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_du_pack_sope)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Decouvrez les packs"}})
            client.sendText(number, retour_au_menu_des_packs)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "remplissage de informations pack sope"}})
            clients.update_one({"numero": number}, {"$set": {"produit": "PACK SOPE"}})
            client.sendText(number, pack_sope_a_ete_choisit)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_du_pack_sope)

    elif user["status"] == "remplissage de informations pack sope":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, pack_sope_a_ete_choisit)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "pack sope"}})
            client.sendText(number, retour_au_menu_du_pack_sope)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "prenom et nom"}})
            client.sendText(number, prenom_et_nom)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, pack_sope_a_ete_choisit)

    elif user["status"] == "prenom et nom":
        client.sendText(number, adresse_mail)
        clients.update_one({"numero": number}, {"$set": {"status": "adresse mail"}})

    elif user["status"] == "adresse mail":
        clients.update_one({"numero": number}, {"$set": {"status": "matricule_de_la_voiture"}})
        client.sendText(number, matricule_de_la_voiture)

    elif user["status"] == "matricule_de_la_voiture":
        clients.update_one({"numero": number}, {"$set": {"status": "Type de vehicule"}})
        client.sendText(number, Type_de_vehicule)

    elif user["status"] == "Type de vehicule":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_de_vehicule)
            return str(text)
        if option == 5:
            client.sendText(number, retour_au_menu_du_pack_sope)
            clients.update_one({"numero": number}, {"$set": {"status": "remplissage de informations pack sope"}})
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Voiture touristique"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Voiture particuliere"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Camionnette"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_de_vehicule)

    elif user["status"] == "marque_de_voiture":
        clients.update_one({"numero": number}, {"$set": {"status": "Type energie"}})
        client.sendText(number, Type_energie)

    elif user["status"] == "Type energie":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_energie)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "Type de vehicule"}})
            client.sendText(number, Type_de_vehicule)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"Type_energie": "diesel"}})
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"Type_energie": "super"}})
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_energie)

    elif user["status"] == "puissance du vehicule":
        clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
        client.sendText(number, menu_de_paiement)

    elif user["status"] == "menu de paiement":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_paiement)
            return str(text)
        if option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "paiement en espece"}})
            client.sendText(number, paiement_en_espece)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_paiement)

    elif user["status"] == "menu de choix de paiement":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_choix_de_paiement)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
            client.sendText(number, menu_de_paiement)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment wave"}})
            client.sendText(number, Paiment_wave)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment orange money"}})
            client.sendText(number, Paiment_orange_money)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment free money"}})
            client.sendText(number, Paiment_free_money)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_choix_de_paiement)

    elif user["status"] == "paiement en espece":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, paiement_en_espece)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
            client.sendText(number, menu_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, paiement_en_espece)

    elif user["status"] == "Paiment wave":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_wave)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_wave)

    elif user["status"] == "Paiment orange money":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_orange_money)

    elif user["status"] == "Paiment free money":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_free_money)

    ############## PACK VIP  #################################################################################################################
    ############## PACK VIP  #################################################################################################################
    ############## PACK VIP  #################################################################################################################

    elif user["status"] == "pack vip":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_du_pack_vip)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Decouvrez les packs"}})
            client.sendText(number, retour_au_menu_des_packs)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "remplissage de informations pack vip"}})
            clients.update_one({"numero": number}, {"$set": {"produit": "PACK VIP"}})
            client.sendText(number, pack_vip_a_ete_choisit)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, retour_au_menu_du_pack_vip)

    elif user["status"] == "remplissage de informations pack vip":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, pack_vip_a_ete_choisit)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "pack vip"}})
            client.sendText(number, retour_au_menu_du_pack_vip)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "prenom et nom"}})
            client.sendText(number, prenom_et_nom)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, pack_vip_a_ete_choisit)

    elif user["status"] == "prenom et nom":
        client.sendText(number, adresse_mail)
        clients.update_one({"numero": number}, {"$set": {"status": "adresse mail"}})

    elif user["status"] == "adresse mail":
        clients.update_one({"numero": number}, {"$set": {"status": "matricule_de_la_voiture"}})
        client.sendText(number, matricule_de_la_voiture)

    elif user["status"] == "matricule_de_la_voiture":
        clients.update_one({"numero": number}, {"$set": {"status": "Type de vehicule"}})
        client.sendText(number, Type_de_vehicule)

    elif user["status"] == "Type de vehicule":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_de_vehicule)
            return str(text)
        if option == 5:
            client.sendText(number, retour_au_menu_du_pack_sope)
            clients.update_one({"numero": number}, {"$set": {"status": "remplissage de informations pack vip"}})
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Voiture touristique"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Voiture particuliere"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"Type de vehicule": "Camionnette"}})
            clients.update_one({"numero": number}, {"$set": {"status": "marque_de_voiture"}})
            client.sendText(number, marque_de_voiture)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_de_vehicule)

    elif user["status"] == "marque_de_voiture":
        clients.update_one({"numero": number}, {"$set": {"status": "Type energie"}})
        client.sendText(number, Type_energie)

    elif user["status"] == "Type energie":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_energie)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "Type de vehicule"}})
            client.sendText(number, Type_de_vehicule)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"Type_energie": "diesel"}})
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"Type_energie": "super"}})
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Type_energie)

    elif user["status"] == "puissance du vehicule":
        clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
        client.sendText(number, menu_de_paiement)

    elif user["status"] == "menu de paiement":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_paiement)
            return str(text)
        if option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        elif option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "puissance du vehicule"}})
            client.sendText(number, puissance_du_vehicule)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "paiement en espece"}})
            client.sendText(number, paiement_en_espece)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_paiement)

    elif user["status"] == "menu de choix de paiement":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_choix_de_paiement)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
            client.sendText(number, menu_de_paiement)
        elif option == 1:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment wave"}})
            client.sendText(number, Paiment_wave)
        elif option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment orange money"}})
            client.sendText(number, Paiment_orange_money)
        elif option == 3:
            clients.update_one({"numero": number}, {"$set": {"status": "Paiment free money"}})
            client.sendText(number, Paiment_free_money)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_de_choix_de_paiement)

    elif user["status"] == "paiement en espece":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, paiement_en_espece)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de paiement"}})
            client.sendText(number, menu_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, paiement_en_espece)

    elif user["status"] == "Paiment wave":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_wave)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_wave)

    elif user["status"] == "Paiment orange money":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_orange_money)

    elif user["status"] == "Paiment free money":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            return str(text)
        if option == 5:
            clients.update_one({"numero": number}, {"$set": {"status": "menu de choix de paiement"}})
            client.sendText(number, menu_de_choix_de_paiement)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Paiment_free_money)


    elif user["status"] == "pack a la carte":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_a_la_carte)
            return str(text)
        if option == 2:
            clients.update_one({"numero": number}, {"$set": {"status": "Decouvrez les packs"}})
            client.sendText(number, menu_des_packs)
        elif option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, menu_a_la_carte)




    ############## Renouveler_votre_assurance  #################################################################################################################
    ############## Renouveler_votre_assurance  #################################################################################################################
    ############## Renouveler_votre_assurance  #################################################################################################################
    ############## Renouveler_votre_assurance  #################################################################################################################

    elif user["status"] == "Renouveler votre assurance":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Renouveler_votre_assurance)
            return str(text)
        if option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Renouveler_votre_assurance)


    ############## Trouver_une_agence  #################################################################################################################
    ############## Trouver_une_agence  #################################################################################################################
    ############## Trouver_une_agence  #################################################################################################################
    ############## Trouver_une_agence  #################################################################################################################

    elif user["status"] == "Trouver une agence":
        try:
            option = int(text)
        except:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Trouver_une_agence)
            return str(text)
        if option == 0:
            clients.update_one({"numero": number}, {"$set": {"status": "main"}})
            client.sendText(number, return_to_welcome_message)
        else:
            client.sendText(number, invalid_option_message)
            client.sendText(number, Trouver_une_agence)



    clients.update_one({"numero": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})
    print("Connection Reussie !")


client.onMessage(reply)
