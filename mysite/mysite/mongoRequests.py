import djongo
from mongoModel import *

def addConv(UserList):
    string_id = ""
    for user in UserList:
        string_id += str(user)
    conv = ModelConversation.create({'users' : UserList, 'id_conv' : string_id})
    conv_collection.insert_one(conv)
    for user in UserList:
        user_collection.update_one({"_id": user}, {$push: {"conversation": string_id}})
