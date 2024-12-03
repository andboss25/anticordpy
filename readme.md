# ANTICORD (anticordpy)

![anticord logo](https://github.com/andboss25/anticordpy/raw/main/Anticord_logo.jpg?raw=true)

### REMEMBER , THIS LIBRARY WAS MADE BY AN ANTI-FURRY 🐺🚫

---

#### **THIS PROJECT IS STILL IN DEVELOPMENT , AND IT LACKS SOME FEATURES , FEEL FREE TO SUPPORT THIS PROJECT AND CONTRIBUTE , WE WILL GREATLY APPRECIATE THIS**

## ABOUT

### anticord is a discord python library meant for:

- Another aproach at the discord api
- A lower level attachment to the discord api

### this is not specifically meant for beginers

- you may need to have a bit of knowlege on how the discord api works
- you may need to have a tab with the discord api docs open while writing code in this library

## **check demos folder (in the github page) for examples**

To install the library using pip , please do:

`pip install anticord`

# DOCUMENTATION

### Some information:

- Most functions have errors and will return errors if they failed to do a set action

- Most function will return the json body from the request but some other won't

- The library is split into two importable files with functions in them

- One of them is used for plain simple http requests and the other is used for gateway events and such

### Errors:

- Will usually return the message from discord api along with the code
- There may be exceptions

## AntiCordPlainHttpRequest:

- Plain HTTPS requests to the discord api
- Specific functions for your requests

### CLASSES:

- Every class will usually have a `BOTParentToken` (THE TOKEN OF BOT WHO OWNS THE OBJECT) and a specific id like: `channelid`,`guildid`,`userid` and so on
- BOT class is an exception to this
- Most classes will have a get attribute function and maybe a change attribute one (stuff like `changechannelattribute(chg_data:dict)`)
- Most classes will have a header object that will be used to send requests (contains token)

---

#### Channel:

- A discord guild channel

**Functions (self explanatory):**

`SendMessage(content:str):`
`DeleteMessage(messageid:int):`
`DeleteGuildChannel()`
`CreateInivte():`
`GetChannelAttribute(attribute):`

---

#### User:

- A discord user/bot/member

**Functions (self explanatory):**
`CreateUserDm():`
`GetUserAttribute(attribute):`

---

#### Guild:

- A discord guild

**Functions (self explanatory):**
`GetGuildAttribute(attribute):`
`CreateGuildChannelText(name:str,topic:str = ""):`
`ChangeGuildAttribute(chg_data:dict):`
`LeaveGuild()`
`DoesGuildMemberHaveRole(role_id:int,user:User):`
`TimeoutUser(user:User,timestamp_ISO8601_until):`
`KickUser(self,user:User):`
`BanUser(user:User,delete_message_seconds:int = 0):`
`UnBanUser(user:User):`
`GetGuildChannels():`
`GetGuildWebhooks():`
`GetGuildMembers(limit:int):`
`GetGuildMember():`
`GetGuildRoles()`

---

#### BOT:

- A discord bot

**Functions:**

`GetChannelByID(id):`
`GetGuildByID(id):`
`GetUserByID(id):`
`GetBotGuilds():`
`GetBotAttribute(attribute):`
`ChangeBotAttribute(chg_data:dict):`

---

# Get bot attribute

## AntiCordGateway:

- Handles the stuff related to the discord gateway (events)

- Has abstractions

### CLASSES:

##### GatewayWebsocket:

- a gateway websocket

**Atributes:**

`WebSocket` - its websocket object (uses the websocket library)

`Token` - the bot token (str)

**Functions:**

`CreateGatewayObj(Token:str):`

- Returns a GatewayWebsocket object with the token

`CreateConnection():`

- Will make a connection (adds a websocket object and makes a hearthbeat thread)

'SendIntents(Intents:int):'

- Will send the given intents (read discord api and use a intent calculator)

- Will return 0 if it recived a ready opcode , if not , it will return 1

`ReciveEvent():`

- Will recive an event from discord , it ignores the 11 opcode (ack opcode)

### SOME INSTRUCTIONS TO USE:

- first you have to create the gateway object

- then you will need to create a connection with the gateway objectx

- after that you can send your intents and listen for events

- you can also look in the demos if you dont know how to do this
