import logging
import random
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

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = service_pb2_grpc.ServerStub(channel)
        service_add(stub, 1, 2)
        service_dot(stub)

if __name__ == '__main__':
    logging.basicConfig()
    run()