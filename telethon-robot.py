from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon import functions, types
from telethon import TelegramClient
from telethon import events
import asyncio
with TelegramClient('Login',api_id=put your apid format int ,api_hash="put your api hash") as client:
     @client.on(events.NewMessage(pattern='(?i).*info'))
     async def get_list(event):
     	user_list = []
     	channel_list = []
     	bot_list = []
     	group_list = []
     	admin = []
     	not_admin = []
     	dialogs = await client.get_dialogs()
     	for dialog in dialogs:
     		title = dialog.title
     		if getattr(dialog.entity,'bot',None):
     			bot_list.append(title)
     		elif dialog.is_group:
     			group_list.append(dialog.title)
     		elif dialog.is_channel:
     			channel_list.append(dialog.title)
     			if getattr(dialog.entity,'admin_rights',None):
     			 	admin.append(dialog.title)
     			else:
     				not_admin.append(dialog.title)
     		else:
     			user_list.append(dialog.title)
     	await client.send_message('me', f'user list:\n{user_list}\nchannel list\n{channel_list}\nbot list \n{bot_list}\ngroup list \n {group_list}\nchannel admin\n{admin}\nnot admin channel\n{not_admin}')
     client.run_until_disconnected()

