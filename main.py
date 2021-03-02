# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import discord
from discord import Member
from discord import Message

import numpy as np

from decouple import config
import requests
import json
import re

TOKEN = config('TOKEN')

client = discord.Client()


base_command_rgx = "^bot roll "
dices_rgx = "(?P<n_dices>\d+)\s*d\s*(?P<n_sides>\d+)"
modifiers_rgx = "(?P<mod_exp>(\s*[-+]\s*\d+)*)"
roll_pattern = f"{base_command_rgx}{dices_rgx}{modifiers_rgx}"

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
    msg_match = re.search(roll_pattern, message.content)
    if msg_match:
        author: Member = message.author
        #await author.send("test")



        bot_response = f"{author.name}, wants to roll the dices"

        # await message.channel.send(bot_response)
        # await message.channel.send("Let's do it!")

        #  - Roll -

        num_dices = int(msg_match.group('n_dices'))
        num_sides = int(msg_match.group('n_sides'))
        modifier_str = msg_match.group('mod_exp')

        rolls = [np.random.randint(1, 1 + num_sides) for i in range(num_dices)]

        rolls_str = ' + '.join(map(str, rolls))
        rolls_result = np.sum(rolls)

        modif_desc = f" + [{modifier_str}]" if modifier_str else ""
        roll_desc = f"({rolls_str}){modif_desc}"
        rolls_result = rolls_result + num_dices*(eval(modifier_str) if modifier_str else 0)

        auth_name = author.name if author.nick is None else author.nick
        bot_response = f"**{auth_name}** \n *{roll_desc}* \n **{rolls_result}**"

        await message.channel.send(bot_response)



client.run(TOKEN)

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
