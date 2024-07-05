# REMEMBER , THIS WAS MADE BY AN ANTIFURRY

`pip install anticord`

# DOCUMENTATION

## AntiCordPlainHttpRequest:

- Plain http requests to the discord api

- May have some layers of abstractions added to it

### CLASSES:

- Every class will have a `BOTParentToken` and a specific id `channelid`,`guildid`,`userid` and so on

- BOT class is an exception

#### Channel:

- A discord guild cahnnel

**Atributes:**

1.  `channelid` - `int` - `The channel id`

2.  `BOTParentToken` - `str` - `The owner bot token`

3.  `heaader` - 'dict' - `Header used for requests , will be created after you make a channel object`

**Functions:**

`SendMessage(content:str):`

- Will attempt sending a message with `content` in the channel

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to send the message (yet)**

`DeleteMessage(messageid:int):`

- Will attempt to delete a message with the `messageid` in the channel

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to delete the message (yet)**

`DeleteGuildChannel()`

- Will attempt to delete the channel

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to delete the channel (yet)**

`ChangeGuildChannelName(new_name:str):`

- Will attempt to change the channel's name to `new_name`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to rename the channel (yet)**

`CreateInivte():`

- Will attepmt to create an invite using the channel

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to make an invite (yet)**

`GetChannelName():`

- Will attempt to get the channel's name

- Will return the channel's name (str)

- **May give an error if it fails to do so**

`GetChannelTopic():`

- Will attempt to get the channel's topic

- Will return the channel's topic (str)

- **May give an error if it fails to do so**

`GetChannelType():`

- Will attempt to get the channel's type

- Will return the channel's type (corresponding to discord docs) (int)

- **May give an error if it fails to do so**

`IsChannelNsfw():`

- Will attempt to see if the channel is nsfw or not

- Will return a boolean (if the channel is nsfw or not)

- **May give an error if it fails to do so**

`IsChannelErrorfull():`

- Will attempt to see if the channel will give an error when you send a request or not

- If the discord api does not respond with status `200` (okay) on a get channel request then it is gonna return True (boolean) with the content returned in that request (dict) , otherwise if discord responds with `200` (okay) its gonna return false with no content

#### User:

- A discord user/bot

**Atributes:**

1.  `userid` - `int` - `The user id`

2.  `BOTParentToken` - `str` - `The owner bot token`

3.  `header` - `dict` - `Header used for requests , will be created after you make a user object`

**Functions:**

`CreateUserDm():`

- Will attempt to make a user dm channel

- Will return a channel object

- **May give an error if it fails to do so**

`GetUserName():`

- Will attempt to get the user's name

- Will return the user's name (str)

- **May give an error if it fails to do so**

`GetUserGlobalName():`

- Will attempt to get the user's global name

- Will return the user's global name (str)

- **May give an error if it fails to do so**

`GetUserDiscriminator():`

- Will attempt to get the user's discriminator

- Will return the user's discriminator (str)

- **May give an error if it fails to do so**

`GetUserAvatar():`

- Will attempt to get the user's avatar

- Will return the user's avatar hash (str)

- **May give an error if it fails to do so**

`IsUserErrorfull():`

- Will attempt to see if the user will give an error when you send a request or not

- If the discord api does not respond with status `200` (okay) on a get user request then it is gonna return True (boolean) with the content returned in that request (dict) , otherwise if discord responds with `200` (okay) its gonna return false with no content

#### Guild:

- A discord guild

**Atributes:**

1.  `guildid` - `int` - `The guild id`

2.  `BOTParentToken` - `str` - `The owner bot token`

3.  `header` - `dict` - `Header used for requests , will be created after you make a guild object`

**Functions:**

`GetGuildName():`

- Will attempt to get the guild's name

- Will return the guild name (str)

- **May give an error if it fails to do so**

`GetGuildIcon():`

- Will attempt to get the guild's icon

- Will return the guild's icon hash (str)

- **May give an error if it fails to do so**

`GetGuildDescription():`

- Will attempt to get the guild's description

- Will return the guild's description (str)

- **May give an error if it fails to do so**

`IsGuildErrorfull():`

- Will attempt to see if the guild will give an error when you send a request or not

- If the discord api does not respond with status `200` (okay) on a get guild request then it is gonna return True (boolean) with the content returned in that request (dict) , otherwise if discord responds with `200` (okay) its gonna return false with no content

`CreateGuildChannelText(name:str,topic:str = ""):`

- Will attempt to create a text channel in the guild

- Will return the channel created

- **No builtin error that will show up if the application fails to create the channel (yet)**

`ChangeGuildName(NewName:str):`

- Will attempt to change the guild's name to `NewName`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to change the guild name (yet)**

`DoesGuildMemberHaveRole(role_id:int,user:User):`

- Will attempt to see if `user` has a role with the id `role_id` in the guild

- Will return true if the user does , otherwise will return false

- **May return an error or will return false**

`TimeoutUser(user:User,timestamp_ISO8601_until):`

- Will attempt to timeout `user` until `timestamp_ISO8601_until`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to timeout the user (yet)**

`KickUser(self,user:User):`

- Will attempt to kick `user`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to kick the user (yet)**

`KickUser(self,user:User):`

- Will attempt to kick `user`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to kick the user (yet)**

`BanUser(user:User,delete_message_seconds:int = 0):`

- Will attempt to ban `user` and delete the messages after the date `delete_message_seconds`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to ban the user (yet)**

`UnBanUser(user:User):`

- Will attempt to unban `user`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to unban the user (yet)**

`GetGuildChannels():`

- Will attempt to list the guild's channels

- Will return a list of channel objects

- **May return empty list or an error**

`GetGuildMembers(limit:int):`

- Will attempt to return a lsit of the server users , limited by `limit` , max being 1000

- Will return a list of user objects

- **WILL NOT SHOW ALL MEMBERS IN SERVERS WITH 1K+ MEMBERS SCINCE MAX LIMIT IS 1000**

- **May return error or empty list**

`GetGuildMember(user_id:int):`

- Will attempt to return the data of the user in the guild where user has the user id equal to `user_id`

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to get the user (yet)**

`GetGuildMemberAsInObject(user_id:int):`

- Same as `GetGuildMember` but returns an user object

`GetMemberAsInObjectByName(name:str):`

- Same as `GetGuildMemberAsInObject` but it gets the user where name is equal to `name`

`GetGuildRoles():`

- Will attempt to get the guild`s roles

- Will return a dict : the json response from the discord api

- **No builtin error that will show up if the application fails to get the user (yet)**

#### BOT:

- A discord bot

**Atributes:**

1.  `TOKEN` - `str` - `The bot's token`

2.  `header` - `dict` - `Header used for requests , will be created after you make a BOT object`

**Functions:**

`GetChannelByID(id):`

- Will return a channel object with the channelid = `id`

`GetGuildByID(id):`

- Will return a guild object with the guildid = `id`

`GetUserByID(id):`

- Will return a user object with the userid = `id`

`GetBotGuilds():`

- Will attempt to list all the bot's guilds

- Will return a list of guild objects

- **May show an error or it will return an empty string**

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
