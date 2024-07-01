
import websocket
import json
import threading
import time

# Make it easier and less boilerplate (don't import these functions)
def send_json_request(ws,request):
    ws.send(json.dumps(request))

def recive_json_response(ws):
    response = ws.recv()

    if response:
        return json.loads(response)

def HeartbeatStart(ws,interval):
        while True:
            time.sleep(interval)

            heartbeat_object = {
                "op":1,
                "d":"null"
            }
            send_json_request(ws,heartbeat_object)

################################

class GatewayWebsocket:
    def __init__(self,WebSocket,Token) -> None:
        self.WebSocket = WebSocket
        self.Token = Token

    def CreateGatewayObj(Token):
        return GatewayWebsocket(None,Token)
    
    def CreateConnection(self):
        ws = websocket.WebSocket()
        ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
        event = recive_json_response(ws)

        heartbeat_interval = event["d"]["heartbeat_interval"] / 10000

        x = threading.Thread(target=HeartbeatStart,args=(ws,heartbeat_interval))
        x.start()

        self.WebSocket = ws
        return ws
    
    def SendIntents(self,Intents:int):
        payload = {
            "op": 2,
            "d": {
                "token": self.Token,
                "intents": Intents,
                "properties": {
                "os": "linux",
                "browser": "AntiCord",
                "device": "glory_to_antifurry"
                }
            }
        }
        
        send_json_request(self.WebSocket,payload)
        if recive_json_response(ws=self.WebSocket)["op"] == 0:
            return 0
        else:
            return 1
        
    def ReciveEvent(self):
        event = recive_json_response(ws=self.WebSocket)
        if event["op"] == 11:
            pass
        else:
            return event