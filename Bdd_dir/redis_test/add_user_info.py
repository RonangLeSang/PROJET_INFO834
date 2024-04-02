from datetime import datetime
import redis
r = redis.Redis()
r.ping()
def requ(utilisateur):
        a = r.lrange(f"utilisateur:{utilisateur} 0 -1")
        r.lpush(f"utilisateur:{utilisateur} {datetime.now()}")

requ("test_moi")

