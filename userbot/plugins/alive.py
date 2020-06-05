"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**MY STATUS** \n`FRIDAY IS:` **✅ Alive**\n\n"
                     "`🌹TELETHON VERSION:` **6.0.9**✅\n`🐍Python:` **3.7.4**✅\n"
                     "`DATABASE STATUS:` **WORKING FINE 🙂**\n\n`SYSTEM is 🔥!, NO malacious activity detected✅\n`"
                     " `🔘🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔸🔘\n"
               
                     " CURRECT BOT LOCATION:**NEW YORK,UNITED STATES**\n"
                     "`🔻🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻🔺🔻\n"
                     "`IP:` **3.82.66.232**\n"
                     "`SYSTEM TYPE:`👑 LINUX✅\n"
                     "`BASED ON:`🧬JARVIS Works❤️\n"
                     "`SATELLITE🛰️:` ⚡TONY STARK SAT-2⚡\n"
                     "`MADE USING:` 🐍PYTHON\n"
                     f"`MY BOSS`: {DEFAULTUSER}☣️\n\n"
                     "AT YOUR SERVICE ,MY BOSS\n\n"
                     "`MAINTAINER: TONY STARK...aka (ROBERT DOWNEY.Jr)✅ \n\n"
                     )
    
                     

