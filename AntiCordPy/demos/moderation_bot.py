
import anticord
import anticord.AntiCordPlainHttpRequest as AntiCordHttp
import anticord.AntiCordGateway as AntiCordGateway
import threading

BOT = AntiCordHttp.BOT("")
Gateway = AntiCordGateway.GatewayWebsocket.CreateGatewayObj(BOT.TOKEN)

mod_role_id = 1249356732120039465 # The id of the ppl who can use the commands


Gateway.CreateConnection()
Gateway.SendIntents(513)

def kick(Event,guild):
            # One word reason cuz ye
            text = Event["d"]["content"]
            channel = BOT.GetChannelByID(Event["d"]["channel_id"])
            guild = BOT.GetGuildByID(Event["d"]["guild_id"])

            text = text.split()
            try:
                    kick_user = guild.GetMemberAsInObjectByName(text[1])
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

            kick_user.CreateUserDm().SendMessage("You were kicked in " + guild.GetGuildName() + " for reason: ``" + reason + "``")
            guild.KickUser(kick_user)
            channel.SendMessage("Kicked user! (unless they are a higher role than the bot)")

def ban(Event,guild):
            # One word reason cuz ye
            text = Event["d"]["content"]
            channel = BOT.GetChannelByID(Event["d"]["channel_id"])
            guild = BOT.GetGuildByID(Event["d"]["guild_id"])
            
            text = text.split()
            try:
                    kick_user = guild.GetMemberAsInObjectByName(text[1])
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

            kick_user.CreateUserDm().SendMessage("You were banned in " + guild.GetGuildName() + " for reason: ``" + reason + "``")
            guild.BanUser(kick_user)
            channel.SendMessage("Banned user! (unless they are a higher role than the bot)")

while True:
    Event = Gateway.ReciveEvent()

    if Event == None:
        pass
    else:
        if Event["t"] == "MESSAGE_CREATE":
            user = BOT.GetUserByID(Event["d"]["author"]["id"])
            guild = BOT.GetGuildByID(Event["d"]["guild_id"])
            if guild.DoesGuildMemberHaveRole(mod_role_id,user):
                if Event["d"]["content"].split()[0] == "!kick":
                    print("Kick command ran!")
                    threading.Thread(target=kick,args=(Event,guild)).start()
                if Event["d"]["content"].split()[0] == "!ban":
                    print("Ban command ran!")
                    threading.Thread(target=ban,args=(Event,guild)).start()
                


                



