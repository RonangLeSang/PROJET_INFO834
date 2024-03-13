import djongo
from mongoModel import *
from djongo import models


def add_conv(UserList):
    string_id = ""
    for user in UserList:
        string_id += str(user)
    conv = ModelConversation.objects.create({'users' : UserList, 'id_conv' : string_id})
    conv.save()
    for user in UserList:
        ModelUser.objects.filter(_id = user).update(conversation__push = string_id)
        ModelUser.save()

def user_in_conv(id_user, id_conv):
    user = ModelUser.filter(_id=id_user, conversation__contains = id_conv)
    return user


def get_message(id_conv): # fonction retourne les message d'une conversation
    conv = ModelDiscussion.objects.filter(id_conv = id_conv)
    message = list(conv.message)
    

def add_message(id_conv, message): # fonction qui ajoute les message à une conversation
    pass