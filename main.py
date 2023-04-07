import discord
import json
import asyncio
import ascii
import os
import requests
import random
import ascii
import sys
from keepalive import keep_alive
intents = discord.Intents(members=True, messages=True, guilds=True, message_content=True, reactions=True)
intents.members = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(status=discord.Status.online, activity=discord.Game(f"p!help | Being a potato"))

@client.event
async def on_member_remove(member):
  leave = discord.Embed(title="Goodbye!", description="""We are sorry to see you leave! We hope that you enjoyed your time here in the Potato Sack. If you ever wish to rejoin, please DM a member of the server for an invite. Thank you!""")
  leave.set_footer(text="Bot developed by kyky#4277.")
  try:
    await member.send(embed=leave)
  except:
    pass
  x = int(guild.member_count)
  leavems = discord.Embed(title=f"{member} has left the server.", description=f"""{member} has left the server. We are sorry to see them go! There are currently {x} members in the server.""")
  leavems.set_footer(text="Bot developed by kyky#4277.")
  with open("serverconfig", "r", encoding='utf-8') as f:
    data = json.load(f)
  
  channel = await guild.fetch_channel(1084322737473994774)
  await channel.send(embed=leavems)

@client.event
async def on_member_join(member):
  guild = client.get_guild(1084322736257630319)
  if member.id == 796465682408800276:
    VIP = discord.utils.find(lambda r: r.name == "VIP", guild.roles)
    await member.add_roles(VIP)
  welcome = discord.Embed(title="Welcome!", description="""Welcome to the Potato Sack Server. I am the local friendly Discord Bot, Potato Choo Choo. For information on how to use me & my commands, please state p!help in #bot-commands. If you need assistance becoming a potato, please contact the owner of the server, Mo0n, or whoever, gave you the invite to this server. We are aware you currently have no roles, therefore, are unable to see channels. Please contact a server moderator or manager for your role. Thank you for joining!""")
  welcome.set_footer(text="Bot developed by kyky#4277.")
  await member.send(embed=welcome)
  x = int(guild.member_count)
  channelem = discord.Embed(title=f"Welcome to the server, {member}!", description=f"""Please welcome {member} into the server! There are currently {x} membaers in the server.""")
  channelem.set_footer(text="Bot developed by kyky#4277.")
  channel = await guild.fetch_channel(1084322737473994774)
  await channel.send(embed=channelem)

