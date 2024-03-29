import redis

# Connexion à Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Remplacer 'room_name' par le nom de votre salle
room_name = 'cc'
user_list = r.smembers(room_name)

list= [str(user_id, 'utf-8') for user_id in user_list]

# Afficher les utilisateurs dans la salle
print("Utilisateurs dans la salle : ", list)


