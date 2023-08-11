import time

import fetch
from plyer import notification

Data = {
    "https://www.amazon.in/Razer-BlackShark-V2-Headset-RZ04-03240100-R3M1/dp/B08WBJHVYV": 5000,
    "https://www.amazon.in/Alienware-Bluetooth-Frequency-Wired-3-5-AW920H/dp/B0B38WB9HC?th=1": 10000,
    "https://www.amazon.in/Dell-Inspiron-i5-1335U-35-56Cms-Thunderbolt/dp/B0C1595WPW": 76000,
    "https://www.amazon.in/HP-i5-1335U-Graphics-Keyboard-15-hr0001TU/dp/B0C3CJX15D": 70000,
    "https://www.amazon.in/Samsung-inches-Crystal-Ultra-UA55AUE65AKXXL/dp/B0B15GSPQW": 45000,
    "https://www.amazon.in/LG-inches-Collection-OLEDevo-55LX1QPSA/dp/B0BM4PM1HW": 130000
}


while True:
    for url in Data.keys():
        name, price = fetch.fetch_data(url)

        if price == -1:
            print("Error in fetching " + url)
            continue

        if price <= Data[url]:
            notification.notify(title="Price Drop Alert", message="Price of " + name + " has dropped to " + str(price),
                                timeout=5)

    # Sleep for 5 minutes Before checking price again
#    time.sleep(300)
