import argparse
import base64
import json
import logging
import signal
import struct
import sys
import time

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import paho.mqtt.client as mqtt
from datetime import datetime, timezone

temp_value = "VOID"
humidity_value = "VOID"
luminosity_value = "VOID"

ttn_broker = "eu1.cloud.thethings.network"
ttn_username = "lopys2ttn@ttn"
ttn_password = "NNSXS.A55Z2P4YCHH2RQ7ONQVXFCX2IPMPJQLXAPKQSWQ.A5AB4GALMW623GZMJEWNIVRQSMRMZF4CHDBTTEQYRAOFKBH35G2A"
ttn_topic = "v3/+/devices/#"


def on_connect(client, userdata, flags, rc):
    print("Connected to ", client._host, "port: ", client._port)
    print("Flags: ", flags, "returned code: ", rc)

    client.subscribe("v3/+/devices/#", qos=0)


def on_message(client, userdata, msg):
    global humidity_value, temp_value, luminosity_value
    print("msg received with topic: {} and payload: {}".format(
        msg.topic, str(msg.payload)))

    if (msg.topic == "v3/lopys2ttn@ttn/devices/lopy4sense/up"):

        themsg = json.loads(msg.payload.decode("utf-8"))
        dpayload = themsg["uplink_message"]["decoded_payload"]

        print("@%s >> temp=%.3f hum=%.3f lux=%.3f" %
              (time.strftime("%H:%M:%S"), dpayload["temperature"],
               dpayload["lux"], dpayload["humidity"]))

        temp_value = dpayload["temperature"]
        humidity_value = dpayload["humidity"]
        luminosity_value = dpayload["lux"]



def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text="Sorry, I didn't understand that command.")

def gettemp(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(temp_value))

def gethumidity(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(humidity_value))

def getlum(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=str(luminosity_value))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(
    ttn_username,
    password=ttn_password
)
client.connect(ttn_broker, port=1883, keepalive=60)
client.loop_start()


updater = Updater(token='2136157447:AAHN6PWcNz2jcuDT0Hix-0-179Is1gfqWis', use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

gettemp_handler = CommandHandler('gettemp', gettemp, pass_args=False)
dispatcher.add_handler(gettemp_handler)

gethumidity_handler = CommandHandler('gethum', gethumidity, pass_args=False)
dispatcher.add_handler(gethumidity_handler)

getlum_handler = CommandHandler('getlum', getlum, pass_args=False)
dispatcher.add_handler(getlum_handler)

unknown_handler = MessageHandler(Filters.text & (~Filters.command), unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()

updater.idle()
