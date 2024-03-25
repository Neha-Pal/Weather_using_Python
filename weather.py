import requests
import tkinter as tk
from PIL import Image,ImageTk

root = tk.Tk()
root.title("Weather App")
root.geometry("600x300")

def format_weather(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temperature_f=weather['main']['temp']
        temperature_c = (temperature_f - 32) * 5/9
        temp=round(temperature_c)
        final=f'City: {city}\nCondition: {condition}\nTemperature: {temp}°C'
    except Exception as e:
        final = f'There was a problem: {str(e)}'
    return final     

def get_weather(city):
    api_key = '17ca6cb0dd1fe3a1840f54b69129d5a1'
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=imperial"
    response = requests.get(url)
    weather = response.json()
    output_label.config(text=format_weather(weather))


bg_label=tk.Label(root)
bg_label.place(x=0,y=0,width=600,height=300)

title=tk.Label(bg_label,text='Enter City Name:',fg='black',font=('popins',15))
title.place(x=76,y=18)

input_frame=tk.Frame(bg_label,bg='pink',bd=5)
input_frame.place(x=76,y=60,width=450,height=50)

text=tk.Entry(input_frame,font=('popins',15),width=32)
text.grid(row=0,column=0,sticky='w')

btn=tk.Button(input_frame,text='Done',fg='hotpink',font=('popins',15,'bold'),command=lambda:get_weather(text.get()))
btn.grid(row=0,column=1,padx=10)

output_frame = tk.Frame(bg_label, bg='pink', bd=5)
output_frame.place(x=76, y=160, width=450, height=100)

output_label = tk.Label(output_frame, text='', fg='black',bg='pink', font=('popins', 15), wraplength=400, justify='left',anchor='nw')
output_label.place(relheight=1,relwidth=1)
root.mainloop()

