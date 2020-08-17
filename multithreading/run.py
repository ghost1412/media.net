import redis
import threading
import requests

endpoint = "http://127.0.0.1:8000"

redis = redis.Redis(host="localhost", port = 6900)

def response_ser(server, data):
    resp = requests.get(server, data)
    print(f'{resp} is the server response for {data} being pushed')

while True:
    try:
        data = redis.zrange('queue',-1,-1)
        if len(data):
            redis.zrem('queue',data[0])
            t = threading.Thread(target = response_ser, args = [endpoint, data[0]])
            t.start()
    except:
        print('ERROR!')
        pass
~                                                                                                        
~                                                                                                        
~                
