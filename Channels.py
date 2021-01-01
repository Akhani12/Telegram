import re

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

from Forex.Filter import stuck


def Channels(client):
    chats = []
    last_date = None
    chunk_size = 200
    groups = []

    result = client(GetDialogsRequest(
        offset_date=last_date,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=chunk_size,
        hash=0
    ))
    chats.extend(result.chats)

    for chat in chats:
        try:
            if chat.broadcast == True:  # megagroup
                groups.append(chat)
        except:
            continue
    print('From Which Group Yow Want To Scrap A Members:')
    i = 0
    for g in groups:
        print(str(i) + '- ' + g.title)
        i += 1

    return groups

# Buy limit, Buy Stop, Sell Limit, Sell Stop
# file_path = r"C:\Users\DELL\PycharmProjects\Exam\Forex\dtaa.csv"
#         df = pd.read_csv(file_path)
#         df = df.append({'Pair': [],
#                         'Action': [],
#                         'Price': [],
#                         'TP1': [],
#                         'TP2': [],
#                         'TP3': [],
#                         'TP4': [],
#                         'TP5': [],
#                         'TP6': [],
#                         'TP7': [],
#                         'Channel Name': [],
#                         'NY Date': [],
#                         'NY Time': [],
#                         'Update 1': [],
#                         'Update 2': [],
#                         'Update 3': [],
#                         'Update 4': []}, ignore_index=True)
#         df.to_csv(file_path,index=False)
