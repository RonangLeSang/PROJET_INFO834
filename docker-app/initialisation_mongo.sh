docker-compose up -d 
sleep 10
docker-compose exec mongo1 mongosh --port 27019 --quiet --eval 'rs.initiate()' --json relaxed
docker-compose exec mongo1 mongosh --port 27019 --quiet --eval "rs.add('local:27020')" --json relaxed
docker-compose exec mongo1 mongosh --port 27019 --quiet --eval "rs.add('local:27021')" --json relaxed
docker-compose exex mongo1 mongosh --port 27019 --quiet --eval "rs.addArb('local:3000')" --json relaxed
docker-compose exec monapp /bin/sh -c "source venv/bin/activate && python mysite/manage.py migrate && python mysite/manage.py runserver 0.0.0.0:8000"
