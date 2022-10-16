# Bot Download Credit: @apkredo.com

from __future__ import print_function
from __future__ import unicode_literals
import logging
import youtube_dl
import os
import subprocess
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram_upload.client import Client
import telegram
import requests
import urllib.request
import youtube_dl.utils
import json
import os.path
from datetime import datetime
from pytz import timezone
import time
import re
import math 
from telethon import TelegramClient
from functools import partial
from telegram_upload.exceptions import ThumbError, TelegramUploadDataLoss, TelegramUploadNoSpaceError
from telegram_upload.files import get_file_attributes, get_file_thumb
from telethon.version import __version__ as telethon_version
from telethon.tl.types import Message, DocumentAttributeFilename
from telethon.utils import pack_bot_file_id
import psycopg2
from psycopg2 import OperationalError

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
        from sample_config import Config
else:
        from config import Config

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


akunUser = Config.AUTH_USERS
SERVER = SERVER


api_id = 13593788
api_hash = "3faac9cc8c824e815ad40eadc426ee50"
bot_token = Config.BOT_TOKEN

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
bot = telegram.Bot(token=bot_token)

API_NAME1 = "https://rest-api-baymaxstreaming-1.herokuapp.com/"
API_NAME2 = "https://rest-api-baymaxstreaming-2.herokuapp.com/"
API_NAME3 = "https://rest-api-baymaxstreaming-3.herokuapp.com/"
API_NAME4 = "https://rest-api-baymaxstreaming-4.herokuapp.com/"



def upload(update: Update, context: CallbackContext) -> None:
        # print(update)
        with open('namahost.txt') as f:
                content = f.readlines()
        print(content[0])

        if os.path.isfile('Credit @Baymaxstreaming.mp4'):
                print ("File exist")
                os.remove('Credit @Baymaxstreaming.mp4')

        if os.path.isfile('@HiroHamadabatbot.flv'):
                print ("File exist")
                update.message.reply_text('File Masih ada dan akan di upload ulang :)')
                convertText = update.message.reply_text('Sedang menconvert video')
                subprocess.call(['ffmpeg', '-i', '@HiroHamadabatbot.flv', '-codec', 'copy', 'Credit @Baymaxstreaming.mp4','-y'])
                try:
                        bot.deleteMessage(message_id =convertText['message_id'], chat_id =convertText['chat']['id'])
                except:
                        pass
                niceclient('Credit @Baymaxstreaming.mp4',content[0], update, context)

        elif os.path.isfile('@HiroHamadabatbot.flv.part'):
                print ("File exist")
                update.message.reply_text('File Masih ada dan akan di upload ulang :)')
                os.rename('@HiroHamadabatbot.flv.part','@HiroHamadabatbot.flv')
                convertText = update.message.reply_text('Sedang menconvert video')
                subprocess.call(['ffmpeg', '-i', '@HiroHamadabatbot.flv', '-codec', 'copy', 'Credit @Baymaxstreaming.mp4','-y'])
                try:
                        bot.deleteMessage(message_id =convertText['message_id'], chat_id =convertText['chat']['id'])
                except:
                        pass
                niceclient('Credit @Baymaxstreaming.mp4',content[0], update, context)

        else:
                update.message.reply_text('File sudah terhapus, server merestart ulang :(')


def start(update: Update, context: CallbackContext) -> None:
        # print(update)
        update.message.reply_text('Bot Sudah Siap Download! Kirim Link Sekarang :)')

def help_command(update: Update, context: CallbackContext) -> None:
        update.message.reply_text('Tips!\nBeri perintah /start untuk memulai bot\nBeri perintah /upload untuk mencoba upload ulang jika mengalami gagal upload')

