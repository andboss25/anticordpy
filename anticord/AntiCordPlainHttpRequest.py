


import requests
import json

BASEURL = "https://discord.com/api"

## Library functions

class AnticordUtil:
    
    def CheckErrResponsePlainHTTP(response:requests.Response,msg:str) -> dict:
        response_content = json.loads(response.content)
        if response.status_code == 200 or response.status_code == 204 or response.status_code == 201:
            return response_content
        else:
            try:
                raise Exception("Error " + msg + " , code: " + str(response_content["code"]) + " error message: " + response_content["message"])
            except KeyError:
                raise Exception("Error , error message: " + response_content["message"])
    
    def CheckErrResponseAttributeHTTP(response:requests.Response,msg:str,attribute:str):
        return_data_content = json.loads(response.content)

        if response.status_code != 200:
            try:
                raise Exception("Error getting " + msg + " attribute , code: " + str(return_data_content["code"]) + " error message: " + return_data_content["message"])
            except KeyError:
                raise Exception("Error , error message: " + return_data_content["message"])
        else:
            try:
                return_data_content_selected = return_data_content[attribute]
                return return_data_content_selected
            except KeyError:
                raise Exception("Invalid atribute: '" + attribute + "' ")
    
    def CheckErrResponsePlainHttpNoReturn(response:requests.Response,msg:str):
        if response.status_code != 204:
            return_data_content = json.loads(response.content)
            try:
                raise Exception("Error " + msg + " , code: " + str(return_data_content["code"]) + " error message: " + return_data_content["message"])
            except KeyError:
                raise Exception("Error , error message: " + return_data_content["message"])
            

