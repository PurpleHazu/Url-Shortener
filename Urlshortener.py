import pyperclip   
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("250x200", )
root.resizable(False, False)
root.title("Url Shortener")
root.configure(bg="#49A")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)
    
def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)
    
Label(root, text="Url Shortener").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short Url", command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command= copyurl).pack(pady=5)
root.mainloop()