import socket
import pickle
import logging


logger = logging.getLogger()
s_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
s_handler.setFormatter(formatter)
logger.addHandler(s_handler)
logger.setLevel(logging.DEBUG)
socket = socket.socket()
socket.bind(('127.0.0.1', 9091))
socket.listen(10)
conn, addr = socket.accept()

print("Connected:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    L = pickle.loads(data)
    logger.debug('Receiving data from client')
    # print(L)
    conn.send(pickle.dumps(L))
    logger.debug('Sending data to client')

conn.close()
