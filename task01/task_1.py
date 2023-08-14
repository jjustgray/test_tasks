"""
Task_1 Version 0.4

! edit config.py !

Everything is working as it must be
"""

from telethon import TelegramClient
from telethon import functions, utils
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import CheckChatInviteRequest

import asyncio
import json

from config import API_ID, API_HASH, MY_PHONE


client = TelegramClient('Session', API_ID, API_HASH)


async def joinPublicGroup(groupname):
    update = await client(functions.channels.JoinChannelRequest(
        channel = groupname
    ))
    group_ID = str(update.chats[0].id)
    return group_ID


async def joinPrivateGroup(link):
    try:
        update = await client(ImportChatInviteRequest(link))
        group_ID = str(update.chats.Chat.id)
        return group_ID
    except:
        update = await client(CheckChatInviteRequest(link))
        group_ID = str(update.chat.id)
        return group_ID


async def getUsersInfo(chat_id):
    users = await client.get_participants(chat_id)
    users_dict = {}
    for i in users:
        users_dict[i.username] = {
            "name": i.first_name,
            "last_name": i.last_name
            }
    
    return users_dict


def writeDictToJSON(usersDict):
    with open('users.json', 'w') as f:
        json.dump(usersDict,
                  f,
                  ensure_ascii = False,
                  indent = 3)

    return json.dumps(usersDict, ensure_ascii = False, indent = 3)
   

async def main():
    await client.start(MY_PHONE)

    
    chat = await joinPublicGroup('vstup_kpi_chat')
    chat_id = int('-100' + (chat))
    # chats_id = []
    # # get all chat ids in list
    # async for dialog in client.iter_dialogs():
    #     tmp = utils.resolve_id(dialog.id)
    #     chats_id.append(tmp[0])
    #     print('{:>14}: {}'.format(dialog.id, dialog.title))
    usersInfo = await getUsersInfo(chat_id)
    userInfoJSON = writeDictToJSON(usersInfo)
    print(userInfoJSON)

    await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())