from pymongo import MongoClient 

client = MongoClient("localhost", 27019)

 db= client.myChat

user_collection = db["user"]
conv_collection = db["conv"]

def create_conv(UserList): # on crée une fonction pour crée  une conversation entre les utilisateur
	string_id = ""# chaîne de caractère dans laquelle on stocke tous les id des utilisateur
	for user in UserList:
		string_id += str(user)
	conv = {'id_user' : UserList, 'id_conv' : string_id}
	conv_collection.insert_one(conv)
	for user in UserList : 
		user_collection.update_one({"_id" : user}, {$push : {"conversation" : string_id }}) # Pour chaque utilisateur on ajoute dans la base de donnée la conversation

def user_in_conv(user, conv):
	User = user_conv.find({_id : user})
	User = list(User)
	user_res = User[0]
	conversation = user_res["conversation"]
	if conv in conversation:
		return True
	return False

def conv_user_in(UserList): # on crée une fonction qui va récupérer tous les id des conversation dans laquelles les utlisateurs donné se trouvent
	List_conv =[] # liste dans laquelle on stocke les conversation en commun entre les utilisateur
	for user in UserList:
		
	
	
