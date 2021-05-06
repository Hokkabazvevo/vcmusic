# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selamm 👋 sesli sohbetlerde şarkı dinlemeniz için kodlanmış robotum.\n\nBeni grubunuza eklemek için tıklayın. \'Kullanma Klavuzu\' Botu nasıl kullanacağınızı öğrenmek için tıklayın.\n\n✣ Ekle [Müzik Bot](https://t.me/MoolMusicBot) Sesli sohbetinizde müzik dinlemek için.\n\nDeveloper By [Zephyrus](https://t.me/Zep_Unb)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Kullanma Klavuzu", url="https://t.me/Zep_Dev")
                  ],[
                    InlineKeyboardButton(
                        "Destek Grubu", url="https://t.me/DepressionalistChat"
                    ),
                    InlineKeyboardButton(
                        "Kanal", url="https://t.me/Zep_Dev"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Destek Grubu", url="https://t.me/DepressionalistChat"
                    ),
                    InlineKeyboardButton(
                        "Developer", url="https://t.me/Zep_Unb"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Pemutar Musik Sedang Online **""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Destek Grubu", url="https://t.me/DepressionalistChat"
                    ),
                    InlineKeyboardButton(
                        "Developer", url="https://t.me/Zep_Dev"
                    )
                ]
            ]
        )
   )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Panduan Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Panduan Menggunakan BOT 📜", url="https://t.me/Lunatic0de/20"
                    )
                ]
            ]
        ),
    )
