# PROJET_INFO834

pip install Django
pip install django-compressor
pip install djongo

npm install -D tailwindcss
npm install flowbite

pip install channels
pip install -U channels["daphne"]
pip install channels_redis
pip install pymongo==3.12.3
pip install pytz
pip install uuid




(pip install -r requirements.txt) ne sers pas 

## Pour lancer le serveur:

Dans le dossier Bdd_dir
```bash
./MongoForWin
docker run -p 6379:6379 -d redis:5
```

Dans le dossier mysite (pensez à utiliser l'environement python ou vous avez installé les dépendances)
```bash
py manage.py runserver
```


Pour lancer le replicate il faut de lancer le MongoReplicate.
MongReplicate.bat dans le dossier Bdd_dir pour linux
MongoForWin pour windows

des problèmes peuvent se poser lors de l'exécution du script. l'un des problème peut provenir de la première ligne qui précise quelle shell exécuté à modifier si besoin.

Les serveurs sont lancé sur les port 27019 27020 27021, l'arbitre sur le port 30000 
