"""
Task_3 Version 0.4

! edit config.py !

Script can join public, private groups and 
solve arithmetic captcha from bot

DB and class CaptchSolver are not ready yet
"""

from telethon import TelegramClient, events
from telethon import functions
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import CheckChatInviteRequest
import asyncio
import re

from config import API_ID, API_HASH, MY_PHONE

client = TelegramClient('Michael', API_ID, API_HASH)

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


# answer to bot captcha like "(3 + 5) @user, Answer..."
@client.on(events.NewMessage(pattern="^[(0-9) +]+"))
async def captcha_handler(event):
    pattern = re.compile("^[(0-9) +]+")
    string = event.message.message
    statement = pattern.search(string)
    if statement:
        statement = statement.group(0)
        numbers = statement.split('+')
        for i in range(len(numbers)):
            f = filter(str.isdigit, numbers[i])
            numbers[i] = "".join(f)
            
        res = int(numbers[0]) + int(numbers[1])
        await event.respond(str(res))
    
async def main():
    await client.start(MY_PHONE)

    chat_id1 = await joinPublicGroup('vstup_kpi_chat')
    chat_id2 = await joinPrivateGroup('31oiRB1tMoIwNzMy')
    print(chat_id1)
    print(chat_id2)

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())