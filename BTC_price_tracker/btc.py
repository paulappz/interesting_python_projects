#usimg an api to fetech the price of BTC


import requests #for the api
import tkinter as tk # for the ui
from datetime import datetime



#Method to call API

def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response = requests.get(url).json()
    print(response)
    #save text inside ui
    price = response["USD"]
    time = datetime.now().strftime("%H:%M:%S") 


    labelPrice.config(text = str(price) + " $")
    labelTime.config(text = " Updated at: " + time)

    canvas.after(1000, trackBitcoin)


#define ui
canvas = tk.Tk()
canvas.geometry("400x500");
canvas.title("BTC Tracker")

# define  fonts on canvas
f1 = ("poppins", 24,  "bold")
f2 = ("poppins", 22,  "bold")
f3 = ("poppins", 18,  "normal")

#define label
label =tk.Label(canvas, text = "BTC Price", font = f1)
label.pack(pady=20)

labelPrice =tk.Label(canvas, font = f2)
labelPrice.pack(pady=20)

labelTime =tk.Label(canvas, font = f3)
labelTime.pack(pady=20)

trackBitcoin()

canvas.mainloop()