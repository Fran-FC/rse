from utils.electricity_bill_scraping import scrap
from utils.email_notifyer import notify_cheapest_hour
import time
import threading

def check(ini=0):
    prices = scrap()

    price_min = prices[0]
    hour_min = 0

    print("From {} to {} hours".format(ini, len(prices)))
    for i in range(ini, len(prices)):
        if(price_min > prices[i]):
            price_min = prices[i]
            hour_min = i
    return [price_min, hour_min]

def main():
    th_1 = None
    while(True):
        localtime = time.localtime()
        hour = localtime.tm_hour
        [price_min, hour_min] = check(ini=hour)
        
        if(th_1):
            th_1.join()
        th_1 = threading.Thread(target=notify_cheapest_hour, args=(price_min, hour_min))
        th_1.start()

        minutes_remaining = 23*60-hour*60-localtime.tm_min
        time.sleep(minutes_remaining*60) # wait until 00:00 hours of next day

        


if __name__ == "__main__":
    main()