def echo(update: Update, context: CallbackContext) -> None:
        if  update.message.chat.id == akunUser or update.message.chat.id == SERVER:
                #bot.send_message(SERVER, update.message.text )
                if os.path.isfile('Credit @Baymaxstreaming.mp4'):
                        print ("File exist")
                        os.remove('Credit @Baymaxstreaming.mp4')

                if os.path.isfile('Credit @Baymaxstreaming.mp4.part'):
                        print ("File exist")
                        os.remove('Credit @Baymaxstreaming.mp4.part')

                if os.path.isfile('@HiroHamadabatbot.flv'):
                        print ("File exist")
                        os.remove('@HiroHamadabatbot.flv')

                if os.path.isfile('@HiroHamadabatbot.flv.part'):
                        print ("File exist")
                        os.remove('@HiroHamadabatbot.flv.part')

                #bot.send_message(SERVER, update.message.text )
                youtube_dl.utils.std_headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
                import time
                start = time.time()

                headers = {
                "Content-Type": "application/json",
                "Accept": "application/json", 
                }
                data = {
                    "link": update.message.text
                }
                try:
                        r = requests.get(url = API_NAME1, data=json.dumps(data),headers=headers, timeout=20)
                        linkdetail = r.json()
                        namaFile = linkdetail['nama']
                        tipeDownload = linkdetail['tipe']
                except:
                        try:
                                r = requests.get(url = API_NAME2, data=json.dumps(data),headers=headers, timeout=20)
                                linkdetail = r.json()
                                namaFile = linkdetail['nama']
                                tipeDownload = linkdetail['tipe']
                        except:
                                try:
                                        r = requests.get(url = API_NAME3, data=json.dumps(data),headers=headers, timeout=20)
                                        linkdetail = r.json()
                                        namaFile = linkdetail['nama']
                                        tipeDownload = linkdetail['tipe']
                                except:
                                        try:
                                                r = requests.get(url = API_NAME4, data=json.dumps(data),headers=headers, timeout=20)
                                                linkdetail = r.json()
                                                namaFile = linkdetail['nama']
                                                tipeDownload = linkdetail['tipe']
                                        
                                        except:
                                          bot.send_message(akunUser,"Server sibuk nih, Kirim ulang linknya :)")


                url=update.message.text
                findText=re.findall(r'(?<=http)', url) 
                if findText:
                    url = url
                else:
                    url=url.replace('.flv','')
                    print(namaFile)

                uploadText = update.message.reply_text('Downloading '+str(namaFile))

                if tipeDownload == 2 or tipeDownload == 1:
                        outtmpl = '@HiroHamadabatbot.flv'
                        dbl = partial(my_hook,start=start,uploadText= uploadText,namaFile=str(namaFile))
                else:
                        outtmpl = 'Credit @Baymaxstreaming.mp4'
                        dbl = partial(progress_for_pyrogram,total='',ud_type='Sedang Download',start=start,uploadText= uploadText,namaFile=str(namaFile))

                ydl_opts = {
                        'outtmpl': outtmpl,
                        'format': 'best',
                        'logger': MyLogger(),
                        'progress_hooks': [dbl],
                }

                if tipeDownload == 2:
                        subprocess.call(['ffmpeg', '-i', url, '-vcodec', 'copy', '-acodec', 'copy', '@HiroHamadabatbot.flv','-y' ])
                        convertText = update.message.reply_text('Sedang menconvert video')
                        subprocess.call(['ffmpeg', '-i', "@HiroHamadabatbot.flv", '-codec', 'copy', 'Credit @Baymaxstreaming.mp4','-y'])
                        try:
                                bot.deleteMessage(message_id =convertText['message_id'], chat_id =convertText['chat']['id'])
                        except:
                                pass
                        try:
                                niceclient('Credit @Baymaxstreaming.mp4',namaFile, update, context)
                        except:
                                print("gagal")
                else:
                        try:
                                print("masuk sini")
                                print(url)
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                        ydl.download([str(url)])
                                convertText = update.message.reply_text('Sedang menconvert video')
                                subprocess.call(['ffmpeg', '-i', outtmpl, '-codec', 'copy', 'Credit @Baymaxstreaming.mp4','-y'])
                                try:
                                        bot.deleteMessage(message_id =convertText['message_id'], chat_id =convertText['chat']['id'])
                                except:
                                        pass
                                try:
                                        niceclient('Credit @Baymaxstreaming.mp4',namaFile, update, context)
                                except:
                                        print("gagal")

                        except:
                                try:
                                        url = update.message.text
                                        video_name = url.split('/')[-1]
                                        print ("Downloading file:%s" % video_name)
                                        urllib.request.urlretrieve(url, 'Credit @Baymaxstreaming.mp4')
                                        print ("Downloading :%s Selesai" % video_name)
                                        print(os.path.getsize('Credit @Baymaxstreaming.mp4'))
                                        try:
                                                niceclient('Credit @Baymaxstreaming.mp4','@HiroHamadabatbot',update,context)
                                        except:
                                                print("gagal")
                                except:
                                        update.message.reply_text('Link Mati/Bot Tidak Support')
        else:
                update.message.reply_text('''
Bot ini milik orang lain 😁
jika ingin pakai bot seperti ini, kamu bisa Order: @HiroHamadabatbot
[KELEBIHAN BOT DOWNLOAD]
1. Bot ini berfungsi sebagai pengganti IDM
2. Support aplikasi Mango live, Dreamlive, Sugar Live, Bling2, 69Live, Mlive, dll
3. Tidak abisin KUOTA internet karena di download/upload di server bukan hp
4. Tidak menuhin memory hp, karena video kesimpen di telegram, bisa di play/donlot kpn aja
5. Bisa menggunakan HP Andorid/Iphone
6. Download/upload Otomatis (tinggal tidur aja hihihi)
7. hasil video di bot gabisa diliat org lain.
8. Cocok bagi yang suka record untuk koleksi pribadi.

Selengkapnya bisa baca di: https://t.me/Baymaxstreaming
Untuk Order Bot bisa DM admin : @HiroHamadabatbot''')

