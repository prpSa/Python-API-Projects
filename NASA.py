# import required modules
from configparser import ConfigParser
import tkinter
from typing import final
import requests
from tkinter import *
from tkinter import messagebox
from urllib3 import 
  
# extract key from the
# configuration file

url1 = 'https://api.nasa.gov/planetary/apod?api_key=f2keMNnoeYtVXghRRRngZMuQMatW2IdweZAJQzH7'
  
  
# explicit function to get
# weather details
def getweather():
    result = requests.get(url1)       
    if result:
        json = result.json()
        title = json['title']
        author = json['copyright']
        url = json['url']
        final = [title, author, url]
        return final
    else:
        print("NO Content Found")
  
  
# explicit function to
# search city
def search():
    weather = getweather()
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        u = urlopen(weather[2])
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        photo = ImageTk.PhotoImage(im)
        img = PhotoImage(file=weather[2])      
        canvas.create_image(20,20, anchor=NW, image=img)      
        
    else:
        messagebox.showerror('Error', "Cannot find Poem")
  
  
# Driver Code
# create object
app = Tk()
# add title
app.title("NASA Image of the Day")
# adjust window size
app.geometry("700x600")
  
# add labels, buttons and text

Search_btn = Button(app, text="Find Image", 
                    width=12, command=search)
Search_btn.pack()
location_lbl = Label(app, text="", font={'bold', 20})
location_lbl.pack()
canvas = Canvas(app, width = 300, height = 300)  
canvas.pack()  
app.mainloop()