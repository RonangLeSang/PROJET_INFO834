#!/bin/bash

script_directory="$(cd "$(dirname "$0")" && pwd)"

# Utilise le chemin absolu pour accéder au répertoire d'intérêt
mongod --replSet rs0 --port 27018 --dbpath $script_directory/mongdata/R0S1 &
mongod --replSet rs0 --port 27019 --dbpath $script_directory/mongdata/R0S2 &
mongod --replSet rs0 --port 27020 --dbpath $script_directory/mongdata/R0S3 &
mongod --replSet rs0 --port 27021 --dbpath $script_directory/mongdata/R0S4 &

mongod --port 30000 --dbpath $script_directory/mongdata/arb --replSet rs0
