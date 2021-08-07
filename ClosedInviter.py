# インストールした discord.py を読み込む
import discord

from discord.ext import commands

# 自分のBotのアクセストークンに
f = open('TOKEN.txt', 'r')
TOKEN = f.read()
f.close()

# 接続に必要なオブジェクトを生成
client = discord.Client()


def nyan(message):
    return message.channel.send('にゃーん')

async def invite(message):
    if(message.mentions != None):
        for i in message.mentions:
            guild = message.guild.id
            await guild.create_role(name="role name")
            edit(name="role name" )
            await message.channel.send(f'{message.author.mention} {i}')
            await asyncio.sleep(10)
            await message.channel.send(f'{guild}')

#       for i in message.role_mentions:
#            attribute = ""
#            for j in i.members:
#                attribute += j.User
#                return message.channel.send(attribute)
    else:
        await message.channel.send("Usage: /invite ユーザ名")









# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content.startswith('/neko'):
        await nyan(message)
    #「/invite ユーザー名」と発言したら「うんこ」が返る処理
    if message.content.startswith('/invite'):
        await invite(message)
    
client.run(TOKEN)