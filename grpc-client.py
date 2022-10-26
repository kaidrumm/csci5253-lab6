import logging
import random
import base64
from turtle import dot

import grpc
import service_pb2
import service_pb2_grpc

def service_add(stub, a, b):
    sum = stub.add(service_pb2.addMsg(a=a, b=b))
    print(f"Found {sum}")
    return sum

def service_dot(stub):
    v1 = []
    v2 = []
    for n in range(100):
        v1.append(random.random())
        v2.append(random.random())

    dot = stub.dotproduct(service_pb2.dotProductMsg(a=v1, b=v2))
    print(f"Found {dot}")

def service_jsonimage(stub):
    img = open('Flatirons_Winter_sunrise_edit_2.jpg', 'rb').read()
    img_encoded = base64.b64encode(img)
    request = service_pb2.jsonImageMsg(img=img_encoded)
    size = stub.jsonimage(request)
    print(f"Found {size}")

def service_rawimage(stub):
    img = open('Flatirons_Winter_sunrise_edit_2.jpg', 'rb').read()
    request = service_pb2.rawImageMsg(img=img)
    size = stub.rawimage(request)
    print(f"Found {size}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ServerStub(channel)
        service_add(stub, 1, 2)
        service_dot(stub)
        service_jsonimage(stub)
        service_rawimage(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()