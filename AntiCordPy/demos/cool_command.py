import anticord
import anticord.AntiCordPlainHttpRequest as AntiCordHttp
import anticord.AntiCordGateway as AntiCordGateway

BOT = AntiCordHttp.BOT("") # Token here
Gateway = AntiCordGateway.GatewayWebsocket.CreateGatewayObj(BOT.TOKEN)
cool_role_id = 1249356732120039465 # Cool role id here

Gateway.CreateConnection()
Gateway.SendIntents(513)

while True:
    Event = Gateway.ReciveEvent()

    if Event == None:
        pass
    else:
        
        if Event["t"] == "MESSAGE_CREATE":
            text = Event["d"]["content"]
            channel = BOT.GetChannelByID(Event["d"]["channel_id"])

            text = text.split()

            if text[0] == "!cool":
                guild = BOT.GetGuildByID(Event["d"]["guild_id"])
                channel.SendMessage("Thinking...")

                User = guild.GetMemberAsInObjectByName(text[1])
                
                channel.SendMessage("Computing coolness factors...")

                
                if guild.DoesGuildMemberHaveRole(cool_role_id,User) == True:
                    channel.SendMessage("Yes , " +  User.GetUserName() + " is cool")
                else:
                    channel.SendMessage("No he is not")

