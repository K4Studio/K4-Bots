import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.reactions = True
intents.message_content = True  # Enable message content intent

bot = commands.Bot(command_prefix='>', intents=intents)

# Percaktoni listen e roleve qe mund te perdorin komandat >reply dhe >react "ROLE1", "ROLE2" duhet te caktohen si ne discordin tuaj !
allowed_roles = ["ROLE1", "ROLE2"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def reply(ctx, channel_id: int, message_id: int, *, response: str):
    # Check if the user has one of the allowed roles to use the command
    allowed = any(role.name in allowed_roles for role in ctx.author.roles)
    if not allowed: 
        await ctx.send("Ju nuk keni leje per te perdorur kete komande.")
        return

    # Fetch the target channel and message
    target_channel = bot.get_channel(channel_id)
    if not target_channel:
        await ctx.send("Kanali i synuar i nuk gjindet.")
        return

    try:
        target_message = await target_channel.fetch_message(message_id)
    except discord.NotFound:
        await ctx.send("Mesazh i synuar nuk gjindet.")
        return

    # Reply to the target message
    await target_message.reply(response)



# Replace 'YOUR_BOT_TOKEN' with your actual bot token.
bot.run('YOUR_BOT_TOKEN')



# Perdorimi i comandes v v v v v 
#   >reply channel_id message_id Komenti
#   >reply 1165747210751840286 1165748222732533770  Komenti.





credits(K4STUDIOS)























#                       _/|       |\_
#                      /  |       |  \
#                     |    \     /    |
#                     |  \ /     \ /  |
#                     | \  |     |  / | 
#                     | \ _\_/^\_/_ / |      ___  __     ___   ___ 
#                     |   --\\ //--   |     |\  \|\  \  |\  \ |\  \
#                      \_  \     /  _/      \ \  \/  /|_\ \  \\_\  \
#                        \__  |  __/         \ \   ___  \\ \______  \  
#                           \ _ /             \ \  \\ \  \\|_____|\  \ 
#                          _/   \_             \ \__\\ \__\      \ \__\  
#                         / _/|\_ \             \|__| \|__|       \|__|
#                          /  |  \   
#                           / v \
#                            \ /  
 


 
                















