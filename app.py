import redis


def read():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set("hello", "world")
    print("hello %s!" % r.get("hello").decode())


if __name__ == '__main__':
   read() 
