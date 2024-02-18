# pterodactyl-publicserver-bot

Are you tired of making someone start up a server through the control panel?
Look no further with the Pterodactyl-publicserver-bot!

‼️ SERVER OWNERS ‼️

This bot doesnt work out of the box. You will need to change some things in main.py!

Variables!

owner = "Must be you owner id on the discord server" (potentially will be removed later when I get the chance lmao)

api = PterodactylClient("Server panel url e.g: https://panel.slicehosting.tech", "Your api key, you must make one in account settings!")

srv_id = "Server id. You can find this in server settings. You will want the first string of letters before the dash!"

publicBot = "This will be your discord bot token! DO NOT SHARE THIS WITH ANYONE"

Requirements.txt is only used if you are using a hosting platform that requries this!

If you are running this in a VM or on a pc, make sure to have the latest version of python and PiP installed alongside having the packages present in requirements.txt!

‼️ USAGE ‼️

Currently there is one command, /start.
/start will start the server. If its up it will let you know and if its down it will start the server and will notify you when the server is up in DMS. The bot uses ephemals to prevent the server from clogging up with messages from the bot!





I would greatly appreciate it if you credit me if you choose to modify and distribute my work!
