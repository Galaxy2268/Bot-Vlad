from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup

client = commands.Bot(command_prefix='.')


# Connect_status
@client.event
async def on_ready():
    print('Bot connected')


# .commands
@client.command(pass_context=True)
async def commands(ctx):
    await ctx.send(f'```{"".join(open("help.txt", "r", encoding="utf8").readlines())}```')


# .hello
@client.command(pass_context=True)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'{author.mention} Hello!')


# .physics0
@client.command(pass_context=True)
async def physics0(ctx):
    await ctx.send(f'```{"".join(open("formulas0.txt", "r", encoding="utf8").readlines())}```')


# .physics1
@client.command(pass_context=True)
async def physics1(ctx):
    await ctx.send(f'```{"".join(open("formulas1.txt", "r", encoding="utf8").readlines())}```')


# .wg
@client.command(pass_context=True)
async def wg(ctx):
    r = requests.get(url='https://api.waifu.pics/sfw/waifu')
    data = r.json()
    await ctx.send(data['url'])


# .wgnsfw
@client.command(pass_context=True)
async def wgnsfw(ctx):
    r = requests.get(url='https://api.waifu.pics/nsfw/waifu')
    data = r.json()
    await ctx.send(data['url'])


URL = f"https://api.waifu.pics/sfw/waifu"


# .izm
@client.event
async def on_ready():
    channel = client.get_channel(channel_id)
    previous_content = ""

    while True:
        await asyncio.sleep(60)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        events_div = soup.find('div', {'class': 'r64-events'})
        text_content = events_div.text.strip()

        print(f"Current message: {text_content}")
        print(f"Previous message: {previous_content}")

        if text_content != previous_content:
            await channel.send(f'```{text_content}```')
            previous_content = text_content


channel_id = 814166440671969336
url = 'https://www.r64vsk.lv'

# Token


token = open('token.txt', 'r').readline()

client.run(token)
