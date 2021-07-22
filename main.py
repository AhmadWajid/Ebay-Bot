from bs4 import BeautifulSoup
import requests
#from webdriver import keep_alive
import discord
import time
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command("help")

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=""))
	print(f'Logged in as {bot.user.name}')

@commands.command(name="ebay")
async def ebay(ctx):
  message = ctx.message.content.split('!ebay ')
  url = message[1]
  pname = str(url)
  url = url.replace(' ', '+')
  url ='https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&_ipg=200'.format(url)
  print(url)
  pname=str(pname)
  embeder = 	discord.Embed(title='Processing...', description='Looking for `{}`.\n\nThis may take some time...'.format(pname),  color=0x00bfff)
  sendd1 = await ctx.send(embed=embeder)
  x = requests.get(url)
  time.sleep(2)
  embeder = 	discord.Embed(title='Processing...', description='Looking for `{}`.\n\nThis may take some time...\n\n`Scraping Prices...`'.format(pname),  color=0x00bfff)
  embeder.set_thumbnail(url='https://cdn0.iconfinder.com/data/icons/big-file-flat/32/02_Cloud_Computing_computer_internet_file_data-512.png')
  sendd = await sendd1.edit(embed=embeder)
  soup = BeautifulSoup(x.content, 'html.parser')
  together = []
  allitems = soup.find_all('span', class_='s-item__price')
  for price in allitems:
    price = price.text
    price = price.replace('$', '')
    price = price.replace(',', '')
    if 'to' in price:
      pass
    else:
      price = int(float(price))
      together.append(price)
  embeder = 	discord.Embed(title='Processing...', description='Looking for `{}`.\n\nThis may take some time...\n\n`Doing math...`'.format(pname),  color=0x00bfff)
  embeder.set_thumbnail(url='https://www.pngmart.com/files/7/Calculator-PNG-Picture.png')
  new = await sendd1.edit(embed=embeder)
  time.sleep(4)
  items = len(together)
  total = sum(together)
  average = total/items
  average = round(average, 2)
  average = str(average)
  items = str(items)
  embeder = 	discord.Embed(title='Done', description='Here is what I found.\n\nItem : `{}`\n\nAverage Price : `${}`\n\nTotal number of items counted : `{}`'.format(pname,average,items),  color=0x00bfff)
  embeder.set_thumbnail(url='https://assets.stickpng.com/thumbs/5aa78e207603fc558cffbf19.png')
  sendd = await sendd1.edit(embed=embeder)

bot.add_command(ebay)


#keep_alive()

bot.run('bot-token')