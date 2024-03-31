from hashlib import sha256

from pymongo import MongoClient
from datetime import datetime

client = MongoClient("localhost", 27019)

db = client.MyChat

# on définit les collections conversations qui catégorise l'entiéreté de toutes les conversation
# on définit également la collections qui stocke les données des utilisateurs.
user_collection = db["user"]
conv_collection = db["conversations"]


def create_conv(UserList):  # on crée une fonction pour crée  une conversation entre les utilisateur
    string_id = ""  # chaîne de caractère dans laquelle on stocke tous les id des utilisateur
    for user in UserList:
        string_id += str(user)
    conv = {'id_user': UserList, 'id_conv': string_id}
    conv_collection.insert_one(conv)
    for user in UserList:
        user_collection.update_one({"_id": user}, {"$push": {
            "conversation": string_id}})  # Pour chaque utilisateur on ajoute dans la base de donnée la conversation
    return string_id


def user_in_conv(user, conv):
    User = user_conv.find({_id: user})
    User = list(User)
    user_res = User[0]
    conversation = user_res["conversation"]
    if conv in conversation:
        return True
    return False


def conv_user_in(UserList):  # on crée une fonction qui va récupérer tous les id des conversation dans laquelles les
    # utlisateurs donné se trouvent
    List_conv = []  # liste dans laquelle on stocke les conversation en commun entre les utilisateur


def add_message(id_conv, message, id_user):
    discussion_collection = db[
        id_conv]  # on définit la collection de la conversation pour laquelle on souhaite ajouter un message
    message = {'id_user': id_user, 'message': message, 'date': datetime.now()}
    discussion_collection.insert_one(message)


def get_last_message(id_conv, nbr_message=50):
    discussion_collection = db[id_conv]
    Messages = list(discussion_collection.find().sort("date", -1).limit(nbr_message))
    return Messages
