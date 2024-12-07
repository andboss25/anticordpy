import anticord
import anticord.AntiCordPlainHttpRequest as AntiCordHttp
import anticord.AntiCordGateway as AntiCordGateway
import anticord.AntiCordPlainHttpRequest

BOT = AntiCordHttp.BOT("") # Token here
Gateway = AntiCordGateway.GatewayWebsocket.CreateGatewayObj(BOT.TOKEN)
cool_role_id = 1 # Cool role id here

def DoesGuildMemberHaveRole(guild,role_id:int,user):
            if guild.GetGuildMember(user.userid)["roles"] == []:
                return False
            else:
                for i in guild.GetGuildMember(user.userid)["roles"]:

                    i = int(i)
                    if role_id == i:
                        return True
                
                return False

def GetMemberAsInObjectByName(guild,name:str):
    for i in guild.GetGuildMembers(1000):
        if i.GetUserAttribute("username") == name:
            return i
                
    return None

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

                User = GetMemberAsInObjectByName(guild,text[1])
                
                channel.SendMessage("Computing coolness factors...")

                
                if DoesGuildMemberHaveRole(guild,cool_role_id,User) == True:
                    channel.SendMessage("Yes , " +  User.GetUserAttribute("username") + " is cool")
                else:
                    channel.SendMessage("No he is not")