### CHANNEL ###
class Channel:
    def __init__(self,channelid:int,BOTParentToken:str) -> None:
        self.channelid = channelid

        self.BOTParentToken = BOTParentToken
        self.header = {
            "Authorization" : BOTParentToken
        }

    def SendMessage(self,content:str):
        # Send a message
        URL = BASEURL + "/channels/" + str(self.channelid) + "/messages"

        data = {
            "content":content,
            "enforce_nonce":False
        }

        msg = requests.post(url=URL,data=data,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHTTP(msg,"sending message")
    
    def DeleteMessage(self,messageid:int):
        # Delete a message
        URL = BASEURL + "/channels/" + str(self.channelid) + "/messages/" + str(messageid)

        msg = requests.delete(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHttpNoReturn(msg,"deleting message")
            
    
    def DeleteGuildChannel(self):
        # Delete the channel
        URL = BASEURL + "/channels/" + str(self.channelid)

        chan = requests.delete(url=URL,headers=self.header)
        
        return AnticordUtil.CheckErrResponsePlainHTTP(chan,"deleting guild channel")

    def ChangeGuildChannelAttribute(self,chg_data:dict):
        # Change guild name
        URL = BASEURL + "/channels/" + str(self.channelid)

        chan = requests.patch(url=URL,headers=self.header,json=chg_data)
    
        return AnticordUtil.CheckErrResponsePlainHTTP(chan,"changing guild channel")
    
    def CreateInivte(self):
        # Create invite
        URL = BASEURL + "/channels/" + str(self.channelid) + "/invites"
        
        inv = requests.post(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHTTP(inv,"making invite")
    
    def GetChannelAttribute(self,attribute):
        # Make channel attribute
        URL = BASEURL + "/channels/" + str(self.channelid)
        
        return_data = requests.get(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponseAttributeHTTP(return_data,"channel",attribute)

### USER ###
class User:
    def __init__(self,userid:int,BOTParentToken:str) -> None:
        self.userid = userid
        self.BOTParentToken = BOTParentToken
        self.header = {
            "Authorization" : BOTParentToken
    }
        
    def CreateUserDm(self) -> Channel:
        # Make user dm
        URL = BASEURL + "/users/@me/channels"

        data = {
            "recipient_id":self.userid
        }
        
        response_data = requests.post(url=URL,headers=self.header,json=data)

        # TODO MAKE SPECIFIC FUNCTION THAT TURNS RESPONSE RETURN TO A CHANNEL (on next update or so)
        if response_data.status_code != 200:
            return_data = json.loads(response_data.content)
            try:
                raise Exception("Error making making user DM , code: " + str(return_data["code"]) + " error message: " + return_data["message"])
            except KeyError:
                raise Exception("Error , error message: " + return_data["message"])
        else:
            return_data = json.loads(response_data.content)
            return_data = return_data["id"]

            return Channel(return_data,self.BOTParentToken)
    
    def GetUserAttribute(self,attribute):
        # Get user attribute
        URL = BASEURL + "/users/" + str(self.userid)
        
        return_data = requests.get(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponseAttributeHTTP(return_data,"user",attribute)
    

    
### GUILD ###
class Guild:
    def __init__(self,guildid:int,BOTParentToken:str) -> None:
        self.guildid = guildid
        self.BOTParentToken = BOTParentToken
        self.header = {
            "Authorization" : BOTParentToken,
            'Content-Type': 'application/json'
    }
    
    def GetGuildAttribute(self,attribute):
        # Get guild attribute
        URL = BASEURL + "/guilds/" + str(self.guildid)

        return_data = requests.get(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponseAttributeHTTP(return_data,"guild",attribute)

    def CreateGuildChannelText(self,name:str,topic:str=""):
        # Create a guild text channel
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/channels"

        data = {
            "name":name,
            "topic":topic,
            "type":0
        }

        return_data = requests.post(url=URL,json=data,headers=self.header)

        return_data_content = json.loads(return_data.content)

        # TODO MAKE SPECIFIC FUNCTION THAT TURNS RESPONSE RETURN TO A CHANNEL (on next update or so)

        if return_data.status_code != 201:
            try:
                raise Exception("Error making text channel , code: " + str(return_data_content["code"]) + " error message: " + return_data_content["message"])
            except KeyError:
                try:
                    raise Exception("Error , error message: " + return_data_content["message"])
                except:
                    raise Exception("There is Errorfull content in your CreateGuildChannelText arguments")
        else:
            return Channel(return_data_content["id"],self.BOTParentToken)
        

    def ChangeGuildAttribute(self,chg_data:dict):
        # Change guild name
        URL = BASEURL + "/guilds/" + str(self.guildid)

        return_data = requests.patch(url=URL,json=chg_data,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHTTP(return_data,"changing guild")
    
    def LeaveGuild(self):
        # Leave a guild
        URL = BASEURL + "/users/@me/guilds/" + str(self.guildid)

        return_data = requests.delete(url=URL,json={},headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHttpNoReturn(return_data,"leaving guild")

    
    def TimeoutUser(self,user:User,timestamp_ISO8601_until):
        # Timeout user
        # NOT TESTED CORRECTLY!
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user.userid)

        data = {
            "communication_disabled_until":timestamp_ISO8601_until
        }

        return_data = requests.patch(url=URL,json=data,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHttpNoReturn(return_data,"timeouting user")
    
    def KickUser(self,user:User):
        # Kick user
        # NOT TESTED CORRECTLY!
        # THE ERROR MESSAGE IS A BIT WEIRDER BECAUSE THE KICK WILL RETURN A ERROR ONLY IF THE USER DOES NOT EXIST AT ALL
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user.userid)

        return_data = requests.delete(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHttpNoReturn(return_data,"kicking user")
    
    def BanUser(self,user:User,delete_message_seconds:int = 0):
        # BAN user
        # NOT TESTED CORRECTLY!
        # THE ERROR MESSAGE IS A BIT WEIRDER BECAUSE THE KICK WILL RETURN A ERROR ONLY IF THE USER DOES NOT EXIST AT ALL
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/bans/" + str(user.userid)

        data = {"delete_message_seconds":delete_message_seconds}

        return_data =  requests.put(url=URL,headers=self.header,json=data)

        return AnticordUtil.CheckErrResponsePlainHttpNoReturn(return_data,"banning user")

        
    
    def UnBanUser(self,user:User):
        # UnBan user
        # NOT TESTED CORRECTLY!
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/bans/" + str(user.userid)
        
        data = {}

        return_data = requests.delete(url=URL,headers=self.header,json=data)

        return AnticordUtil.CheckErrResponsePlainHttpNoReturn(return_data,"unbanning user")
        

    def GetGuildChannels(self) -> dict :
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/channels"

        return_data = requests.get(url=URL,headers=self.header)

        return_data_content = AnticordUtil.CheckErrResponsePlainHTTP(return_data,"getting guild channels")

        list_of_channels = []

        for i in return_data_content:
            list_of_channels.append(Channel(int(i["id"]),self.BOTParentToken))
        
        return list_of_channels
    
    def GetGuildWebhooks(self) -> dict :
            URL = BASEURL + "/guilds/" + str(self.guildid) + "/webhooks"

            return_data = requests.get(url=URL,headers=self.header)

            return_data_content = AnticordUtil.CheckErrResponsePlainHTTP(return_data,"getting guild webhooks")

            return return_data_content
    
    def GetGuildMembers(self,limit:int):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members?limit=" + str(limit)

        return_data = requests.get(URL,headers=self.header)

        return_data_content = AnticordUtil.CheckErrResponsePlainHTTP(return_data,"getting guild members")

        list_of_users = []

        for i in return_data_content:
            list_of_users.append(User(int(i["user"]["id"]),self.BOTParentToken))
        
        return list_of_users
    
    def GetGuildMember(self,user_id:int):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user_id)

        response = requests.get(URL,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHTTP(response,"getting guild member")

    def GetGuildRoles(self):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/roles"

        response = requests.get(URL,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHTTP(response,"getting guild roles")

### BOT ###
class BOT:
    def __init__(self,token:str) -> None:
        
        self.TOKEN = "Bot " + token

        self.header = {
            "Authorization" : self.TOKEN
        }

    def GetBotAttribute(self,attribute):
        # Get bot attribute
        URL = BASEURL + "/applications/@me"

        return_data = requests.get(url=URL,headers=self.header)

        return AnticordUtil.CheckErrResponseAttributeHTTP(return_data,"bot",attribute)
    
    def ChangeBotAttribute(self,chg_data:dict):
        # Change bot attribute
        URL = BASEURL + "/applications/@me"

        return_data = requests.patch(url=URL,json=chg_data,headers=self.header)

        return AnticordUtil.CheckErrResponsePlainHTTP(return_data,"changing bot")


    def GetChannelByID(self,id) -> Channel:
        return Channel(id,self.TOKEN)
    
    def GetGuildByID(self,id) -> Guild:
        return Guild(id,self.TOKEN)
    
    def GetUserByID(self,id) -> User:
        return User(id,self.TOKEN)
    
    def GetBotGuilds(self) -> list:
        URL = BASEURL + "/users/@me/guilds"

        response_data = requests.get(url=URL,headers=self.header)
        return_data = AnticordUtil.CheckErrResponsePlainHTTP(response_data,"getting bot guilds")

        guild_list = []
        for i in return_data:
            guild_list.append(self.GetGuildByID(i["id"]))

        return guild_list
    
