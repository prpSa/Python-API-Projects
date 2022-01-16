# import required modules
from configparser import ConfigParser
from typing import final
import requests
from tkinter import *
from tkinter import messagebox
import random
  
# extract key from the
# configuration file

url = 'https://poetrydb.org/author,title/Shakespeare;Sonnet'
  
  
# explicit function to get
# weather details
def getweather():
    result = requests.get(url) 
    num = random.randint(0,20)
      
    if result:
        json = result.json()
        title = json[num]['title']
        author = json[num]['author']
        lines = json[num]['lines']
        linecount = json[num]['linecount']
        final = [title, author, lines, 
                 linecount]
        return final
    else:
        print("NO Content Found")
  
  
# explicit function to
# search city
def search():
    weather = getweather()
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[2]).replace(', ', '\n')
        weather_l['text'] = weather[3]
        
    else:
        messagebox.showerror('Error', "Cannot find Poem")
  
  
# Driver Code
# create object
app = Tk()
# add title
app.title("Poem Generator")
# adjust window size
app.geometry("700x600")
  
# add labels, buttons and text

Search_btn = Button(app, text="Search Poem", 
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(app, text="")
temperature_label.pack()
weather_l = Label(app, text="")
weather_l.pack()
app.mainloop()