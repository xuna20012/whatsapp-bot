from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://xuna20012:7815@cluster0.r0hwd.mongodb.net/?retryWrites=true&w=majority")
db = cluster["xunabot"]
users = db["users"]
orders = db["orders"]

app = Flask(__name__)
@app.route("/", methods=["get", "post"])

def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    res = MessagingResponse()
    user = users.find_one({"number": number})

    if bool(user) == False:
        res.message("Hi, thank for contacting *Xuna Cakes*.\nYou can choose from one of the options below: "
                    "\n\n*Type*\n\n 1️⃣ To *contact* us \n 2️⃣ To *order* snacks \n 3️⃣ To know our *working hours* \n 4️⃣ "
                    "To get our *address*")
        users.insert_one({"number": number, "status": "main", "messages": []})
    elif user["status"] == "main":
        try:
            option = int(text)
        except:
            res.message("Svp veuiller entrer une reponse valide")
            return str(res)

        if option == 1:
            res.message("Nunemro Telephone: 781745898 \nE-mail* : cheikhounafall20012@gmail.com")

        elif option == 2:
            res.message("You have entered *ordering mode*.")
            users.update_one({"number": number}, {"$set": {"status": "ordering"}})
            res.message("You can select one of the following cakes to order: \n\n1️⃣ Red Velvet  \n2️⃣ Dark Forest \n3️⃣ Ice Cream Cake"
                "\n4️⃣ Plum Cake \n5️⃣ Sponge Cake \n6️⃣ Genoise Cake \n7️⃣ Angel Cake \n8️⃣ Carrot Cake \n9️⃣ Fruit Cake  \n0️⃣ Go Back")

        elif option == 3:
            res.message("Nous travaillons tous les jours de *8h a 00h* ")

        elif option == 4:
            res.message("Nous sommes au Scat Urbam a cote du Prestige Deco Villa 45")

        else:
            res.message("Svp veuiller entrer une reponse valide")
            return str(res)

    elif user["status"] == "ordering":
        try:
            option = int(text)
        except:
            res.message("Svp veuiller entrer une reponse valide")
            return str(res)

        if option == 0:
            users.update_one({"number": number}, {"$set": {"status": "main"}})
            res.message("You can choose from one of the options below: "
                        "\n\n*Type*\n\n 1️⃣ To *contact* us \n 2️⃣ To *order* snacks \n 3️⃣ To know our *working hours* \n 4️⃣ "
                        "To get our *address*")

        elif 1 <= text <= 9:
            cakes = ["Red Velvet", "Dark Forest", "Ice Cream Cake", "Plum Cake", "Sponge Cake", "Genoise Cake", "Angel Cake", "Carrot Cake"]
            selected = cakes[option -1]
            users.update_one({"number": number}, {"$set": {"status": "address"}})
            users.update_one({"number": number}, {"$set": {"item": selected}})
            res.message("Excellente choice 😉")
            res.message("Please enter your address to confirm this order")
        else:
            res.message("Svp veuiller entrer une reponse valide")

    elif user["status"] == "address":
        selected = user["item"]
        res.message("Thanks for shopping with us !")
        res.message(f"Your order for {selected} hase been recieved and will be delivered within an houre")
        orders.insert_one({"number": number, "item": selected, "address": text, "order_time": datetime.now()})
        users.update_one({"number": number}, {"$set": {"status": "ordered"}})
    elif user["status"] == "ordered":
        res.message("Hi, thank for contacting again.\nYou can choose from one of the options below: "
                    "\n\n*Type*\n\n 1️⃣ To *contact* us \n 2️⃣ To *order* snacks \n 3️⃣ To know our *working hours* \n 4️⃣ "
                    "To get our *address*")
        users.update_one({"number": number}, {"$set": {"status": "main"}})


    users.update_one({"number": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})
    return str(res)

if __name__ == "__main__":
    app.run()