class MyLogger(object):
        def debug(self, msg):
                pass
        def warning(self, msg):
                pass
        def error(self, msg):
                print(msg)

def my_hook(d,start,uploadText,namaFile):
        message_id=uploadText['message_id']
        chat_id=uploadText['chat']['id']

        if d['status'] == 'finished':
                print('Download RTMP SELESAI')
                # file_tuple = os.path.split(os.path.abspath(d['filename']))
                # print("Done downloading {}".format(d['filename']))
                try:
                        bot.deleteMessage(message_id =message_id, chat_id =chat_id)
                except:
                        pass

        if d['status'] == 'downloading':
                print(d['filename'], d['_speed_str'], d['_percent_str'], d['_eta_str'])
                now = time.time()
                diff = now - start
                if round(diff % 10.00) == 0:
                        elapsed_time = round(diff) * 1000
                        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
                        progress = "[█████████████░░░]"
                        tmp = progress + "\nSpeed: {0}\nElapsed time: {1}\n".format(d['_speed_str'],elapsed_time)
                        print("{0} {1}\n {2}".format("Sedang Download",namaFile,tmp))
                        try:
                                bot.editMessageText(message_id =message_id, chat_id =chat_id,
                                        text="{0} {1}\n {2}".format("Sedang Download",namaFile,tmp)
                                )
                        except:
                                pass

