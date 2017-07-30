import time
from DB import Db
from Weather import Weather


w = Weather()
db = Db()

while True:
    c_temp = w.getTemp()
    print("Current temp :{}".format(c_temp))
    db.update_temperature(c_temp)
    print("Temperature updated.\n")
    time.sleep(10)
