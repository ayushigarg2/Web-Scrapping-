import time

import fetch
import mail

Data = {
    "https://www.amazon.in/gp/product/B0BSGQTVP1/ref=s9_acss_bw_cg_hpcg1_3a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-7&pf_rd_r=7JF04XYPMWWRM2MDM17N&pf_rd_t=101&pf_rd_p=13135cb5-6199-41c4-b472-1b7664bea9e6&pf_rd_i=1388921031&th=1" : (1000, "user1@gmail.com", "boAt Airdopes 170 TWS Earbuds"),
    "https://www.amazon.in/Sony-Cancellation-Headphones-Multi-Point-Connection/dp/B0BS74M665/ref=sr_1_2?keywords=wh720n&qid=1697452709&s=electronics&sr=1-2" : (8000, "user2@gmail.com", "Sony WH-CH720N, Wireless Over-Ear Active Noise Cancellation Headphones"),
    "https://www.amazon.in/Samsung-inches-Crystal-iSmart-UA55CUE60AKLXL/dp/B0C1GYTFXY/ref=sr_1_18?_encoding=UTF8&content-id=amzn1.sym.d980e9f6-d3ec-4916-9717-3b447a6dedc7&pd_rd_r=fdb63f0f-1346-402d-a275-46233142fa6c&pd_rd_w=WJ4yY&pd_rd_wg=SiySQ&pf_rd_p=d980e9f6-d3ec-4916-9717-3b447a6dedc7&pf_rd_r=T0577C9DDKYTSJWWF9F4&qid=1697452856&s=electronics&sr=1-18" : (44000, "user2@gmail.com", "Samsung 138 cm (55 inches) Crystal iSmart 4K Ultra HD Smart LED TV UA55CUE60AKLXL (Black)"),    
    "https://www.amazon.in/Fire-Boltt-Bluetooth-Calling-Assistance-Resolution/dp/B0BF57RN3K/?_encoding=UTF8&pd_rd_w=EUIFO&content-id=amzn1.sym.6b95a7bb-790e-4951-b966-0f05e9bb2a73&pf_rd_p=6b95a7bb-790e-4951-b966-0f05e9bb2a73&pf_rd_r=M7D6RM0MM5Q16AF80W09&pd_rd_wg=kvMOa&pd_rd_r=4074da48-a748-4e01-9877-844d9f7d3a95&ref_=pd_gw_CEPC&th=1" : (1000, "aggarwalayush251@gmail.com", "Fire-Boltt Ninja Call Pro Plus 1.83' Smart Watch" ),
    "https://www.amazon.in/LG-Inverter-Fully-Automatic-Loading-T70SKSF1Z/dp/B08DF1Y7T7/ref=sr_1_1?aaxitk=0059de2b2de3739700929f8b3ca49366&qid=1697457050&refinements=p_78%3AB084LF24Z8%7CB08DF1Y7T7%7CB0BD8ZGBD3%7CB0BF5RGZ8V%7CB0C3LPXHL3&sr=8-1&th=1" : (17000, "aggarwalayush251@gmail.com", "LG 7 Kg 5 Star Inverter TurboDrum Fully Automatic Top Loading Washing Machine "),
}

cooldown_price = 0.95

sender_email = input("Enter the Sender Email : ")
sender_pswd = input("Enter password or token : ")

while True:
    for url in Data.keys():
        name, price = fetch.fetch_data(url)

        print(price)

        if price == -1:
            print("Error in fetching " + url)
            continue
        
        if price <= Data[url][0]:
            mail.send_email("Amazon Price Drop Alert !",
                             "Exciting News! Price for your requested product, " + Data[url][2] + " has dropped to  an amazing " + str(price) +" value.\n\n Buy it before it goes out of stock or the price goes back up!\nHappy Shopping!",
                             Data[url][1], "smtp.gmail.com", 465, sender_email, sender_pswd)


            # This will automatically set the new desired price as 5% less than the current price
            Data[url] = (Data[url][0]*0.95, Data[url][1], Data[url][2])
    
    # Sleep for 5 minutes Before checking price again, freeing up resources for other processes
    time.sleep(300)
 

