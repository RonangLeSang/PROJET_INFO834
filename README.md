# PROJET_INFO834

pip install Django
pip install django-compressor

npm install -D tailwindcss
npm install flowbite

pip install channels
pip install -U channels["daphne"]
python3 -m pip install channels_redis




(pip install -r requirements.txt) ne sers pas 

Pour lancer le serveur:
docker run -p 6379:6379 -d redis:5
py manage.py runserver

Pour lancer le replicate il faut de lancer le MongoReplicate.
des problèmes peuvent se poser lors de l'exécution du script. l'un des problème peut provenir de la première ligne qui précise quelle shell exécuté à modifier si besoin.

Les serveurs sont lancé sur les port 27019 27020 27021, l'arbitre sur le port 30000 
