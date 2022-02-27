import sys
import tkinter as tk
import requests
import time

def getWeather(canvas):
    # Your api key
    api_key = "984b5d94811565a7725c9bbc4da5b5e0"
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + api_key
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 3600))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 3600))
    final_info = condition + "\n" + str(temp) + "C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed:" + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    data1.config(text = final_info)
    data2.config(text = final_data)

# background
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Pogoda")

# font
a = ("poppins", 15, "bold")
b = ("Times", 35, "bold italic")
# input window
textfield = tk.Entry(canvas, font = b)
textfield.pack(pady = 50)
textfield.focus()
textfield.configure(bg='yellow')
textfield.bind('<Return>', getWeather)
# show the data
data1 = tk.Label(canvas, font = b)
data1.pack()
data2 = tk.Label(canvas, font = a)
data2.pack()

# Loop
canvas.mainloop()