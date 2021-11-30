import smtplib, ssl
import time

port = 465 # ssl port for smtp

reciever_email = "frafolcm@gmail.com"
sender_email = "raspberryfranfc@gmail.com"
password = "proyecto_rse_fran_21"
#reciever_email = input("Enter your reciever email address: ") 
#sender_email = input("Enter your sender email address: ")
#password = input("Enter the sender email password: ")

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(msg):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciever_email, msg)

def notify_cheapest_hour(price_min, hour_min):
    msg = "El precio mas bajo es {0}kW/h a las {1} horas".format(price_min/1000, hour_min)
    if hour_min == 0:
        hour_min = 24
    send_email(msg)
    minutes_remaining = hour_min*60-time.localtime().tm_hour*60-time.localtime().tm_min

    print("Waiting to send {} minutes".format(minutes_remaining))
    time.sleep(minutes_remaining*60)
    send_email(msg)
