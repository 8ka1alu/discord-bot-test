from discord.ext import commands # Bot Commands Frameworkのインポート

import discord

import random

color_code = random.choice((0,0x1abc9c,0x11806a,0x2ecc71,0x1f8b4c,0x3498db,0x206694,0x9b59b6,0x71368a,0xe91e63,0xad1457,0xf1c40f,0xc27c0e,0xe67e22,0x95a5a6,0x607d8b,0x979c9f,0x546e7a,0x7289da,0x99aab5))

# コグとして用いるクラスを定義。
class TestCog(commands.Cog):

    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['s'])
    async def say(self, ctx, what):
        await ctx.send(f'{what}')

    @commands.command(aliases=['q'])
    async def queue(self, ctx, q1, q2):
        embed = discord.Embed(title=q1,description=q2,color=color_code)
        await ctx.send(embed=embed)

    # メインとなるroleコマンド
    @commands.group()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['cr'])
    async def create(self, ctx):
        guild = ctx.guild
        set1 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set2 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set3 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set4 = random.choice(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'))
        set_name = set1 + set2 + set3 + set4
        await guild.create_role(name=set_name)
        await ctx.send(f'作成しました。@' + set_name)
        
    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['ad'])
    async def add(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)
        await ctx.send('付与しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーから指定した役職を剥奪する。
    @role.command(aliases=['rm'])
    async def remove(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)
        await ctx.send('剥奪しました。')

    # roleコマンドのサブコマンド
    # 指定したユーザーに指定した役職を付与する。
    @role.command(aliases=['cr2'])
    async def create2(self, ctx, what):
        guild = ctx.guild
        set_name2 = f"{what}"
        await guild.create_role(name=set_name2)
        await ctx.send(f'作成しました。@' + set_name2)
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == '..i in':
            await message.channel.send('..in')

        if message.author.bot:
            return

        if message.content == 'こんにちは':
            await message.channel.send('こんにちは')

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(TestCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
