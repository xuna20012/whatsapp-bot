from wa_automate_socket_client import SocketClient
from wati_api import client
from time import sleep

client = SocketClient('http://localhost:5000/')

def reply(message):
    data = message["data"]
    text = data["text"]
    number = data["from"]
    id = data["id"]

    if "Hello" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")


    if "Salut" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")

    if "Bonsoir" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")
    if "bonsoir" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")
    if "Hi" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")

    if "Bonjour" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")
    if "bonjour" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")
    if "Bnjr" in text:
        client.sendText(number, "Bienvenu sur le REBOT de *CheiXuna*.\nveuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")
        client.sendImage(number, "")
    if "Merci" in text:
        client.sendText(number, "Merciiii A bientot")
    if "Ok" in text:
        client.sendText(number, "Merciiii A bientot")
    if "ok" in text:
        client.sendText(number, "Merciiii A bientot")
    if "merci" in text:
        client.sendText(number, "Merciiii A bientot")
    if "Excellent" in text:
        client.sendText(number, "Merciiii A bientot")
    if text == "1":
        client.sendText(number,
                        "Merci de suivre votre commande: \n\n *5:* Commander une *Pizza*\n *6:* Commander un *Burger*\n "
                        "*7:* Commander un *Tacos*\n *0:* Retourner au Menu Principal")
    if "0" in text:
        client.sendText(number, "veuiller choisir parmis les options suivantes: "
                                "\n\n*Tapez*\n\n *1:* Pour *commander* \n *2:* Pour Connaitre nos *heures de travails* \n *3:* Pour nous *contacter* "
                                "\n *4:* Pour connaitre notre *adresse*")

    elif text == "2":
        client.sendText(number,
                        "Lundi : De 8h:00 a 00H00\nMardi : De 8h:00 a 00H00\nMercredi : De 8h:00 a 00H00\nJeudi : De 8h:00 a 00H00\n"
                        "Vendredi : De 8h:00 a 00H00\nSamedi : De 9h:00 a 00H00\nDimanche : De 9h:00 a 23H00\n\n\n"
                        "*0:* Retourner au Menu Principal")
    elif text == "3":
        client.sendText(number,
                        "*Nos contacts:*\nTelephone : 781745898\nMail : cheikhounafall20012@gmail.com\nInstagram : @xuna_fall\n\n\n"
                        "*0:* Retourner au Menu Principal")
    elif text == "4":
        client.sendText(number, "Nous sommes aux HLM Grand Yoff\n\n\n*0:* Retourner au Menu Principal")
    elif text == "5":
        client.sendText(number, "*Woplow !! Nos Pizza sont les meilleurs !!*\n\n")
        client.sendImage(number, "images/Pizza.jpg", "image", "*Menu*\n\n *0:* Retourner au Menu Principal")
    elif text == "6":
        client.sendText(number, "*Woplow !! Nos Burger sont les meilleurs !!*\n\n")
        client.sendImage(number, "images/Burger.jpeg", "image", "*Menu*\n\n *0:* Retourner au Menu Principal")
    elif text == "7":
        client.sendText(number, "*Woplow !! Nos Tacos sont les meilleurs !!*\n\n")
        client.sendImage(number, "img/biff.jpg", "image", "*Menu*\n\n *0:* Retourner au Menu Principal")


client.onMessage(reply)
