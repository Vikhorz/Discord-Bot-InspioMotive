import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

------------------------------------

#Please check keep_alive.py because we use it for making our Bot work 24 hours a Day
#I used uptime robot to send a Ping every 5 minutes so the Bot keeps working! check https://uptimerobot.com
#read the uptime robot file for more information
------------------------------------

print('logging...')
#discord.ActivityType.watching()
client = discord.Client()


sad_words = ["sad", "depressed", "heartbroken", "unhappy", "lonely", "depressing", "angry", "bored", "boring", "worried"]

happy_words = ["happy", "better", "good", "helpful", "cheerful", "joyful"]

other_words = ["Thank you", "Thanks", "thanks", "thank you", "appreciate", "Appreciate"]

special_words = ["HBD", "hbd", "Happy Birthday"]

starter_inspo = [
 "Cheer up!",
 "everything is going to be OK.",
 "Some days you have to create your own sunshine."
]

starter_inspo2 = ["That's so good to hear!", "That's great! :D ", "I am glad I was able to help :)", ":)", ":D"
]

starter_inspo3 = ["You're welcome.", "You're very welcome.", "No problem.", "Don't mention it.", "It's my pleasure.", "My pleasure.", "Anytime.", "Glad to help!", "Sure!"
]

starter_inspo4 = ['“Wishing you a beautiful day with good health and happiness forever. Happy birthday!”', 'Words alone are not enough to express how happy I am you are celebrating another year of your life! My wish for you on your birthday is that you are, and will always be, happy and healthy. Don’t ever change! Happy birthday my dear.']


if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_inspo(inspiring_message):
  if "inspo" in db.keys():
   inspo = db["inspo"]
   inspo.append(inspiring_message)
   db["inspo"] = inspo
  
  else:
    db["inspo"] = [inspiring_message]

def delete_inspo(index):
  inspo = db["inspo"]
  if len(inspo) > index:
    del inspo[index]
    db["inspo"] = inspo


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name='CHANGE THIS!(your preferred platform if u want)', url="CHANGE THIS!(your preferred url...)")) 

@client.event
async def on_message(message):

  if message.author == client.user:
   return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_inspo
    if "inspo" in db.keys():
      options = options + (db["inspo"]).value
    
    if any(word in msg for word in sad_words):
     await message.channel.send(random.choice(options))
   
    if any(word in msg for word in happy_words):
     await message.channel.send(random.choice(starter_inspo2))

    if any(word in msg for word in other_words):
     await message.channel.send(random.choice(starter_inspo3))

    if any(word in msg for word in special_words):
     await message.channel.send(random.choice(starter_inspo4))

  if msg.startswith('$new'):
    inspiring_message = msg.split("$new ",1)[1]
    update_inspo(inspiring_message)
    await message.channel.send('New inspiring message added.')

  if msg.startswith('$del'):
    inspo = []
    if "inspo" in db.keys():
      index = int(msg.split("del",1)[1])
      delete_inspo(index)
      inspo = db["inspo"]
      str_ins1 = "Message was deleted successfully. list of remaining inspiring messages: "
      await message.channel.send(str_ins1)
      await message.channel.send(inspo.value)

  if msg.startswith('$list'):
    inspo = []
    if "inspo" in db.keys():
      inspo = db["inspo"]
      str_ins2 = "List of inspiring messages: "
      await message.channel.send(str_ins2)
      await message.channel.send(inspo.value)
  
  if msg.startswith('$responding'):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is [ON].")
    else:
      db["responding"] = False
      await message.channel.send("Responding is [OFF].") 

keep_alive()
client.run(os.getenv('nheni')) 

