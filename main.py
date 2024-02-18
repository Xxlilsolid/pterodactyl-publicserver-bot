from pydactyl import PterodactylClient
import discord
from discord.ext import commands
from discord import app_commands
from discord import Interaction
import asyncio
import nest_asyncio

# Patches asyncio module

nest_asyncio.apply()


# Variables

suspended = 0
owner = 
isServerUp = False
api = PterodactylClient('', '')
srv_id = ""
srv_utilization = api.client.servers.get_server_utilization(srv_id)



publicBot = ""


discordToken = publicBot





client = discord.Client(command_preifx = "!", intents= discord.Intents.all())
tree = app_commands.CommandTree(client)


@client.event 
async def on_ready():

    # Variables 

    global isServerUp

    # On Start Stuff

    owner_user = await client.fetch_user(owner)
    synced = await tree.sync()
    print('We have logged in as {0.user}'.format(client))
    print(f"Synced {len(synced)} commands")
    print(f"The owner of the server is "+ str(owner_user))
    #print(srv_utilization)

    
    #Check current state of server

    if "running" in srv_utilization['current_state']:
        isServerUp = True
        print("Server is active")
    
    else:
        
        isServerUp = False
        print("Server is inactive")



# Sync Command


@tree.command(name='sync', description='Owner only')
async def sync(interaction: discord.Interaction):
    if interaction.user.id == owner:
        await tree.sync()
        print('Command tree synced.')
        await interaction.response.send_message(f"Command Tree synced", ephemeral=True)
    else:
        await interaction.response.send_message('You must be the owner to use this command!', ephemeral=True)


# Start Commanmd

@tree.command(name="start", description="It will start the server")
async def start(interaction : discord.Interaction):
    
    # Variables

    global isServerUp
    global srv_utilization
    global srv_id
    global api
    
    user = 0

    # IsServerUp Determiner

    srv_utilization = api.client.servers.get_server_utilization(srv_id)



    if "running" in srv_utilization['current_state']:
        isServerUp = True
        print("Server is up!")
    
    else:
        isServerUp = False
        print("Server is down")




# Main Payload



    if suspended == 0:
        
        if isServerUp == False:
            await interaction.response.send_message(f"Server is going up, please wait a while, we will DM you when its up! Make sure to enable DMS from this server!", ephemeral=True)
            
            startServer()
            while isServerUp == False:
                await asyncio.sleep(5)
                srv_utilization = api.client.servers.get_server_utilization(srv_id)
                if "running" in srv_utilization['current_state']:
                    user = await interaction.user.create_dm()
                    userid = interaction.user.id
                    await user.send(f"Hi <@"+str(userid)+">, the server is now up! Enjoy! ")
                    isServerUp = True
                    
                
                else:
                    pass
                   # print("Retrying! "+srv_utilization['current_state'])


        elif isServerUp == True:
            await interaction.response.send_message(f"Server is already up! Join in on the action!", ephemeral=True)
        
    
    elif suspended == 1:
        owner_dm = await client.fetch_user(owner)
        await interaction.response.send_message(f"There is a problem with the server panel. I have contacted the server owner for you!", ephemeral=True)
        await owner_dm.send(f"Hey, just warning you that the server is suspended! If you use a server such as SliceHosting you will want to visit the site BEFORE 2-3 days otherwise the server will be deleted!")




















def startServer():
    # Global variables

    global suspended
    global srv_utilization

    runningCheck = False

    # New Code should hopefully find out weather the server is suspended or not!

    while runningCheck == False:
        try:
            api.client.servers.send_power_action(srv_id, 'start')
            print("Start signal requested!")
            suspended = 0
            runningCheck = True
        
        except:
            print("Contact Me")
            suspended = 1

    
    
        
        

        

 





client.run(discordToken)

