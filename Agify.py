# import required modules
from configparser import ConfigParser
import requests
from tkinter import *
from tkinter import messagebox
  
# extract key from the
# configuration file

url = 'https://api.agify.io/?name={}'
  
  
# explicit function to get
# weather details
def getweather():
    result = requests.get(url.format(city_entry.get()))       
    if result:
        json = result.json()
        title = json['name']
        author = json['age']
        final = [title, author]
        return final
    else:
        print("NO Content Found")
  
  
# explicit function to
# search city
def search():
    weather = getweather()
    if weather:
        location_lbl['text'] = '{} :{}'.format(weather[0], weather[1])  
    else:
        messagebox.showerror('Error', "PLEASE ENTER A VALID NAME")
  
  
# Driver Code
# create object
app = Tk()
# add title
app.title("Agify")
# adjust window size
app.geometry("200x200")
  
# add labels, buttons and text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()
Search_btn = Button(app, text="Calculate Age", 
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()

