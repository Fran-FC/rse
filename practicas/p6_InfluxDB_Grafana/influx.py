from influxdb import InfluxDBClient

client = InfluxDBClient(host="localhost", port="8086")
client.switch_database("telegraf")
res = client.query('SELECT * FROM "TTN" WHERE time > now() - 15m')
points = res.get_points()

for p in points:
    if p["uplink_message_decoded_payload_temperature"] and p["uplink_message_decoded_payload_humidity"]:
        temp = p["uplink_message_decoded_payload_temperature"]
        hum = p["uplink_message_decoded_payload_humidity"]

        print("Time {0}-> Temp: {1}, humidity: {2}".format(p["time"], temp, hum))
