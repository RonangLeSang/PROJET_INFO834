#!/bin/bash

(
mongod --replSet rs0 --port 27018 --dbpath mongdata/R0S1 &
mongod --replSet rs0 --port 27019 --dbpath mongdata/R0S2 &
mongod --replSet rs0 --port 27020 --dbpath mongdata/R0S3 &
mongod --replSet rs0 --port 27021 --dbpath mongdata/R0S4 &
)

mongod --port 30000 --dbpath mongdata/arb --replSet rs0

mongosh --port 27018 --eval "rs.initiate({_id: 'rs0',members: [{_id: 0,host:'localhost:27018'},{_id: 1,host: 'localhost:27019'},{_id: 2,host: 'localhost:27020'},{_id: 3,host: 'localhost:27021'},{_id: 4,host: 'localhost:30000',arbiterOnly: true}]});"