@client.event
async def on_guild_join(guild):
  embed = discord.Embed(title="Thank You For Utilizing Potato Choo Choo!", description="Thank you for deciding to utilize the bot Potato Choo Choo. We are thankful for your patronage, and hope that you will enjoy this bot as much as we will. Please forward any bot glitches found to kyky#4277. Do note that we are still in the development phase, so your bug may already be found. **To configure the bot for moderation, type '.configuremods' in any channel within the guild.** Other than that, enjoy!")
  await guild.owner.send(embed=embed)
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  guild = message.author.guild
  guildid = message.author.guild.id
  channels = await guild.fetch_channel(1084499619427405825)
  if message.channel == channels:
    await message.channel.send("<@1087207191997583452>")
  try:
    with open("serverconfig.json", "r", encoding='utf-8') as f:
      data = json.load(f)
    w = data[f"{guildid}"]["LogChannel"]
    logchannel = await guild.fetch_channel(int(w))
    x = data[f"{guildid}"][f"ModRole"]
    modrole = discord.utils.find(lambda r: r.name.lower() == f"{x}", guild.roles)
    y = data[f"{guildid}"][f"ManagerRole"]
    manrole = discord.utils.find(lambda r: r.name.lower() == f"{y}", guild.roles)
    z = data[f"{guildid}"]["MutedRole"]
    mutedrole = discord.utils.find(lambda r: r.name.lower() == f"{z}", guild.roles)
    configured = True
  except Exception as e:
    print(e)
    configured = False
  if message.content.lower() == ".anupdate":
    if message.author.id == 796465682408800276:
      embed = discord.Embed(title="**MESSAGE FROM POTATO HQ: MAJOR BOT UPDATE**",description="""Hi everyone!
      
This is Kyle. I have been working on the bot for several days to encorporate the code to encompass multiple servers at the same time. This means that the bot's permissions settings can be configured on it's own, becoming more versatile.

Additionally, I have implemented a few new updates that I have announced over the past few days:

  (a) The bot has been shifted to a different hosting website. This means that downtimes    have been decreased by approximately 40-45%, depending on your location. This also        includes the fact that the bot should be up nearly 24/7.
  
  (b) The 'p!kick' command has been changed so that only Managers can use this. The         currently configured Manager role is 'RISES THE MOON'. If you have any questions or     
  kick requests, please DM someone with that role to kick a user you feel should be   
  kicked. There have been multiple reasons and individuals that Moon & I have noticed     
  that contribute to this decision, including accidental and purposely-driven Admin 
  Abuse, that results in removal of individuals that should not be kicked.
  
  Do note that in no way am I blaming any certain individual for the actions that I have    stated above, I am merely stating that due to my past experience in bot development &     admin handling, situations where power is entrusted to a large body of individuals have   not gone well. Additionally, I understand that we are all human, and that we will all   
  make rash or irrational actions that we feel we should not have committed. 

  (c) The new "GIF Actions" module is out! The featured commands include p!hug, p!kiss,     p!cuddle, p!smack, p!punch, p!gifkick, and so much more! Discover them for yourself in    #bot-commands.
  
  (d) The bot has been submitted to Top.gg, a popular bot discovery website, for review!    This means that we could soon see the bot featured in multiple different servers. This    is a major step in the bot's development as this means the beta version is now released   to the public.

Thank you for your patience while I take my path down Computer Science, Discord, Bot Engineering, Programming, and so much more. I can't wait to see what the bot has to hold for the future of this server.

*Regards,

Potato Choo Choo Developers,
kyky#4277.*""")
      channel = await guild.fetch_channel(1088277687635804231)
      await channel.send(embed=embed)
      await channel.send("@everyone")
  if message.content.lower() == "p!crime":
    with open("crimecooldown.json", "r", encoding='utf-8') as f:
      data = json.load(f)
    if str(message.author.id) in data.keys():
      asf = int(data[f"{str(message.author.id)}"])
    else:
      asf = 0
    if asf == 0:
      valuetoadd = random.randint(-1500, 1500)
      print(valuetoadd)
      with open("econ.json", "r", encoding='utf-8') as f:
        data = json.load(f)
      if str(message.author.id) in data.keys():
        x = data[f"{str(message.author.id)}"]
        y = x + valuetoadd
        data.update({f"{str(message.author.id)}": y})
        with open("econ.json", "w", encoding='utf-8') as f:
          json.dump(data, f, indent=4, separators=(',',': '))
      else:
        y = valuetoadd
        data.update({f"{str(message.author.id)}": y})
        with open("econ.json", "w", encoding='utf-8') as f:
          json.dump(data, f, indent=4, separators=(',',': '))
      if valuetoadd < 0:
        embed = discord.Embed(title="You got caught!", description=f"You tried committing a crime, but you got caught by your local police. L. You had to pay a bail of {valuetoadd * -1} 🪙.")
        await message.channel.send(embed=embed)
      if valuetoadd == 0:
        embed = discord.Embed(title="You didn't get anything.", description="You tried committing a crime, but you didn't get away with anything. Luckily, you didn't get caught by the police.")
        await message.channel.send(embed=embed)
      if valuetoadd > 0:
        embed = discord.Embed(title="You committed a crime.", description=f"You committed a crime, and didn't get caught by your local police. You earned {valuetoadd} 🪙.")
        await message.channel.send(embed=embed)
      with open("crimecooldown.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        data.update({f"{message.author.id}": 300})
        with open("crimecooldown.json", "w", encoding='utf-8') as f:
          json.dump(data, f, indent=4, separators=(',',': '))
        x = True
        while x == True:
          with open("crimecooldown.json", "r", encoding='utf-8') as uwu:
            uwus = json.load(uwu)
          if uwus[f"{str(message.author.id)}"] != 0:
            frick = uwus[f"{str(message.author.id)}"]
            frick = frick - 1
            uwus[f"{str(message.author.id)}"] = frick
            with open("crimecooldown.json", "w", encoding='utf-8') as asdf:
              json.dump(uwus, asdf, indent=4, separators=(',',': '))
              print("success", x)
            await asyncio.sleep(1)
          else:
            x = False
    else:
      cool = discord.Embed(title="You are on cooldown!", description=f"You recently ran this command. Please try again in {asf} seconds.")
      await message.channel.send(embed=cool)
  if message.content.lower() == ".configuremods":
    if int(guild.owner_id) == int(message.author.id):
      channel = message.channel
      autor = message.author
      with open("serverconfig.json", "r", encoding="utf-8") as z:
        data = json.load(z)
      data.update({f"{guildid}": {"ModRole": "", "ManagerRole": "", "MutedRole": "", "LogChannel": ""}})
      with open("serverconfig.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, separators=(',',': '))
      first = discord.Embed(title="Configure Manager Role", description="Please reply to this message with a role for the Manager role. This role will be able to kick, ban, and unban users. To skip this, type 'Skip'.")
      second = discord.Embed(title="Configure Moderator Role", description="Please repy to this message with a role for the Moderator role. This role will be able to warn and mute users. To skip this, type 'Skip'.")
      third = discord.Embed(title="Configure Muted Role", description="Please reply to this message with a role for the Muted role. To skip this, type 'Skip'.")
      fourth = discord.Embed(title="Configure Logging Channel", description="Please reply to this message with the channel ID for the logging channel. This is where logs of moderation actions will go. To skip this, type 'Skip'.")
      timeout = discord.Embed(title="Timeout Error", description="You went over the limit of 30 seconds to provide a message. This portion has been skipped.")
      done = discord.Embed(title="Moderation Configuration Done!", description="Your server has been set up with the Moderator Role, Manager Role, and Muted Role. Your bot should be fully functional in this server now.")
      x = await message.channel.send(embed=first)
      try:
        msg1 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
        grr = msg1.content
        if grr.lower() == "skip":
          await message.channel.send(embed=second)
          msg2 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
          grr2 = msg2.content
          if grr2.lower() == "skip":
            await message.channel.send(embed=third)
            msg3 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
            grr3 = msg3.content
            if grr3.lower() != "skip":
              ModRole = grr3.lower()
              with open("serverconfig.json", "r", encoding='utf-8') as f:
                data = json.load(f)
              data[f"{guildid}"].update({"MutedRole": f"{ModRole}"})
              with open("serverconfig.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4, separators=(',',': '))
              await message.channel.send(embed=done)
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                await message.channel.send(embed=done)
            if grr3.lower() == "skip":
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
              
          if grr2.lower() != "skip":
            ModRole = grr2.lower()
            with open("serverconfig.json", "r", encoding='utf-8') as f:
              data = json.load(f)
            data[f"{guildid}"].update({"ModRole": f"{ModRole}"})
            with open("serverconfig.json", "w", encoding='utf-8') as f:
              json.dump(data, f, indent=4, separators=(',',': '))
            await message.channel.send(embed=third)
            msg3 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
            grr3 = msg3.content
            if grr3.lower() != "skip":
              ModRole = grr3.lower()
              with open("serverconfig.json", "r", encoding='utf-8') as f:
                data = json.load(f)
              data[f"{guildid}"].update({"MutedRole": f"{ModRole}"})
              with open("serverconfig.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4, separators=(',',': '))
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
            if grr3.lower() == "skip":
              await message.channel.send(embed=done)
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
        if grr.lower() != "skip":
          ModRole = grr.lower()
          with open("serverconfig.json", "r", encoding='utf-8') as f:
            data = json.load(f)
          data[f"{guildid}"].update({"ManagerRole": f"{ModRole}"})
          with open("serverconfig.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, separators=(',',': '))
          await message.channel.send(embed=second)
          msg2 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
          grr2 = msg2.content
          if grr2.lower() == "skip":
            await message.channel.send(embed=third)
            msg3 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
            grr3 = msg3.content
            if grr3.lower() != "skip":
              ModRole = grr3.lower()
              with open("serverconfig.json", "r", encoding='utf-8') as f:
                data = json.load(f)
              data[f"{guildid}"].update({"MutedRole": f"{ModRole}"})
              with open("serverconfig.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4, separators=(',',': '))
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
            if grr3.lower() == "skip":
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
              
          if grr2.lower() != "skip":
            ModRole = grr2.lower()
            with open("serverconfig.json", "r", encoding='utf-8') as f:
              data = json.load(f)
            data[f"{guildid}"].update({"ModRole": f"{ModRole}"})
            with open("serverconfig.json", "w", encoding='utf-8') as f:
              json.dump(data, f, indent=4, separators=(',',': '))
            await message.channel.send(embed=third)
            msg3 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
            grr3 = msg3.content
            if grr3.lower() != "skip":
              ModRole = grr3.lower()
              with open("serverconfig.json", "r", encoding='utf-8') as f:
                data = json.load(f)
              data[f"{guildid}"].update({"MutedRole": f"{ModRole}"})
              with open("serverconfig.json", "w", encoding='utf-8') as f:
                json.dump(data, f, indent=4, separators=(',',': '))
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
            if grr3.lower() == "skip":
              await message.channel.send(embed=fourth)
              msg4 = await client.wait_for('message', timeout=30.0, check=lambda message: message.author == autor)
              grr4 = msg4.content
              if grr4.lower() == "skip":
                await message.channel.send(embed=done)
              if grr4.lower() != "skip":
                ModRole = grr4.lower()
                with open("serverconfig.json", "r", encoding='utf-8') as f:
                  data = json.load(f)
                data[f"{guildid}"].update({"LogChannel": f"{ModRole}"})
                with open("serverconfig.json", "w", encoding='utf-8') as f:
                  json.dump(data, f, indent=4, separators=(',',': '))
                  await message.channel.send(embed=done)
      except asyncio.TimeoutError:
        await message.channel.send(embed=timeout)
        
    else:
      perm = discord.Embed(title="Invalid Permissions", description="You must be the owner of the server to use this command. If this is an error, please contact kyky#4277.")
      await message.channel.send(embed=perm)
  if message.content.lower().startswith(".setmanagerrole"):
    print(guild.owner_id)
    if int(guild.owner_id) == int(message.author.id):
      new = message.content.split(".setmanagerrole ")[1]
      with open("managerrole.json", "r", encoding='utf-8') as f:
        data = json.load(f)
      guildid = str(guild.id)
      if guildid in data.keys():
        x = data[f"{guildid}"]
        modrole = discord.utils.find(lambda r: r.name == f"{x}", guild.roles)
        data.update({f"{guildid}": f"{new}"})
        with open("managerrole.json", "w", encoding='utf-8') as z:
          json.dump(data, z, indent=4, separators=(',',': '))
        embed = discord.Embed(title="There is already a Manager role!", description=f"Your previous Manager role was {x}, but it has been changed to {new}.")
        await message.channel.send(embed=embed)
      else:
        data.update({f"{guildid}": f"{new}"})
        with open("managerrole.json", "w", encoding='utf-8') as z:
          json.dump(data, z, indent=4, separators=(',',': '))
          success = discord.Embed(title="Successfully Set the Manager Role.", description=f"The new Manager role is {new}.")
          await message.channel.send(embed=success)
    else:
      noperm = discord.Embed(title="Invalid Permissions!", description="You must be the owner of the server to run this command.")
      await message.channel.send(embed=noperm)
  if message.content.lower().startswith(".setmodrole"):
    with open("managerrole.json", "r", encoding='utf-8') as f:
      data = json.load(f)
    try:
      man = data[f"{message.author.guild.id}"].lower()
      print(man)
      role = discord.utils.find(lambda r: r.name.lower() == f"{man}", guild.roles)
      if role in message.author.roles:
        new = message.content.split(".setmodrole ")[1]
        with open("modrole.json", "r", encoding='utf-8') as f:
          data = json.load(f)
        guildid = str(guild.id)
        if guildid in data.keys():
          x = data[f"{guildid}"]
          modrole = discord.utils.find(lambda r: r.name == f"{x}", guild.roles)
          data.update({f"{guildid}": f"{new}"})
          with open("modrole.json", "w", encoding='utf-8') as z:
            json.dump(data, z, indent=4, separators=(',',': '))
          embed = discord.Embed(title="There is already a mod role!", description=f"Your previous modrole was {x}, but it has been changed to {new}.")
          await message.channel.send(embed=embed)
        else:
          data.update({f"{guildid}": f"{new}"})
          with open("modrole.json", "w", encoding='utf-8') as z:
            json.dump(data, z, indent=4, separators=(',',': '))
            success = discord.Embed(title="Successfully Set the Moderator Role.", description=f"The new moderator role is {new}.")
            await message.channel.send(embed=embed)
    except Exception as e:
      error = discord.Embed(title="Manager Role Not Configured", description=f"The manager role for this server is not configured. This is the only role that can use this command. If this is an error, please contact kyky#4277. Error: {e}")
      await message.channel.send(embed=error)
  if message.content.lower().startswith("p!gifkick"):
    response = requests.get("https://g.tenor.com/v1/search?q=animekick&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You kicked {user}. Ouch.", description=f"{message.author.mention} kicked {user.mention} and gave them emotional damage. RIP.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower() == "p!taxfraud":
    response = requests.get("https://g.tenor.com/v1/search?q=taxevasion&key=LIVDSRZULELA&limit=50")
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title="You committed tax fraud.", description=f"{message.author.mention} committed tax fraud and ran from the IRS. Congrats on being a criminal.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!dislocate_rib"):
    response = requests.get("https://g.tenor.com/v1/search?q=animejump&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You dislocated {user}'s ribs.", description=f"{message.author.mention} dislocated {user.mention}'s ribs. Damn. Too bad this server doesn't have a doctor.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!kill"):
    response = requests.get("https://g.tenor.com/v1/search?q=animekill&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You killed {user}...", description=f"{message.author.mention} killed {user.mention}. Damn. Personally, I would not take that level of disrespect.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower() == "p!cow":
    response = requests.get("https://g.tenor.com/v1/search?q=cow&key=LIVDSRZULELA&limit=50")
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    await message.channel.send(quote)
  if message.content.lower().startswith("p!run"):
    response = requests.get("https://g.tenor.com/v1/search?q=animerunaway&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You ran away from {user} because they were creeping you out.", description=f"{message.author.mention} ran away from {user.mention}. Damn. Personally, I would not take that level of disrespect.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower() == "p!shrug":
    response = requests.get("https://g.tenor.com/v1/search?q=animeshrug&key=LIVDSRZULELA&limit=50")
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    await message.channel.send(quote)
  if message.content.lower() == "p!cat":
    response = requests.get("https://g.tenor.com/v1/search?q=cat&key=LIVDSRZULELA&limit=50")
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    await message.channel.send(quote)
  if message.content.lower() == "p!dog":
    response = requests.get("https://g.tenor.com/v1/search?q=dog&key=LIVDSRZULELA&limit=50")
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    await message.channel.send(quote)
  if message.content.lower().startswith("p!role"):
    if configured == True:
      if modrole or manrole in message.author.roles:
        user = await guild.fetch_member(int(message.content.split(" ", 2)[1].split("<@")[1].split(">")[0]))
        g = message.content.split(" ", 2)[2].lower()
        roletoadd = discord.utils.find(lambda r: r.name.lower() == f"{g}", guild.roles)
        if roletoadd not in user.roles:
          await user.add_roles(roletoadd)
          sucess = discord.Embed(title="Added Roles", description=f"I have added the {roletoadd} role to {user.mention}'s roles.")
          await message.channel.send(embed=sucess)
        else:
          await user.remove_roles(roletoadd)
          sucess = discord.Embed(title="Removed Roles", description=f"I have removed the {roletoadd} role from {user.mention}'s roles.")
          await message.channel.send(embed=sucess)
      else:
        inv = discord.Embed(title="Invalid Permissions!", description="You do not have the necessary permissions to run this command.")
        await message.channel.send(embed=inv)
    else:
      un = discord.Embed(title="Server Not Configured!", description="This server has not been configured for the moderation module. Please contact the owner to run .configuremods to fix this. If this is an error, please contact kyky#4277. Thank you.")
      await message.channel.send(embed=un)
      
  if message.content.lower() == "p!meme":
    response = requests.get("https://g.tenor.com/v1/search?q=meme-gifs&key=LIVDSRZULELA&limit=50")
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    await message.channel.send(quote)
  if message.content.lower().startswith("p!makeout"):
    response = requests.get("https://g.tenor.com/v1/search?q=animemakeout&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You uhh... made out with {user}?", description=f"{message.author.mention} made out with {user.mention}... Okay...")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!cuddle"):
    response = requests.get("https://g.tenor.com/v1/search?q=animecuddleinbed&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You cuddled with {user}.", description=f"{message.author.mention} cuddled with {user.mention} and nearly got STDs.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!bite"):
    response = requests.get("https://g.tenor.com/v1/search?q=animebite&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You bit {user}...", description=f"{message.author.mention} took a bite out of {user.mention}. Tasty.")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!lick"):
    response = requests.get("https://g.tenor.com/v1/search?q=animelickface&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You gave {user} a lick...", description=f"{message.author.mention} gave {user.mention} a lick? ;)")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!blush"):
    response = requests.get("https://g.tenor.com/v1/search?q=animeblush&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You blushed at {user}.", description=f"{message.author.mention} blushed at {user.mention}. Cute!")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!punch"):
    response = requests.get("https://g.tenor.com/v1/search?q=animepunch&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You gave {user} a nice punch..", description=f"{message.author.mention} gave {user.mention} a punch. Ouch!")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!pat"):
    response = requests.get("https://g.tenor.com/v1/search?q=animepat&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"You gave {user} a pat.", description=f"{message.author.mention} gave {user.mention} a sweet pat. :))")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!kiss"):
    response = requests.get("https://g.tenor.com/v1/search?q=animekiss&key=LIVDSRZULELA&limit=50")
    user = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(user))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"Aww... You kissed {user}!", description=f"{message.author.mention} kissed {user.mention}. How sweet!")
    embed.set_image(url=quote)
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!smack"):
    response = requests.get("https://g.tenor.com/v1/search?q=animesmack&key=LIVDSRZULELA&limit=50")
    user = await guild.fetch_member(int(message.content.split(" ")[1].split("<@")[1].split(">")[0]))
    json_data = json.loads(response.text)
    quote = json_data["results"][random.randint(0, 49)]["media"]
    quote = quote[0]
    quote = quote["gif"]["url"]
    embed = discord.Embed(title=f"Ouch! {message.author} smacked {user}!", description=f"""{message.author.mention} smacked {user.mention}. Yikes.""")
    embed.set_image(url=f"{quote}")
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!hug"):
    tohug = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(tohug)
    response = requests.get("https://some-random-api.ml/animu/hug")
    json_data = json.loads(response.text)
    quote = json_data["link"]
    embed = discord.Embed(title=f"You hugged {user}!", description=f"{message.author.mention} hugged {user.mention}.")
    embed.set_image(url=f"{quote}")
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!wink"):
    towink = message.content.split(" ")[1].split("<@")[1].split(">")[0]
    user = await guild.fetch_member(int(towink))
    response = requests.get("https://some-random-api.ml/animu/wink")
    json_data = json.loads(response.text)
    quote = json_data["link"]
    embed = discord.Embed(title=f"You winked at {user}!", description=f"{message.author.mention} winked at {user.mention}.")
    embed.set_image(url=f"{quote}")
    await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!steal "):
    with open("stealcooldown.json", "r", encoding='utf-8') as a:
      cooldowns = json.load(a)
      print(cooldowns)
    if str(message.author.id) in cooldowns.keys():
      asf = cooldowns[f"{str(message.author.id)}"]
      print(asf)
    else:
      with open("stealcooldown.json", "w", encoding='utf-8') as b:
        cooldowns.update({f"{str(message.author.id)}":0})
        asf = cooldowns[f"{str(message.author.id)}"]
      with open("stealcooldown.json", "w", encoding="utf-8") as c:
        json.dump(cooldowns, c, indent=4, separators=(',',': '))
      print(asf)
    
    if asf == 0:
      user = str(message.content.split("p!steal ")[1].split("<@")[1].split('>')[0])
      with open("econ.json", "r", encoding='utf-8') as g:
        data = json.load(g)
      if user in data.keys():
        bal = int(data[f"{user}"]/3)
        tosteal = random.randint(-bal, bal)
        print(tosteal)
        author = str(message.author.id)
        if author in data.keys():
          x = data[f"{author}"]
          z = x + tosteal
          data[f"{author}"] = z
          y = data[f"{user}"]
          gb = y - tosteal
          data[f"{user}"] = gb
          with open("econ.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, separators=(',',': '))
          if tosteal < 0:
            x = abs(tosteal)
            embed = discord.Embed(title="You tried stealing, but you were caught!", description=f"You tried to steal money from someone, but you were caught. You paid them {x} 🪙.")
            await message.channel.send(embed=embed)
          if tosteal == 0:
            embed = discord.Embed(title="You got nothing.", description="You tried stealing money from that user, but you didn't get anything. Thankfully, you didn't get caught though!")
            await message.channel.send(embed=embed)
          if tosteal > 0:
            embed = discord.Embed(title="You stole from someone!", description=f"You stole money from someone, and you weren't found. You got away with {tosteal} 🪙.")
            await message.channel.send(embed=embed)
          
        else:
          data.update({f"{author}":0})
          x = data[f"{author}"]
          z = x + tosteal
          data[f"{author}"] = z
          y = data[f"{user}"]
          gb = y - tosteal
          data[f"{user}"] = gb
          with open("econ.json", "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4, separators=(',',': '))
      else:
        broke = discord.Embed(title="This user has no money!", description=f"The user that you are attempting to rob has no money.")
        await message.channel.send(embed=broke)
      with open("stealcooldown.json", "r", encoding='utf-8') as d:
        data = json.load(d)
        print(data)
      data.update({f"{str(message.author.id)}":300})
      with open("stealcooldown.json", "w", encoding='utf-8') as e:
        json.dump(data, e, indent=4, separators=(',',': '))
      x = True
      while x == True:
        with open("stealcooldown.json", "r", encoding='utf-8') as uwu:
          uwus = json.load(uwu)
        if uwus[f"{str(message.author.id)}"] != 0:
          frick = uwus[f"{str(message.author.id)}"]
          frick = frick - 1
          uwus[f"{str(message.author.id)}"] = frick
          with open("stealcooldown.json", "w", encoding='utf-8') as asdf:
            json.dump(uwus, asdf, indent=4, separators=(',',': '))
            print("success", x)
          await asyncio.sleep(1)
        else:
          x = False
    else:
      cooldown = discord.Embed(title="You are on cooldown.", description=f"You ran this command recently! Please try again in {asf} seconds.")
      await message.channel.send(embed=cooldown)
  if message.content.lower() == "p!mybal":
    user = str(message.author.id)
    usertag = await guild.fetch_member(int(user))
    with open("econ.json", "r", encoding='utf-8') as f:
      data = json.load(f)
      if f"{user}" in data.keys():
        x = data[f"{user}"]
        print(x)
        embed = discord.Embed(title=f"Displaying {usertag}'s balance", description=f"{usertag}'s balance is currently {x} 🪙.")
        await message.channel.send(embed=embed)
      else:
        x = 0
        print(x)
        embed = discord.Embed(title=f"Displaying {usertag}'s balance", description=f"{usertag}'s balance is currently {x} 🪙.")
        await message.channel.send(embed=embed)
  if message.content.lower().startswith("p!reactions"):
    embed = discord.Embed(title="All Reaction Options", description="""React with the corresponding emoji to recieve the corresponding role. Do note that if you already have the role, that role will be removed upon reacting.
    
React with 🍑 to get the <@&1084634455509053490> role. *Note this will give you access to Simp channels.*

React with 😡 to get the <@&1086118294777495572> role. *Note this will give you access to Venting channels, which has sensitive content.*

React with :weary: to get the <@&1084362982475173938> role.

React with :eggplant: to get the <@&1084717749114241104> to get the NSFW role. *Note that this will give you access to NSFW channels.*

React with :postal_horn: to get the <@&1084713453928861757> role.""")
    f = await message.channel.send(embed=embed)
    await f.add_reaction("🍑")
    await f.add_reaction("😩")
    await f.add_reaction("🍆")
    await f.add_reaction("📯")
    await f.add_reaction("😡")
    @client.event
    async def on_reaction_add(reaction, user):
      if reaction.message == f:
        if reaction.emoji == "😡":
          simps = discord.utils.find(lambda r: r.name == "vent", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Venting role from your roles. You are no longer able to see Venting channels.")
            await user.send(embed=embed)
          else:
            await user.add_roles(simps)
            embed = discord.Embed(title="Role Added", description="I have added the Venting role to your roles. You may now see Vent channels.")
            await user.send(embed=embed)
        if reaction.emoji == "🍑":
          simps = discord.utils.find(lambda r: r.name == "simps", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Simps role from your roles. You are no longer able to see Simping channels.")
            await user.send(embed=embed)
          else:
            await user.add_roles(simps)
            embed = discord.Embed(title="Role Added", description="I have added the Simps role to your roles. You may now see Simp channels.")
            await user.send(embed=embed)
        if reaction.emoji == "🍆":
          simps = discord.utils.find(lambda r: r.name == "NSFW", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the NSFW Access role from your roles. You are no longer able to see NSFW channels.")
            await user.send(embed=embed)
          else:
            await user.add_roles(simps)
            embed = discord.Embed(title="Role Added", description="I have added the NSFW Access role to your roles.")
            await user.send(embed=embed)
        if reaction.emoji == "😩":
          simps = discord.utils.find(lambda r: r.name == "Mommy", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Mommy role from your roles.")
            await user.send(embed=embed)
          else:
            await user.add_roles(simps)
            embed = discord.Embed(title="Role Added", description="I have added the Mommy role to your roles.")
            await user.send(embed=embed)
        if reaction.emoji == "📯":
          simps = discord.utils.find(lambda r: r.name == "horny", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Horny role from your roles.")
            await user.send(embed=embed)
          else:
            await user.add_roles(simps)
            embed = discord.Embed(title="Role Added", description="I have added the Horny role to your roles.")
            await user.send(embed=embed)
        
    @client.event
    async def on_reaction_remove(reaction, user):
      if reaction.message == f:
        if reaction.emoji == "😡":
          simps = discord.utils.find(lambda r: r.name == "vent", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Venting role from your roles. You are no longer able to see vent channels.")
            await user.send(embed=embed)
          else:
            pass
        if reaction.emoji == "😩":
          simps = discord.utils.find(lambda r: r.name == "Mommy", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Mommy role from your roles.")
            await user.send(embed=embed)
          else:
            pass
        if reaction.emoji == "📯":
          simps = discord.utils.find(lambda r: r.name == "horny", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Horny role from your roles.")
            await user.send(embed=embed)
          else:
            pass
        if reaction.emoji == "🍆":
          simps = discord.utils.find(lambda r: r.name == "NSFW", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the NSFW Acess role from your roles. You will no longer be able to see NSFW channels.")
            await user.send(embed=embed)
          else:
            pass
        if reaction.emoji == "🍑":
          simps = discord.utils.find(lambda r: r.name == "simps", guild.roles)
          if simps in user.roles:
            await user.remove_roles(simps)
            embed = discord.Embed(title="Role Removed", description="I have removed the Simp role from your roles. You will no longer be able to see Simp channels.")
            await user.send(embed=embed)
          else:
            pass
    
    reationsembed = discord.Embed(title="Displaying All Gender Reactions", description="""React with the corresponding emoji to recieve the necessary roles. If you already have the roles, reacting will delete the role from your roles.
    
React with :male_sign: if your pronouns are <@&1085786657032253520>.

React with :female_sign: if your pronouns are <@&1085786688728612915>.

React with :transgender_symbol: if your pronouns are <@&1085786744672231434>.

React with :dog: if your pronouns are <@&1086704249909542952>.

React with :helicopter: if your gender is <@&1086703713281908850>.""")
    ms = await message.channel.send(embed=reationsembed)
    await ms.add_reaction("♂️")
    await ms.add_reaction("♀️")
    await ms.add_reaction("⚧")
    await ms.add_reaction("🐶")
    await ms.add_reaction("🚁")
    @client.event
    async def on_reaction_remove(reaction, user):
      if reaction.message == ms:
        if reaction.emoji == "🐶":
          him = discord.utils.find(lambda r: r.name == "It/It's", guild.roles)
          if him in user.roles:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the It/It's role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "♂️":
          him = discord.utils.find(lambda r: r.name == "He/Him", guild.roles)
          if him in user.roles:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the He/Him role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "♀️":
          him = discord.utils.find(lambda r: r.name == "She/Her", guild.roles)
          if him in user.roles:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the She/Her role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "⚧":
          him = discord.utils.find(lambda r: r.name == "They/Them", guild.roles)
          if him in user.roles:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the They/Them role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "🤷‍♂️":
          him = discord.utils.find(lambda r: r.name == "Other Gender (Ask)", guild.roles)
          if him in user.roles:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the Other Gender (Ask) role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "🚁":
          him = discord.utils.find(lambda r: r.name == "Helicopter Gender", guild.roles)
          if him in user.roles:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the Helicopter role from your roles.")
            await user.send(embed=success)
          else:
            pass
    @client.event
    async def on_reaction_add(reaction, user):
      if reaction.message == ms:
        if reaction.emoji == "🐶":
          him = discord.utils.find(lambda r: r.name == "It/It's", guild.roles)
          if him not in user.roles:
            await user.add_roles(him)
            success = discord.Embed(title="Added Roles", description="I have added the It/It's role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the It/It's role from your roles.")
            await user.send(embed=success)
        if reaction.emoji == "♂️":
          him = discord.utils.find(lambda r: r.name == "He/Him", guild.roles)
          if him not in user.roles:
            await user.add_roles(him)
            success = discord.Embed(title="Added Roles", description="I have added the He/Him role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the He/Him role from your roles.")
            await user.send(embed=success)
        if reaction.emoji == "⚧":
          him = discord.utils.find(lambda r: r.name == "They/Them", guild.roles)
          if him not in user.roles:
            await user.add_roles(him)
            success = discord.Embed(title="Added Roles", description="I have added the They/Them role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the They/Them role from your roles.")
            await user.send(embed=success)
        if reaction.emoji == "🚁":
          him = discord.utils.find(lambda r: r.name == "Helicopter Gender", guild.roles)
          if him not in user.roles:
            await user.add_roles(him)
            success = discord.Embed(title="Added Roles", description="I have added the Helicopter Gender role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the Helicopter Gender role from your roles.")
            await user.send(embed=success)
        if reaction.emoji == "♀️":
          him = discord.utils.find(lambda r: r.name == "She/Her", guild.roles)
          if him not in user.roles:
            await user.add_roles(him)
            success = discord.Embed(title="Added Roles", description="I have added the She/Her role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(him)
            success = discord.Embed(title="Removed Roles", description="I have removed the She/Her role from your roles.")
            await user.send(embed=success)
    reactions = discord.Embed(title="Displaying all Ping Reactions", description=f"""React with the corresponding emoji to recieve the corresponding roles. Do note if you already have the role, reacting will cause the role to be removed.

React with :video_game: if you wish to recieve the <@&1087207150000017449>, to be pinged for Moon's events.

React with :newspaper: to recieve the <@&1087125627137699931> ping, for Potato Task of the Day.

React with :robot: to recieve the <@&1087207191997583452>, to be pinged when the bot recieves an update or input is required.""")
    d = await message.channel.send(embed=reactions)
    await d.add_reaction("🎮")
    await d.add_reaction("📰")
    await d.add_reaction("🤖")
    @client.event
    async def on_reaction_remove(reaction, user):
      if reaction.message == d:
        if reaction.emoji == "🎮":
          game = discord.utils.find(lambda r: r.name == "Events Ping", guild.roles)
          if game in user.roles:
            await user.remove_roles(game)
            success = discord.Embed(title="Role Removed", description="I have removed the Events Ping role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "📰":
          game = discord.utils.find(lambda r: r.name == "Task Ping", guild.roles)
          if game in user.roles:
            await user.remove_roles(game)
            success = discord.Embed(title="Role Removed", description="I have removed the Task Ping role from your roles.")
            await user.send(embed=success)
          else:
            pass
        if reaction.emoji == "🤖":
          game = discord.utils.find(lambda r: r.name == "Bot Development Ping", guild.roles)
          if game in user.roles:
            await user.remove_roles(game)
            success = discord.Embed(title="Role Removed", description="I have removed the Bot Development Ping role from your roles.")
            await user.send(embed=success)
          else:
            pass
    @client.event
    async def on_reaction_add(reaction, user):
      if reaction.message == d:
        if reaction.emoji == "🎮":
          game = discord.utils.find(lambda r: r.name == "Events Ping", guild.roles)
          if game not in user.roles:
            await user.add_roles(game)
            success = discord.Embed(title="Role Added", description="I have added the Events Ping role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(game)
            success = discord.Embed(title="Removed Role", description="I have removed the Events Ping from your roles.")
        if reaction.emoji == "📰":
          game = discord.utils.find(lambda r: r.name == "Task Ping", guild.roles)
          if game not in user.roles:
            await user.add_roles(game)
            success = discord.Embed(title="Role Added", description="I have added the Task Ping role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(game)
            success = discord.Embed(title="Removed Role", description="I have removed the Task Ping from your roles.")
        if reaction.emoji == "🤖":
          print("start")
          game = discord.utils.find(lambda r: r.name == "Development Ping", guild.roles)
          if game not in user.roles:
            print("has")
            await user.add_roles(game)
            success = discord.Embed(title="Role Added", description="I have added the Bot Development Ping role to your roles.")
            await user.send(embed=success)
          else:
            await user.remove_roles(game)
            success = discord.Embed(title="Removed Role", description="I have removed the Bot Development Ping from your roles.")
  if message.content.lower().startswith("p!suggest "):
      print(message.content)
      arguments = message.content.split(" ", 1)
      print(len(arguments))
      if len(arguments) == 2:
        guild = message.author.guild
        channeled = await guild.fetch_channel(1087238025853026356)
        suggestion = arguments[1]
        sug = discord.Embed(title="Incoming suggestion!", description=f"""Username: {message.author.mention}
Suggestion: {suggestion}""")
        f = await channeled.send(embed=sug)
        await f.add_reaction("✅")
        await f.add_reaction("❌")
  if message.content.lower() == "ping":
    await message.channel.send("Pong!")
  if message.content.lower().startswith("p!clearwarnings "):
    potatorole = discord.utils.find(lambda r: r.name == "Potato", guild.roles)
    moon = discord.utils.find(lambda r: r.name == "RISES THE MOON", guild.roles)
    fish = discord.utils.find(lambda r: r.name == "Fishlami", guild.roles)
    if potatorole or moon or fish in message.author.roles:
      args = message.content.split(" ", 2)
      print(len(args))
      user = args[1].split("<@")[1]
      user = user.split(">")[0]
      if len(args) == 2:
        with open("warnings.json", "r", encoding="utf-8") as f:
          data = json.loads(f.read())
        for x in data.keys():
          if x == user:
            data[f"{x}"] = []
            print(data)
            with open("warnings.json", "w", encoding="utf-8") as x:
              json.dump(data, x, indent=4, separators=(',',': '))
            clear = discord.Embed(title="Cleared Warnings", description=f"I have cleared all warnings for {args[1]}.")
            await message.channel.send(embed=clear)
            logemb = discord.Embed(title="Possible Admin Abuse", description=f"""{message.author.mention} has cleared all warnings for {args[1]} for no given reason. Potatoes, please review for Admin Abuse as soon as possible.""")
            await logchannel.send(embed=logemb)
            await logchannel.send("<@&1084328650272428102>")
      if len(args) == 3:
        reason = args[2]
        with open("warnings.json", "r", encoding="utf-8") as f:
          data = json.loads(f.read())
        for x in data.keys():
          if x == user:
            data[f"{x}"] = []
            print(data)
            with open("warnings.json", "w", encoding="utf-8") as x:
              json.dump(data, x, indent=4, separators=(',',': '))
            clear = discord.Embed(title="Cleared Warnings", description=f"I have cleared all warnings for {args[1]} for the reason: {reason}.")
            await message.channel.send(embed=clear)
            logemb = discord.Embed(title="Cleared Warnings", description=f"""{message.author.mention} has cleared all warnings for {args[1]} for the reason: {reason}""")
            await logchannel.send(embed=logemb)     
 
    
  if message.content.lower().startswith("p!mute "):
    if configured == True:
      if manrole or modrole in message.author.roles:
        args = message.content.split(" ", 3)
        print(len(args))
        if len(args) == 4:
          time = str(args[2])
          reason = args[3]
          userp = args[1].split("<@")
          user = userp[1].split(">")[0]
          userid = await guild.fetch_member(user)
          if mutedrole not in userid.roles:
            await userid.add_roles(mutedrole)
            try:
              await userid.remove_roles(potato)
            except:
              pass
            success = discord.Embed(title="Muted User", description=f"{userid} has been muted for the reason: {reason}.")
            await message.channel.send(embed=success)
            logembed = discord.Embed(title="Member Muted", description=f"{userid.mention} has been muted by {message.author.mention} for the reason: {reason}.")
            await logchannel.send(embed=logembed)
            days = time.split("d")
            print(days)
            try:
              daysx = int(days[0]) * 86400
              print(daysx)
            except:
              days.insert(0, '')
              daysx = 0
            hours = days[1].split("h")
            try:
              hoursx = int(hours[0]) * 3600
              print(hoursx)
            except:
              hours.insert(0, '')
              hoursx = 0
            minutes = hours[1].split("m")
            try:  
              minutesx = int(minutes[0]) * 60
              print(minutesx)
            except:
              minutes.insert(0, '')
              minutesx = 0
            secondsf = minutes[1].split("s")
            try:
              seconds = int(secondsf[0])
              print(secondsf[0])
            except:
              secondsf.insert(0, '')
              seconds = 0
            waittime = daysx + hoursx + minutesx + seconds
            print(waittime)
            await asyncio.sleep(waittime)
            await userid.remove_roles(mutedrole)
            await userid.add_roles(potato)
            unmuted = discord.Embed(title="Automatic Unmute", description=f"{userid} has been unmuted for the reason: Automatic unmute.")
            await message.channel.send(embed=unmuted)
            await logchannel.send(embed=unmuted)

          else:
            error = discord.Embed(title="Error", description=f"{userid} is already muted.")
            await message.channel.send(embed=error)
        if len(args) == 3:
          time = str(args[2])
          userp = args[1].split("<@")
          user = userp[1].split(">")[0]
          userid = await guild.fetch_member(user)
          mutedrole = discord.utils.find(lambda r: r.name == "Muted", guild.roles)
          if mutedrole not in userid.roles:
            await userid.add_roles(mutedrole)
            await userid.remove_roles(potato)
            success = discord.Embed(title="Muted User", description=f"{userid} has been muted for no reason given.")
            await message.channel.send(embed=success)
            emergencylog = discord.Embed(title=f"Possible Admin Abuse", description=f"""{message.author.mention} has muted {userid} for no reason given.
Potatoes, please review this log for possible admin abuse as soon as possible.""")
            await logchannel.send(embed=emergencylog)
            await logchannel.send("<@&1084328650272428102>")
        
            days = time.split("d")
            print(days)
            try:
              daysx = int(days[0]) * 86400
              print(daysx)
            except:
              days.insert(0, '')
              daysx = 0
            hours = days[1].split("h")
            try:
              hoursx = int(hours[0]) * 3600
              print(hoursx)
            except:
              hours.insert(0, '')
              hoursx = 0
            minutes = hours[1].split("m")
            try:  
              minutesx = int(minutes[0]) * 60
              print(minutesx)
            except:
              minutes.insert(0, '')
              minutesx = 0
            secondsf = minutes[1].split("s")
            try:
              seconds = int(secondsf[0])
              print(secondsf[0])
            except:
              secondsf.insert(0, '')
              seconds = 0
            waittime = daysx + hoursx + minutesx + seconds
            print(waittime)
            await asyncio.sleep(waittime)
            await userid.remove_roles(mutedrole)
            await userid.add_roles(potato)
            unmuted = discord.Embed(title="Automatic Unmute", description=f"{userid} has been unmuted for the reason: Automatic unmute.")
            await message.channel.send(embed=unmuted)
            await logchannel.send(embed=unmuted)

          else:
            error = discord.Embed(title="Error", description=f"{userid} is already muted.")
            await message.channel.send(embed=error)
    else:
      uncon = discord.Embed(title="Server Moderation Not Configured", description="This server does not have moderation configured. To fix this, please contact the server owner to run '.configuremods' in a channel. If this is an error, please DM kyky#4277. Thank you.")
      await message.channel.send(embed=uncon)
  if message.content.lower().startswith("p!unmute "):
    if configured == True:
      if modrole or manrole in message.author.roles:
        args = message.content.split(" ", 2)
        user1 = args[1].split("<@")
        user = user1[1].split(">")
        user = user[0]
        userid = await guild.fetch_member(user)
        if len(args) == 3:
          reason = args[2]
          if mutedrole in userid.roles:
            await userid.remove_roles(mutedrole)
            try:
              await userid.add_roles(potato)
            except:
              pass
            embed = discord.Embed(title="User unmuted", description=f"{message.author.mention} has unmuted {userid.mention} for the reason: {reason}.")
            await message.channel.send(embed=embed)
            logchannel = await client.fetch_channel(1084329933339365388)
            logembed = discord.Embed(title=f"Unmuted User", description=f"{message.author.mention} unmuted {userid.mention} for the reason: {reason}")
            await logchannel.send(embed=logembed)
          else:
            error = discord.Embed(title="Error", description=f"""Error unmuting member. Please check if they are muted.
Command Format: p!unmute [Ping user] [Reason]""")
            await message.channel.send(embed=error)
        if len(args) == 2:
          mutedrole = discord.utils.find(lambda r: r.name == "Muted", guild.roles)
          if mutedrole in userid.roles:
            await userid.remove_roles(mutedrole)
            try:
              await userid.add_roles(potato)
            except:
              pass
            embed = discord.Embed(title="User unmuted", description=f"{message.author.mention} has unmuted {userid.mention} for no given reason.")
            await message.channel.send(embed=embed)
            logchannel = await client.fetch_channel(1084329933339365388)
            emergencylog = discord.Embed(title=f"Possible Admin Abuse", description=f"""{message.author.mention} has unmuted {userid.mention} for no reason given.
Potatoes, please review this log for possible admin abuse as soon as possible.""")
            await logchannel.send(embed=emergencylog)
            await logchannel.send("<@&1084328650272428102>")
          else:
            error = discord.Embed(title="Error", description=f"""Error unmuting member. Please check if they are muted.
Command Format: p!unmute [Ping user] [Reason]""")
            await message.channel.send(embed=error)
    else:
      uncon = discord.Embed(title="Server Moderation Not Configured", description="This server does not have moderation configured. To fix this, please contact the server owner to run '.configuremods' in a channel. If this is an error, please DM kyky#4277. Thank you.")
      await message.channel.send(embed=uncon)
  if message.content.lower().startswith("p!growpotato "):
    moon = discord.utils.find(lambda r: r.name == "RISES THE MOON", guild.roles)
    lami = discord.utils.find (lambda r: r.name == "FISHLAMI", guild.roles)
    ky = discord.utils.find(lambda r: r.name == "VIP", guild.roles)
    if moon or lami or ky in message.author.roles:
      args = message.content.split(" ")
      user1 = args[1].split("<@")
      user = user1[1].split(">")
      user = user[0]
      userid = await guild.fetch_member(user)
      potatorole = discord.utils.find(lambda r: r.name == "Potato", guild.roles)
      if potatorole not in userid.roles:
        await userid.add_roles(potatorole)
        await message.channel.send(f"{userid.mention} is now a potato.")
      if potatorole in userid.roles:
        await userid.remove_roles(potatorole)
        await message.channel.send(f"{userid.mention} has been un-potatotized.")
    
  if message.content.lower().startswith("p!help"):
    embed = discord.Embed(title="Displaying all Commands (Page 1 of 2)", description="""Available Commands:

**p!help:** Gives a list of all commands.

**.configuremods:** Server owner only. Configures the moderation module, setting up the Moderator role, Manager role, and Muted role.

**p!reactions**: Gives a list of reactions roles that may be utilized to recieve gender assignments, channel access, and pings.

**p!mybal**: Allows you to view your balance in our economy based system.

**p!work:** Allows you to work in the economy based system.

**p!steal:** Steals money from the specified user in our economy based system.

**p!crime:** Commits a crime in our economy based system.

**p!role [User ping]:** *Moderator/Manager role only.* Allows you to add or remove a role from a user depending on if they already have it or not.

**p!warn [User ping] [Reason]:** *Moderator/Manager role only.* Warns a user.

**p!mute [User ping] [Duration] [Reason]:** *Moderator/Manager role only*. Mutes a user for a duration. Example Durations include s(seconds), m(minutes), h(hours), and/or d(days).

**p!unmute [User ping] [Reason]:** *Moderator/Manager only.* Unmutes a user if they are muted.

**p!delwarn [User ping] [Moderation ID] [Reason]:** *Moderator/Manager only.* Deletes a warning for a user.

**p!clearwarnings [User ping] [Reason]**: *Moderator/Manager only.* Clears all warnings for a given user.

**p!kick [User] [Reason]:** *Manager only.* Kicks a user from the server.

**p!ban [User ping] [Reason]:** *Manager only.* Bans a user from the server.

**p!unban [User ID] [Reason]:** *Manager only.* Unbans a user from the server.

React with ⏩ to see the next page.""")
    embed.set_footer(text="Bot made by kyky#4277.")
    x = await message.channel.send(embed=embed)
    await x.add_reaction("⏪")
    await x.add_reaction("⏩")
    @client.event
    async def on_reaction_add(reaction, user):
      if reaction.message == x:
        if reaction.emoji == "⏪":
          await x.edit(embed=embed)
          await x.remove_reaction("⏪", user)
        if reaction.emoji == "⏩":
          newem = discord.Embed(title="Displaying all Commands (Page 2 of 2)", description=f"""**p!smack [User ping]:** Smacks the specified user.

**p!hug [User ping]:** Hugs the specified user.

**p!punch [User ping]:** Punches the specified user.

**p!kiss [User ping]:** Kisses the specified user.

**p!cuddle [User ping]:** Cuddles with the specified user.

**p!meme:** Generates a random meme.

**p!makeout [User ping]:** Makes out with the specified user.

**p!bite [User ping]:** Bites the specified user.

**p!lick [User ping]:** Licks the specified user.

**p!blush [User ping]:** Blushes at the specified user.

**p!pat [User ping]:** Pats the specified user.

**p!cat:** Sends a GIF of a cat.

**p!dog:** Sends a GIF of a dog.

**p!cow:** Sends a GIF of a cow.

**p!run [User ping]:** Runs away from the specified user.

**p!shrug:** Sends a GIF of someone shrugging.

React with ⏪ to display the previous page.""")
          grr = await x.edit(embed=newem)
          await x.remove_reaction("⏩", user)
  if message.content.lower() == "p!work":
    args = str(message.author.id)
    user1 = args.split("<@")
    user = args.split(">")
    id = user[0]
    with open("workcooldown.json", "r+", encoding='utf-8') as a:
      cooldowns = json.load(a)
      print(cooldowns)
    if str(id) in cooldowns.keys():
      asf = cooldowns[f"{id}"]
      print(asf)
    else:
      with open("workcooldown.json", "w", encoding='utf-8') as b:
        cooldowns.update({f"{id}":0})
        asf = cooldowns[f"{id}"]
      with open("workcooldown.json", "w", encoding="utf-8") as c:
        json.dump(cooldowns, c, indent=4, separators=(',',': '))
      print(asf)
    
    if asf == 0:
      with open("econ.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        print(data)
      val = random.randint(100, 500)
      print(val)
      if id in data.keys():
        dataval = data[f"{id}"]
        print(dataval)
        dataval += val
        dataval = dataval
        print(dataval)
        data[f"{id}"] = dataval
        print(data)
        with open("econ.json", "w", encoding='utf-8') as x:
          json.dump(data, x, indent=4, separators=(',',': '))
      else:
        dataval = data.update({id:0})
        dataval = data[f"{id}"]
        dataval += val
        print(dataval)
        data[f"{id}"] = dataval
        print(data)
        with open("econ.json", "w", encoding='utf-8') as x:
          json.dump(data, x, indent=4, separators=(',',': '))
      embedtosend = discord.Embed(title="Went to work", description=f"You went to work and earned {val}. Current balance: {dataval}")
      await message.channel.send(embed=embedtosend)
      with open("workcooldown.json", "r", encoding='utf-8') as d:
        data = json.load(d)
        print(data)
      data.update({f"{id}":30})
      with open("workcooldown.json", "w", encoding='utf-8') as e:
        json.dump(data, e, indent=4, separators=(',',': '))
      x = True
      while x == True:
        with open("workcooldown.json", "r", encoding='utf-8') as uwu:
          uwus = json.load(uwu)
        if uwus[f"{id}"] != 0:
          frick = uwus[f"{id}"]
          frick = frick - 1
          uwus[f"{id}"] = frick
          with open("workcooldown.json", "w", encoding='utf-8') as asdf:
            json.dump(uwus, asdf, indent=4, separators=(',',': '))
            print("success", x)
          await asyncio.sleep(1)
        else:
          x = False
    else:
      cem = discord.Embed(title="You are on cooldown!", description=f"You are on cooldown. Please re-attempt this command in {asf} seconds.")
      await message.channel.send(embed=cem)
  if message.content.lower().startswith("p!unban"):
    if configured == True:
      if manrole in message.author.roles:
        args= message.content.split(" ", 3)
        if len(args) == 2:
          print(args)
          user = await client.fetch_user(args[1])
          try:
            await guild.unban(user)
            success = discord.Embed(title="Successfully Unbanned User", description=f"{message.author.mention} has unbanned the user {user} for no given reason.")
            await message.channel.send(embed=success)
            log = discord.Embed(title="Unbanned User", description=f"{message.author.mention} has unbanned the user {user} without a given reason. Potatoes, please review for legitamacy confirmation. Thank you.")
            await logchannel.send(embed=log)
            await logchannel.send("<@&1084328650272428102>")
          except Exception as e:
            await message.channel.send(f"Error unbanning user. Error code: {e}")
        if len(args) == 3:
          reason = args[2]
          user = await client.fetch_user(args[1])
          try:
            await guild.unban(user)
            success = discord.Embed(title="Successfully Unbanned User", description=f"{message.author.mention} has unbanned the user {user} for the given reason: {reason}.")
            await message.channel.send(embed=success)
            log = discord.Embed(title="Unbanned User", description=f"{message.author.mention} has unbanned the user {user} for the given reason: {reason}.")
            await logchannel.send(embed=log)
          except Exception as e:
            await message.channel.send(f"Error unbanning user. Error code: {e}")
    else:
      uncon = discord.Embed(title="Server Moderation Not Configured", description="This server does not have moderation configured. To fix this, please contact the server owner to run '.configuremods' in a channel. If this is an error, please DM kyky#4277. Thank you.")
      await message.channel.send(embed=uncon)
  if message.content.lower().startswith("p!delwarn"):
    if configured == True:
      if modrole or manrole in message.author.roles:
        args = message.content.split(" ", 3)
        try:
          args.remove(" ")
        except:
          pass
        print(len(args))
        print(args)
        if len(args) == 4:
          print(args)
          id = args[2]
          reason = args[3]
          print(type(id))
          print(id)
          user_id = args[1].split("<@")
          user_id = user_id[1].split(">")
          try:
            user_id.remove("")
          except:
            pass
          user_id = user_id[0]
          user_id = str(user_id)
          username = await client.fetch_user(user_id)
          print(user_id)
          with open('warnings.json', 'r+', encoding='utf-8') as f: #open file
            data = json.load(f) #read it and convert to python
            ind = data[f"{user_id}"]
            print(ind)
            print(type(ind))
            for x in data.keys():
              if x == user_id: #look for the correct user id
                print("succcess")
                for z in ind:
                  dict = z["id"]
                  dict = int(dict)
                  print(dict)
                  print(type(z))
                  print(args[2])
                  print(type(dict))
                  print(type(args[2]))
                  goofy = int(args[2])
                  if dict == goofy:
                    xyz = ind.index(z)
                    print(z)
                    ind.pop(xyz)
                    with open('warnings.json', 'r', encoding='utf-8') as f:
                      data = json.load(f)
                    del data[f"{user_id}"][xyz]
                    print(data)
                    with open('warnings.json', 'w', encoding='utf-8') as f:
                      json.dump(data, f, indent=4, separators=(',',': '))
                    warningembed = discord.Embed(title=f"Removed warning for {username}", description=f"Removed the warning with the moderation ID {id} for {username} for the reason: {reason}.")
                    logembed = discord.Embed(title=f"Warning Removed for {username}", description=f"{message.author.mention} removed the warning with a moderation ID {id} for {username}. Reason: {reason}")
                    await logchannel.send(embed=logembed)
                    await message.channel.send(embed=warningembed)
                    break
        if len(args) == 3:
          print(args)
          id = args[2]
          print(type(id))
          print(id)
          user_id = args[1].split("<@")
          user_id = user_id[1].split(">")
          try:
            user_id.remove("")
          except:
            pass
          user_id = user_id[0]
          user_id = str(user_id)
          username = await client.fetch_user(user_id)
          print(user_id)
          with open('warnings.json', 'r+', encoding='utf-8') as f: #open file
            data = json.load(f) #read it and convert to python
            ind = data[f"{user_id}"]
            print(ind)
            print(type(ind))
            for x in data.keys():
              if x == user_id: #look for the correct user id
                print("succcess")
                for z in ind:
                  dict = z["id"]
                  dict = int(dict)
                  print(dict)
                  print(type(z))
                  print(args[2])
                  print(type(dict))
                  print(type(args[2]))
                  goofy = int(args[2])
                  if dict == goofy:
                    xyz = ind.index(z)
                    print(z)
                    ind.pop(xyz)
                    with open('warnings.json', 'r', encoding='utf-8') as f:
                      data = json.load(f)
                    del data[f"{user_id}"][xyz]
                    print(data)
                    with open('warnings.json', 'w', encoding='utf-8') as f:
                      json.dump(data, f, indent=4, separators=(',',': '))
                    warningembed = discord.Embed(title=f"Removed warning for {username}", description=f"Removed the warning with the moderation ID {id} for {username} for no reason.")
                    logchannel = await client.fetch_channel(1084329933339365388)
                    emergencylog = discord.Embed(title=f"Possible Admin Abuse", description=f"""{message.author.mention} has removed a warning from {username} for no reason given.
Potatoes, please review this log for possible admin abuse as soon as possible.""")
                    await logchannel.send(embed=emergencylog)
                    await logchannel.send("<@&1084328650272428102>")
                    await message.channel.send(embed=warningembed)
                    break
                  
    else:
      uncon = discord.Embed(title="Server Moderation Not Configured", description="This server does not have moderation configured. To fix this, please contact the server owner to run '.configuremods' in a channel. If this is an error, please DM kyky#4277. Thank you.")
      await message.channel.send(embed=uncon)
  if message.content.lower().startswith("p!warn "):
    if configured == True:
      if modrole or manrole in message.author.roles:
        moderator = message.author.mention
        moderatorjson = f"<@{moderator}>"
        id = random.randint(1, 1000000)
        argspr = message.content.split("p!warn ", 2)
        args1 = argspr[1]
        argspre = args1.split("<@")
        argsal = argspre[1]
        argsne = argsal.split(">")
        try:
          argsne.remove("")
        except:
          pass
        print(argsne)
        print(len(argsne))
        print(argsne)

        if len(argsne) == 2:
          reason = str(argsne[1])
          member = argsne[0]
          print(member)
          member_id = member  # Replace with actual member ID
          data = []

# Read JSON file
          with open('warnings.json') as fp:
            data = json.load(fp)
          print(data)
          print(type(data))
          appender = {"id": id, "mod": moderator, "reason": reason}
 
          if member_id in data.keys():
            data[f"{member_id}"].append({"id": id, "mod": moderator, "reason": reason})
            print(data)
 
            with open('warnings.json', 'w') as json_file:
              json.dump(data, json_file, indent=4, separators=(',',': '))
          else:
            data[f"{member_id}"] = []
            data[f"{member_id}"].append({"id": id, "mod": moderator, "reason": reason})
            print(data)
            with open('warnings.json', 'w') as json_file:
              json.dump(data, json_file, indent=4, separators=(',',': '))
          warnem = discord.Embed(title="Member warned", description=f"<@{member}> has been warned for the reason: {reason} by {message.author.mention}.")
          warnem.set_footer(text=f"Moderation ID: {id}")
          await message.channel.send(embed=warnem)
          await logchannel.send(embed=warnem)
        if len(argsne) == 1:
          member = argsne[0]
          print(member)
          member_id = member  # Replace with actual member ID
          data = []
          with open('warnings.json') as fp:
            data = json.load(fp)
          print(data)
          print(type(data))
 
          if member_id in data.keys():
            data[f"{member_id}"].append({"id": id, "mod": moderator, "reason": "No reason given."})
            print(data)
 
            with open('warnings.json', 'w') as json_file:
              json.dump(data, json_file, indent=4, separators=(',',': '))
          else:
            data[f"{member_id}"] = []
            data[f"{member_id}"].append({"id": id, "mod": moderator, "reason": reason})
            print(data)
 
            with open('warnings.json', 'w') as json_file:
              json.dump(data, json_file, indent=4, separators=(',',': '))
          warnem = discord.Embed(title="Member warned", description=f"<@{member}> has been warned for no reason by {message.author.mention}.")
          warnem.set_footer(text=f"Moderation ID: {id}")
          await message.channel.send(embed=warnem)
          emergenc = discord.Embed(title="Possible Admin Abuse", description=f"""<@{member}> has been warned for no given reason by {message.author.mention}.
Overseers, please review for possible admin abuse as soon as possible.""")
          await logchannel.send(embed=emergenc)
          await logchannel.send("<@&1084328650272428102>")
    else:
      uncon = discord.Embed(title="Server Moderation Not Configured", description="This server does not have moderation configured. To fix this, please contact the server owner to run '.configuremods' in a channel. If this is an error, please DM kyky#4277. Thank you.")
      await message.channel.send(embed=uncon)
  if message.content.lower().startswith("p!warnings "):
    if configured == True:
      if modrole or manrole in message.author.roles:
        args = message.content.split("p!warnings ")
        userping = args[1]
        user1 = userping.split("<@")
        g = user1[1]
        userlst = g.split(">")
        user = userlst[0]
        print(user)
        try:
          with open("warnings.json", "r") as f:
            data = json.load(f)

          user_data = data[str(user)]
          user_data = str(user_data)
          user_data = str(user_data)
          user_data = user_data.replace("},", "\n")
          user_data = user_data.replace("'", "")
          user_data = user_data.replace("{", "")
          user_data = user_data.replace("}", "")
          user_data = user_data.replace("[", "")
          user_data = user_data.replace("]", "")
          user_data = user_data.replace("id", "ID")
          user_data = user_data.replace("mod:", "Moderator:")
          user_data = user_data.replace("reason", "Reason")
          userping = await client.fetch_user(user)
          warningembed = discord.Embed(title=f"Displaying all warnings for {userping}", description=f"{user_data}")
          await message.channel.send(embed=warningembed)
        except KeyError:
          await message.channel.send("User has no warnings.")
      else:
        perm = discord.Embed(title="Invalid Permissions!", description=f"You do not have the required role to do this. The current Moderator role is {modrole}, and the current Manager role is {manrole}. If this is a mistake, please contact the owner of the server to reconfigure the moderation module.")
        await message.channel.send(embed=perm)
    else:
      unconf = discord.Embed(title="Moderation Module Not Configured!", description="The moderation module has not been set up by the server's owner yet. If  this is an error, please contact the server's owner to run '.configuremods'. If that does not work, please DM kyky#4277 instantly. Thank you.")
      await message.channel.send(embed=unconf)
  if message.content.lower().startswith("p!wakeup"):
    role = discord.utils.find(lambda r: r.name == "Potato", guild.roles)
    if role in message.author.roles:
      argus = message.content.split(" ")
      ax = argus[1]
      idsas = ax.split("<@")
      c = idsas[1]
      targetid = c.split(">")
      victimid = targetid[0]
      print(victimid)
      final = int(victimid)
      kicked = guild.get_member(final)
      x = True
      await message.channel.send(f"Waking up {ax}, please hold...")
      while x <= 100:
        await kicked.send(f"{kicked.mention}")
        x += 1
    
  if message.content.lower().startswith("p!kick"):
    if configured == True:
      if manrole in message.author.roles:
        try:
          argsaf = message.content.split("p!kick ")
          print(len(argsaf))
          argsaf = argsaf[1]
          try:
            args = argsaf.split(" ", 1)
            print(len(args))
            print(args)
            if len(args) == 2:
              reason = args[1]
              print(reason)
              member = args[0]
              print(member)
              try:
                idsas = member.split("<@")
                c = idsas[1]
                roleid = c.split(">")
                final = roleid[0]
                print(final)
                final = int(final)
                kicked = guild.get_member(final)
                await kicked.kick(reason=reason)
            
                kickemr = discord.Embed(title="Member kicked", description=f"{member} has been kicked from the server.")
                await message.channel.send(embed=kickemr)
                logmsg = discord.Embed(title="Member Kicked", description=f"{member} was kicked by {message.author.mention} for the reason: {reason}")
                await logchannel.send(embed=logmsg)
              except Exception as e:
                errorembed = discord.Embed(title="Error kicking user", description=f"Error kicking {member}. Please ensure that this is a valid member, or that you dragged my role above the highest role of the member that you are trying to kick. Error Code: {e}")
                await message.channel.send(embed=errorembed)
            if len(args) == 1:
              member = args[0]
              print(member)
              try:
                idsas = member.split("<@")
                c = idsas[1]
                roleid = c.split(">")
                final = roleid[0]
                print(final)
                final = int(final)
                kicked = guild.get_member(final)
                await kicked.kick()
                kickemb = discord.Embed(title="Member kicked.", description=f"{member} has been kicked from the server.")
                await message.channel.send(embed=kickemb)
                emergencyemb = discord.Embed(title="ADMIN ABUSE ALERT", description=f"""{member} has been kicked for no reason by {message.author.mention}.
Overseers, please review for possible Admin Abuse as soon as possible.""")
                await logchannel.send(embed=emergencyemb)
                await logchannel.send("<@&1084328650272428102>")
              except Exception as e:
                await message.channel.send(f"Error kicking {member}. Please ensure that is a valid member, or that you dragged my role above the highest role of the member you are trying to kick. Error code: {e}")
          
          except IndexError:
            errorembeds = discord.Embed(title="Error", description="""Invalid arguments. Please try again.
Format: p!kick [Ping user] [REASON]""")
            await message.channel.send(embed=errorembeds)
          except Exception as e:
            print(e)
        except IndexError:
          errorembeds = discord.Embed(title="Error", description="""Invalid arguments. Please try again.
Format: p!kick [Ping user] [REASON]""")
          await message.channel.send(embed=errorembeds)
    else:
      unconf = discord.Embed(title="Moderation Module Not Configured!", description="The moderation module is not configured in this server yet. If this is a mistake, please contact the owner of the server to fix this by running '.configuremods'. If this still does not work, please contact kyky#4277 immediately. Thank you.")
      await message.channel.send(embed=unconf)
  if message.content.lower().startswith("p!ban"):
    if configured == True:
      if manrole in message.author.roles:
        try:
          argsafb = message.content.split("p!ban ")
          print(len(argsafb))
          argsafb = argsafb[1]
          try:
            argsb = argsafb.split(" ", 1)
            print(len(argsb))
            print(argsb)
            if len(argsb) == 2:
              reasonb = argsb[1]
              print(reasonb)
              memberb = argsb[0]
              print(memberb)
              try:
                idsasb = memberb.split("<@")
                cb = idsasb[1]
                roleidb = cb.split(">")
                finalb = roleidb[0]
                print(finalb)
                finalb = int(finalb)
                banned = guild.get_member(finalb)
                await banned.ban(reason=reasonb)
                banemr = discord.Embed(title="Member banned", description=f"{memberb} has been banned from the server.")
                await message.channel.send(embed=banemr)
                logmsgb = discord.Embed(title="Member Banned", description=f"{memberb} was banned by {message.author.mention} for the reason: {reasonb}")
                await logchannel.send(embed=logmsgb)
              except Exception as e:
                errorembedb = discord.Embed(title="Error kicking user", description=f"Error kicking {memberb}. Please ensure that this is a valid member, or that you dragged my role above the highest role of the member that you are trying to kick. Error Code: {e}")
                await message.channel.send(embed=errorembedb)
          except IndexError:
            errorembeds = discord.Embed(title="Error", description="""Invalid arguments. Please try again.
Format: p!kick [Ping user] [REASON]""")
            await message.channel.send(embed=errorembeds)
          if len(argsb) == 1:
            memberb = argsb[0]
            print(memberb)
            try:
              idsasb = memberb.split("<@")
              cb = idsasb[1]
              roleidb = cb.split(">")
              finalb = roleidb[0]
              print(finalb)
              finalb = int(finalb)
              banned = guild.get_member(finalb)
              await banned.ban()
              banemb = discord.Embed(title="Member Banned", description=f"{memberb} has been banned from the server.")
              await message.channel.send(embed=banemb)
              emergencyemb = discord.Embed(title="ADMIN ABUSE ALERT", description=f"""{memberb} has been banned for no reason by {message.author.mention}.
Potatoes, please review for possible Admin Abuse as soon as possible.""")
              await logchannel.send(embed=emergencyemb)
              await logchannel.send("<@&1084328650272428102>")
            except Exception as e:
              await message.channel.send(f"Error with {memberb}. Please ensure that is a valid member, or that you dragged my role above the highest role of the member you are trying to kick. Error code: {e}")
          else:
            errorembeds = discord.Embed(title="Error", description="""Invalid arguments. Please try again.
Format: p!ban [Ping user] [REASON]""")
            await message.channel.send(embed=errorembeds)  
        except IndexError:
          errorembeds = discord.Embed(title="Error", description="""Invalid arguments. Please try again.
Format: p!ban [Ping user] [REASON]""")          
          await message.channel.send(embed=errorembeds)
        except Exception as e:
          print(e)
    else:
      uncon = discord.Embed(title="Server Moderation Not Configured", description="This server does not have moderation configured. To fix this, please contact the server owner to run '.configuremods' in a channel. If this is an error, please DM kyky#4277. Thank you.")
      await message.channel.send(embed=uncon)
keep_alive()

client.run(os.getenv('TOKEN'))