def TimeFormatter(milliseconds: int) -> str:
        seconds, milliseconds = divmod(int(milliseconds), 1000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        tmp = ((str(days) + "d, ") if days else "") + \
                ((str(hours) + "h, ") if hours else "") + \
                ((str(minutes) + "m, ") if minutes else "") + \
                ((str(seconds) + "s, ") if seconds else "") + \
                ((str(milliseconds) + "ms, ") if milliseconds else "")
        return tmp[:-2]

def humanbytes(size):
        # https://stackoverflow.com/a/49361727/4723940
        # 2**10 = 1024
        if not size:
                return ""
        power = 2**10
        n = 0
        Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
        while size > power:
                size /= power
                n += 1
        return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'

def progress_for_pyrogram(current,total,ud_type,start,uploadText,namaFile):
        # message_id= message['message_id']
        # chat_id= message['chat']['id']
        if ud_type == 'Sedang Download':
           total=current['total_bytes']
           current=current['downloaded_bytes']
        else:
                current = current
                total = total
        print(ud_type , current, 'out of', total,
                  'bytes: {:.2%}'.format(current / total))
        message_id=uploadText['message_id']
        chat_id=uploadText['chat']['id']

        now = time.time()
        diff = now - start
        if round(diff % 10.00) == 0 or current == total:
                # if round(current / total * 100, 0) % 5 == 0:
                percentage = current * 100 / total
                speed = current / diff
                elapsed_time = round(diff) * 1000
                time_to_completion = round((total - current) / speed) * 1000
                estimated_total_time = elapsed_time + time_to_completion

                elapsed_time = TimeFormatter(milliseconds=elapsed_time)
                estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

                progress = "[{0}{1}] \nP: {2}%\n".format(
                        ''.join(["█" for i in range(math.floor(percentage / 5))]),
                        ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
                        round(percentage, 2))

                tmp = progress + "{0} of {1}\nSpeed: {2}/s\nElapsed time : {3}\nETA: {4}\n".format(
                        humanbytes(current),
                        humanbytes(total),
                        humanbytes(speed),
                        elapsed_time if elapsed_time != '' else "0 s",
                        estimated_total_time if estimated_total_time != '' else "0 s"
                )
                # print("{}\n {}".format(
                #           ud_type,
                #           tmp
                #       ))
                try:
                        bot.editMessageText(message_id =message_id, chat_id =chat_id,
                                text="{} {}\n {}".format(
                                        ud_type,
                                        namaFile,
                                        tmp
                                )
                        )

                except:
                        pass

        if current == total:
                try:
                        bot.deleteMessage(message_id =message_id, chat_id =chat_id)
                except:
                        pass


def upload_video(uploadText,name,namaFile):
        print('sedang upload ' +str(namaFile))
        start = time.time()
        filename = name
        dbl = partial(progress_for_pyrogram,ud_type='Sedang Upload',start=start,uploadText= uploadText,namaFile=namaFile)

        async def upload_file():
                file = await client.upload_file(filename, progress_callback=dbl)
                file_name = os.path.basename(filename)
                file_size = os.path.getsize(filename)
                thumb = None
                try:
                        thumb = get_file_thumb(filename)
                except ThumbError as e:
                        print('{}'.format(e), err=True)
                try:
                        attributes = get_file_attributes(filename)
                        try:
                                await client.send_file(akunUser, file, thumb=thumb, caption=namaFile, attributes=attributes, supports_streaming=True)
                                print('berhasil')
                                await client.send_file(SERVER, file, thumb=thumb, caption=namaFile, attributes=attributes, supports_streaming=True)
                                print('berhasil')
                                # bot.send_message('-1001688810274, 'update.message.text' )

                        finally:
                                print('Upload Video berhasil')
                finally:
                        if thumb:
                                os.remove(thumb)
                print(file)

        with client:
                client.loop.run_until_complete(upload_file())

def niceclient(name, namaFile, update: Update, context: CallbackContext):
        print(name)
        try:
                ya = os.path.getsize(name)
                print(ya)
                try:
                        if ya > 1900000000:
                                halo = subprocess.check_output(['python', 'ffmpegsplit.py' , '-f', name, '-s', '3600'])
                                halo = halo.decode("utf-8")
                                print('INI HASILNYA : '+str(halo))
                                findText=re.findall(r'(?<=SPLIT COUNT =)(.*?)(?= BUAH)', halo)
                                print(findText[0])
                                rep = name.replace('.mp4','')
                                update.message.reply_text('Video size sebesar : '+str(round(ya/1000000))+' MB akan di split menjadi ' +str(findText[0]) +' Video')
                                for x in range(int(findText[0])):
                                        sizesplit = os.path.getsize(rep+'-'+str(x+1)+'-of-'+str(findText[0])+'.mp4')

                                        print('Sedang Upload Video ke '+str(x+1))
                                        print('Sedang Upload Sebesar '+ str(round(sizesplit/1000000))+' MB')
                                        print(rep+'-'+str(x+1)+'-of-'+str(findText[0])+'.mp4')

                                        uploadText = update.message.reply_text('Sedang Upload Video ke '+str(x+1)+ ' dari ' +str(findText[0])+' video, Sebesar '+ str(round(sizesplit/1000000))+' MB')
                                        nameT = rep+'-'+str(x+1)+'-of-'+str(findText[0])+'.mp4'
                                        upload_video(uploadText,nameT,namaFile)
                                        time.sleep(2)
                                        try:
                                                os.remove(rep+'-'+str(x+1)+'-of-'+str(findText[0])+'.mp4')
                                        except:
                                                print('sudah di hapus')
                                        print('berhasil upload')
                                try:
                                        os.remove(name)
                                        os.remove('@HiroHamadabatbot.flv')
                                except:
                                        print('sudah di hapus')
                                update.message.reply_text('Semua Video Berhasil Di Upload, Bot Bisa Digunakan kembali. :)')

                        else:
                                print('Sedang Upload Sebesar '+ str(round(ya/1000000))+' MB')
                                uploadText = update.message.reply_text('Sedang Upload Sebesar '+ str(round(ya/1000000))+' MB')
                                upload_video(uploadText,name,namaFile)
                                time.sleep(2)
                                try:
                                        os.remove(name)
                                        os.remove('@HiroHamadabatbot.flv')
                                except:
                                        print('sudah di hapus')
                                print('berhasil upload')
                                update.message.reply_text('Video Berhasil Di Upload, Bot Bisa Digunakan kembali. :)')

                except:
                        update.message.reply_text('Upload Gagal :( , server tidak stabil. atau Link Mati/Salah')
        except:
                update.message.reply_text('Link Mati/Host Offline/Host Lock Room')

def main():
        updater = Updater(bot_token, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("help", help_command))
        dispatcher.add_handler(CommandHandler("upload", upload))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
        main()

# Bot Download Credit: @apkredo.com
