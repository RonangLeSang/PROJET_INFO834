from pymongo import MongoClient
from pymongo.errors import OperationFailure

replica_set_name = 'myReplicaSet'
hosts = ['localhost:27018', 'localhost:27019', 'localhost:27020', 'localhost:27021', ]

client = MongoClient(hosts[0])

config = {
'_id': replica_set_name,
'members': [
{'_id': 0, 'host': hosts[0]},
{'_id': 1, 'host': hosts[1]},
{'_id': 2, 'host': hosts[2]}
]
}
