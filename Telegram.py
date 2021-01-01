from telethon import TelegramClient
from Forex.Channels import Channels
from Forex.Filter import stuck

# Telegram Api Credentials....
phone = "number"
api_id = int("your api id ")
api_hash = 'api_hash'
client = TelegramClient(phone, api_id, api_hash)
# async def main():
#     await client.send_message('me', 'Hello !!!!')
# with client:
#     client.loop.run_until_complete(main())

# Connect Telegram Api Bot...
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter verification code: '))

# This is For From Which Groups You Scrap Data...
groups = Channels(client)

numList_forward = list(map(int, input("Enter Your Source Channel Number With Space(Ex.23 45 1 7):").strip().split()))[
                  :20]
for forward in numList_forward:

    # Getting Group Or Channel Name...
    target_group = groups[int(forward)]
    channel_name = target_group.title

    # Get From The Channels....
    for message in client.iter_messages(target_group):
        client.connect()
        print(message.text)


        def Filter_data(pair, cursor, reply_message):
            # List Of All Things...
            database_list = ['buy', 'sell', 'price', 'be', 'cmp', 'selllimit', 'sellstop', 'buystop', 'buylimit', 'sl',
                             'tp', 'tp1', 'tp2', 'tp3', 'tp4', 'tp5', 'tp6', 'tp7']

            # This Is The Final Message...
            final_message = ''

            # Get Value From Database....
            for key_word in database_list:
                cursor.execute("SELECT " + key_word + "  FROM stock_data WHERE pair = '" + pair + "'")
                query_results = cursor.fetchone()

                # print(query_results)
                try:
                    query_results = ''.join(map(str, query_results)).lower()
                except Exception:
                    pass
                # print(query_results)

                if query_results == 'none':
                    pass
                elif key_word == 'price':
                    final_message = final_message + "\n" + (pair + ":" + str(query_results))

                elif key_word == 'buy':
                    final_message = final_message + "\n" + (pair + " " + key_word.capitalize() + "@" + str(query_results))

                elif key_word == 'sell':
                    final_message = final_message + "\n" + (pair + " " + key_word.capitalize() + "@" + str(query_results))
                elif key_word == 'tp':
                    if key_word == 'none':
                       final_message = final_message + "\n" + (key_word.capitalize() + ": Open")
                    final_message = final_message + "\n" + (key_word.capitalize() + ":" + str(query_results))

                else:
                    final_message = final_message + "\n" + (key_word.capitalize() + ":" + str(query_results))

            # Final Which Send To Channels....
            if 'sl' in final_message:
                print(final_message)
                pro = "Provider:" + input("Enter Your Provider Number:")
                spe_text = input("Enter Any Free Text:")
                final_message = reply_message + "\n" + final_message + "\n" + pro + "\n" + spe_text

                # Selection For Staging Channel OR Forward Channels....
                print("1 is for staging channel.\n2 is for forward channel")
                choose = int(input("Enter your Option:"))

                # This Is For Staging Channel....
                if choose == 1:

                    # Getting List Of All Groups...
                    groups = Channels(client)
                    numList_forward = list(map(int, input("Enter Your Stagging Channel List:").strip().split()))[:20]
                    for forward in numList_forward:
                        try:
                            target_group = groups[int(forward)]

                            # Send Message To Selected Groups....
                            async def main():
                                final_forward = channel_name + "\n" + final_message
                                await client.send_message(target_group, final_forward)

                            with client:
                                client.loop.run_until_complete(main())
                        except Exception:
                            pass

                # This Is For Forward Channel...
                elif choose == 2:

                    # Getting List Of All Groups...
                    groups = Channels(client)
                    numList_forward = list(
                        map(int, input("Enter Your List From Which Staging You Want:").strip().split()))[
                                      :20]
                    for forward in numList_forward:

                        target_group = groups[int(forward)]

                        all_chat = []
                        for message in client.iter_messages(target_group):
                            all_chat.append(message)
                        i = 0
                        for message_stag in all_chat:
                            print(str(i) + '- ' + message_stag)
                            i += 1
                        numList_forward = list(
                            map(int, input("Enter Your Message List Which You Want To Forward:").strip().split()))[:20]
                        for forward in numList_forward:
                            msg = all_chat[int(forward)]

                            groups = Channels(client)
                            numList_forward = list(map(int, input("Enter Your Forward Channel List:").strip().split()))[
                                              :20]
                            for forward in numList_forward:
                                target_group_forward = groups[int(forward)]
                                msg.forward_to(target_group_forward)


        # Verification For Its Reply Or Not...
        if message.is_reply:
            # reply_message = message.text
            # main_m = message.get_reply_message()
            # pair, cursor = stuck(main_m)
            # Filter_data(pair, cursor,reply_message)
            pass

        else:
            # Getting Pair Name And Postgres Cursor ...
            pair, cursor = stuck(message)
            Filter_data(pair, cursor, '')
