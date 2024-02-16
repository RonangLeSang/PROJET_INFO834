#!/bin/bash
mongod --replSet rs0 --port 27018 --dbpath mongdata/R0S1 &
mongod --replSet rs0 --port 27019 --dbpath mongdata/R0S2 &
mongod --replSet rs0 --port 27020 --dbpath mongdata/R0S3 &
mongod --replSet rs0 --port 27021 --dbpath mongdata/R0S4 &
