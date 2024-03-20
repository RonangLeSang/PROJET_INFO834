REM create C:\data\db0
IF NOT EXIST C:\data mkdir C:\data
IF NOT EXIST C:\data\R0S1 mkdir C:\data\R0S1
IF NOT EXIST C:\data\R0S2 mkdir C:\data\R0S2
IF NOT EXIST C:\data\R0S3 mkdir C:\data\R0S3
IF NOT EXIST C:\data\R0S4 mkdir C:\data\R0S4
IF NOT EXIST C:\data\arb mkdir C:\data\arb

REM start 5 mongod instances
powershell -Command "Start-Process -FilePath 'mongod' -ArgumentList '--replSet rs0 --port 27018 --dbpath C:\data\R0S1'"
powershell -Command "Start-Process -FilePath 'mongod' -ArgumentList '--replSet rs0 --port 27019 --dbpath C:\data\R0S2'"
powershell -Command "Start-Process -FilePath 'mongod' -ArgumentList '--replSet rs0 --port 27020 --dbpath C:\data\R0S3'"
powershell -Command "Start-Process -FilePath 'mongod' -ArgumentList '--replSet rs0 --port 27021 --dbpath C:\data\R0S4'"
timeout 10
powershell -Command "Start-Process -FilePath 'mongod' -ArgumentList '--port 30000 --dbpath C:\data\arb --replSet rs0'"

REM wait for the instances to start
timeout 15

REM open a mongo shell*
mongosh --port 27018 --eval "rs.initiate({_id: 'rs0',members: [{_id: 0,host: 'localhost:27018'},{_id: 1,host: 'localhost:27019'},{_id: 2,host: 'localhost:27020'},{_id: 3,host: 'localhost:27021'},{_id: 4,host: 'localhost:30000',arbiterOnly: true}]});"