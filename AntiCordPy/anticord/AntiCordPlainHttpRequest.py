


import requests
import json

BASEURL = "https://discord.com/api"

### CHANNEL ###
class Channel:
    def __init__(self,channelid:int,BOTParentToken:str) -> None:
        self.channelid = channelid

        self.BOTParentToken = BOTParentToken
        self.header = {
            "Authorization" : BOTParentToken
        }

    def SendMessage(self,content:str):
        URL = BASEURL + "/channels/" + str(self.channelid) + "/messages"

        data = {
            "content":content,
            "enforce_nonce":False
        }

        return json.loads(requests.post(url=URL,data=data,headers=self.header).content)
    
    def DeleteMessage(self,messageid:int):

        URL = BASEURL + "/channels/" + str(self.channelid) + "/messages/" + str(messageid)

        return json.loads(requests.delete(url=URL,headers=self.header).content)
    
    def DeleteGuildChannel(self):
        URL = BASEURL + "/channels/" + str(self.channelid)

        return json.loads(requests.delete(url=URL,headers=self.header).content)
    
    def ChangeGuildChannelName(self,new_name:str):
        URL = BASEURL + "/channels/" + str(self.channelid)

        data = {
            "name":new_name
        }

        return json.loads(requests.patch(url=URL,headers=self.header,json=data).content)
    
    def CreateInivte(self):
        URL = BASEURL + "/channels/" + str(self.channelid) + "/invites"
        return json.loads(requests.post(url=URL,headers=self.header).content)
    
    def GetChannelName(self):
        URL = BASEURL + "/channels/" + str(self.channelid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["name"]

        return return_data
    
    def GetChannelTopic(self):
        URL = BASEURL + "/channels/" + str(self.channelid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["topic"]

        return return_data
    
    def GetChannelType(self):
        URL = BASEURL + "/channels/" + str(self.channelid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["type"]

        return int(return_data)
    
    def IsChannelNsfw(self):
        URL = BASEURL + "/channels/" + str(self.channelid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["nsfw"]

        return return_data
    
    def IsChannelErrorfull(self):
        URL = BASEURL + "/channels/" + str(self.channelid)

        rq = requests.get(url=URL,headers=self.header)

        if rq.status_code != 200:
            return True,rq.status_code,json.loads(rq.content)
        else:
            return False

### USER ###
class User:
    def __init__(self,userid:int,BOTParentToken:str) -> None:
        self.userid = userid
        self.BOTParentToken = BOTParentToken
        self.header = {
            "Authorization" : BOTParentToken
    }
        
    def CreateUserDm(self) -> Channel:
        URL = BASEURL + "/users/@me/channels"

        data = {
            "recipient_id":self.userid
        }
        
        response_data = requests.post(url=URL,headers=self.header,json=data).content

        try:
            return_data = json.loads(response_data)
            return_data = return_data["id"]

            return Channel(return_data,self.BOTParentToken)
        except:
            return None

        
    
    def GetUserName(self):
        URL = BASEURL + "/users/" + str(self.userid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["username"]

        return return_data
    
    def GetUserGlobalName(self):
        URL = BASEURL + "/users/" + str(self.userid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["global_name"]

        return return_data
    
    def GetUserDiscriminator(self):
        URL = BASEURL + "/users/" + str(self.userid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["discriminator"]

        return return_data
    
    def GetUserAvatar(self):
        URL = BASEURL + "/users/" + str(self.userid)
        
        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["avatar"]

        return str(return_data)
    
    def IsUserErrorfull(self):
        URL = BASEURL + "/users/" + str(self.userid)

        rq = requests.get(url=URL,headers=self.header)

        if rq.status_code != 200:
            return True,rq.status_code,json.loads(rq.content)
        else:
            return False
    

    
### GUILD ###
class Guild:
    def __init__(self,guildid:int,BOTParentToken:str) -> None:
        self.guildid = guildid
        self.BOTParentToken = BOTParentToken
        self.header = {
            "Authorization" : BOTParentToken,
            'Content-Type': 'application/json'
    }
    
    def GetGuildName(self):
        URL = BASEURL + "/guilds/" + str(self.guildid)

        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["name"]

        return return_data
    
    def GetGuildIcon(self):
        URL = BASEURL + "/guilds/" + str(self.guildid)

        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["icon"]

        return return_data
    
    def GetGuildDescription(self):
        URL = BASEURL + "/guilds/" + str(self.guildid)

        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)
        return_data = return_data["description"]

        return return_data
    
    def IsGuildErrorfull(self):
        URL = BASEURL + "/guilds/" + str(self.guildid)

        rq = requests.get(url=URL,headers=self.header)

        if rq.status_code != 200:
            return True,rq.status_code,json.loads(rq.content)
        else:
            return False

    
    def CreateGuildChannelText(self,name:str,topic:str = ""):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/channels"

        data = {
            "name":name,
            "topic":topic,
            "type":0
        }

        return Channel(json.loads(requests.post(url=URL,json=data,headers=self.header).content)["id"],self.BOTParentToken)

    def ChangeGuildName(self,NewName:str):
        URL = BASEURL + "/guilds/" + str(self.guildid)

        data = {
            "name":NewName
        }

        return json.loads(requests.patch(url=URL,json=data,headers=self.header).content)
    
    def DoesGuildMemberHaveRole(self,role_id:int,user:User):
            guild = Guild(self.guildid,self.BOTParentToken)

            if guild.GetGuildMember(user.userid)["roles"] == []:
                return False
            else:
                for i in guild.GetGuildMember(user.userid)["roles"]:

                    i = int(i)
                    if role_id == i:
                        return True
                
                return False

    
    def TimeoutUser(self,user:User,timestamp_ISO8601_until):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user.userid)

        data = {
            "communication_disabled_until":timestamp_ISO8601_until
        }

        return json.loads(requests.patch(url=URL,json=data,headers=self.header).content)
    
    def KickUser(self,user:User):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user.userid)

        return json.loads(requests.delete(url=URL,headers=self.header).content)
    
    def BanUser(self,user:User,delete_message_seconds:int = 0):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/bans/" + str(user.userid)

        data = {"delete_message_seconds":delete_message_seconds}

        return json.loads(requests.put(url=URL,headers=self.header,json=data).content)
    
    def UnBanUser(self,user:User):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/bans/" + str(user.userid)
        
        data = {}

        return json.loads(requests.delete(url=URL,headers=self.header,json=data).content)

    def GetGuildChannels(self):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/channels"

        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)

        channel_list = []
        for i in return_data:
            channel_list.append(Channel(i["id"],self.BOTParentToken))

        return channel_list
    
    def GetGuildMembers(self,limit:int):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members?limit=" + str(limit)

        responsedata = requests.get(URL,headers=self.header)
        responsedata = json.loads(responsedata.content)

        memberlist = []
        for i in responsedata:
            memberlist.append(User(i["user"]["id"],self.BOTParentToken))

        return memberlist
    
    def GetGuildMember(self,user_id:int):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user_id)

        return json.loads(requests.get(URL,headers=self.header).content)
    
    def GetGuildMemberAsInObject(self,user_id:int):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/members/" + str(user_id)

        return User(json.loads(requests.get(URL,headers=self.header).content)["user"]["user_id"],self.BOTParentToken)
    

    def GetMemberAsInObjectByName(self,name:str):
        for i in Guild(self.guildid,self.BOTParentToken).GetGuildMembers(1000):
            if i.GetUserName() == name:
                return i
                
        return None

    def GetGuildRoles(self):
        URL = BASEURL + "/guilds/" + str(self.guildid) + "/roles"

        return json.loads(requests.get(URL,headers=self.header).content)
    

### BOT ###
class BOT:
    def __init__(self,token:str) -> None:
        
        self.TOKEN = "Bot " + token

        self.header = {
            "Authorization" : self.TOKEN
        }


    def GetChannelByID(self,id) -> Channel:
        return Channel(id,self.TOKEN)
    
    def GetGuildByID(self,id) -> Guild:
        return Guild(id,self.TOKEN)
    
    def GetUserByID(self,id) -> User:
        return User(id,self.TOKEN)
    
    def GetBotGuilds(self) -> list:
        URL = BASEURL + "/users/@me/guilds"

        return_data = requests.get(url=URL,headers=self.header).content
        return_data = json.loads(return_data)

        guild_list = []
        for i in return_data:
            guild_list.append(self.GetGuildByID(i["id"]))

        return guild_list