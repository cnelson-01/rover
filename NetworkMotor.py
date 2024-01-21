import json
import socket
import threading

import Stepper


class NetworkMotor:
    def __init__(self, port, motor: Stepper, ip=''):
        pass
        self.keepRunning = True
        self.ip = ip
        self.port = port
        self.motor = motor

        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def shutdown(self):
        self.keepRunning = False

    def run(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to a public host, and a well-known port
        serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversocket.bind((self.ip, self.port))
        # become a server socket
        serversocket.listen(5)
        print('waiting for connections')
        while self.keepRunning:
            # serversocket.settimeout(0)
            # accept connections from outside
            (clientsocket, address) = serversocket.accept()
            clientsocket.setblocking(True)
            print("connected: " + str(self.port))
            self.connected = True
            clientsocket.settimeout(1.0)
            data = clientsocket.recv(4000)
            if data:
                cmds = json.loads(data.decode('utf-8'))
                print(cmds)
                if cmds['forward']:
                    self.motor.moveForward(cmds['amount'])
                else:
                    self.motor.moveBackward(cmds['amount'])
