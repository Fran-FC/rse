import smtplib, ssl, json, os
import time

port = 465 # ssl port for smtp
config_path = os.getcwd() + "/config/config.json"
sender_email = ""
password = ""
reciever_email = ""
with open(config_path) as fd:
    fconfig = fd.read()
    jconfig = json.loads(fconfig)

    reciever_email = jconfig["reciever_email"] 
    sender_email = jconfig["sender_email"]
    password = jconfig["sender_password"]


# Create a secure SSL context
context = ssl.create_default_context()

def send_mail(msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, msg)

def notify_cheapest_hour(price_min, hour_min):
    price_min = price_min
    msg = "Subject: Precio de la luz mas barato\n\nEl precio mas bajo es {0}kW/h a las {1} horas\nTabla de precios en: http://www.tarifadeluz.com".format(price_min, hour_min)

    # first we send an email at the beginning of a day (00:00)
    send_mail(msg)

    # we send another mail when the cheapest hour comes 
    if hour_min == 0:
        hour_min = 24
    minutes_remaining = (hour_min-1)*60-time.localtime().tm_hour*60-time.localtime().tm_min
    time.sleep(minutes_remaining*60) # sleep in seconds

    send_mail(msg)

    

