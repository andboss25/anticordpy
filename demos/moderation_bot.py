
import anticord
import anticord.AntiCordPlainHttpRequest as AntiCordHttp
import anticord.AntiCordGateway as AntiCordGateway
import threading

BOT = AntiCordHttp.BOT("")
Gateway = AntiCordGateway.GatewayWebsocket.CreateGatewayObj(BOT.TOKEN)

mod_role_id = 1 # The id of the ppl who can use the commands

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

def kick(Event,guild):
            # One word reason cuz ye
            text = Event["d"]["content"]
            channel = BOT.GetChannelByID(Event["d"]["channel_id"])
            guild = BOT.GetGuildByID(Event["d"]["guild_id"])

            text = text.split()
            try:
                    kick_user = GetMemberAsInObjectByName(guild,text[1])
            except:
                    channel.SendMessage("No user provided")
                    return 0

            if kick_user == None:
                    channel.SendMessage("User does not exist")
                    return 0
            
            try:
                    reason = text[2]
            except:
                    reason = "No reason provided"

            kick_user.CreateUserDm().SendMessage("You were kicked in " + guild.GetGuildAttribute("name") + " for reason: ``" + reason + "``")
            try:
                guild.KickUser(kick_user)
                channel.SendMessage("Kicked user! (unless they are a higher role than the bot)")
            except:
                channel.SendMessage("Failed to kick")

def ban(Event,guild):
            # One word reason cuz ye
            text = Event["d"]["content"]
            channel = BOT.GetChannelByID(Event["d"]["channel_id"])
            guild = BOT.GetGuildByID(Event["d"]["guild_id"])
            
            text = text.split()
            try:
                    kick_user = GetMemberAsInObjectByName(guild,text[1])
            except:
                    channel.SendMessage("No user provided")
                    return 0

            if kick_user == None:
                    channel.SendMessage("User does not exist")
                    return 0
            
            try:
                    reason = text[2]
            except:
                    reason = "No reason provided"

            kick_user.CreateUserDm().SendMessage("You were banned in " + guild.GetGuildAttribute("name") + " for reason: ``" + reason + "``")
            try:
                guild.BanUser(kick_user)
                channel.SendMessage("Banned user! (unless they are a higher role than the bot)")
            except:
                channel.SendMessage("Failed to ban")

while True:
    Event = Gateway.ReciveEvent()

    if Event == None:
        pass
    else:
        if Event["t"] == "MESSAGE_CREATE":
            user = BOT.GetUserByID(Event["d"]["author"]["id"])
            guild = BOT.GetGuildByID(Event["d"]["guild_id"])
            if DoesGuildMemberHaveRole(guild,mod_role_id,user):
                if Event["d"]["content"].split()[0] == "!kick":
                    print("Kick command ran!")
                    threading.Thread(target=kick,args=(Event,guild)).start()
                if Event["d"]["content"].split()[0] == "!ban":
                    print("Ban command ran!")
                    threading.Thread(target=ban,args=(Event,guild)).start()
                


                



