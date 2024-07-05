import anticord
import anticord.AntiCordPlainHttpRequest as AntiCordHttp
import anticord.AntiCordGateway as AntiCordGateway

BOT = AntiCordHttp.BOT("") # Token here
Gateway = AntiCordGateway.GatewayWebsocket.CreateGatewayObj(BOT.TOKEN)

Gateway.CreateConnection()
Gateway.SendIntents(513)

while True:
    Event = Gateway.ReciveEvent()

    if Event == None:
        pass
    else:
        if Event["t"] == "MESSAGE_CREATE":
            if Event["d"]["content"] == "!ping":
                channel = BOT.GetChannelByID(Event["d"]["channel_id"])

                channel.SendMessage("pong")