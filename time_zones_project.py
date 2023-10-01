from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz 
import time

root = Tk()
root.geometry("500x500")
india_map_image = ImageTk.PhotoImage(Image.open("india.png"))

usa_map_image = ImageTk.PhotoImage(Image.open("usa.png"))

japan_map_image = ImageTk.PhotoImage(Image.open("japan.png"))

austrailia_map_image = ImageTk.PhotoImage(Image.open("clock.jpg"))

india_label = Label(root, text = "India")
india_label.place(relx = 0.25, rely = 0.05, anchor = CENTER)

india_map = Label(root)
india_map["image"] = india_map_image
india_map.place(relx = 0.25, rely = 0.1, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.25, rely = 0.5, anchor = CENTER)

usa_label = Label(root, text = "USA")
usa_label.place(relx = 0.75, rely = 0.05, anchor = CENTER)

usa_map = Label(root)
usa_map["image"] = usa_map_image
usa_map.place(relx = 0.75, rely = 0.1, anchor = CENTER)

usa_time = Label(root)
usa_time.place(relx = 0.75, rely = 0.5, anchor = CENTER)

japan_map = Label(root)
japan_map["image"] = japan_map_image
japan_map.place(relx = 0.2, rely = 0.35, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor = CENTER)


india_map = Label(root)
india_map["image"] = india_map_image
india_map.place(relx = 0.2, rely = 0.35, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor = CENTER)

class India():
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time: " + current_time
        india_time.after(100, self.times)

class USA():
    def times(self):
        home = pytz.timezone("US/Eastern")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time["text"] = "Time: " + current_time
        usa_time.after(100, self.times)
    
obj_india = India()
obj_usa = USA()
india_btn = Button(root, text = "Show Time", command = obj_india.times)
india_btn.place(relx = 0.2, rely = 0.8, anchor = CENTER)
usa_btn = Button(root, text = "Show Time", command = obj_usa.times)
usa_btn.place(relx = 0.7, rely = 0.8, anchor = CENTER)

root.mainloop()