from tkinter import *
import pyshorteners
import clipboard
from tkinter import messagebox

window = Tk()

window.geometry("525x680")  # width x height

# make window non-resizable
window.resizable(False, False)  # non-resizable in x and y

# app title
window.title("HaloURL Shortener")

window.configure(background='#1e3d59')

heading_label = Label(window, text="HaloURL", font=("Montserrat", "24", "bold"), fg="#ff6e40", bg="#1e3d59")
heading_label.grid(row=1, column=6, pady=16)

window.iconbitmap('C:/Users/Rushil/PycharmProjects/Halo_URLShortener/HaloIcon.ico')

Halo_Logo = PhotoImage(file="Logo8.PNG")
Logo_label = Label(window, image=Halo_Logo)
Logo_label.grid(row=14, column=6)

# url entry
url_input = Entry(window, font=("Helvetica", "16"), bg="#1e3d59", fg="white")
url_input.insert(0, "Enter a valid URL")
url_input.grid(row=15, column=6, pady=6)

# label shortened url
str_url = StringVar(window)

shortened_url = Label(window, textvariable=str_url, font=("Trebuchet MS", "16"), fg="#ff6e40", bg="#1e3d59")
shortened_url.grid(row=16, column=6, pady=6)


# copy url function
def copy_short_url():
    try:
        clipboard.copy(str_url.get())
        print("URL copied successfully, you're good to go!")
    except:
        str_url.set("Something wrong, try again")


# Copy url button
copy_btn = Button(window, text="Copy!", bg="#1e3d59", fg="#ff6e40", font=("Montserrat", "12", "bold"),
                  command=copy_short_url)
copy_btn.grid(row=16, column=5, pady=10, padx=12)


# short url function
def short_url():
    try:
        s = pyshorteners.Shortener()
        url = url_input.get()
        final_result = s.tinyurl.short(url)
        str_url.set(final_result)
        url_input.delete(0, END)  # clear input
    except:
        str_url.set("Enter the URL ")


# button to shorten url
btn = Button(window, text=" Shorten!", padx=8, pady=4, bg="#1e3d59", fg="#ff6e40", font=("Montserrat", "16"),
             activebackground="#fff", command=short_url, relief=RAISED)

btn.grid(row=15, column=5, pady=6)

text_label = Label(window, text='''Why HaloURL Shortener?

Tired of pasting long URLs?
Creating, Shortening & Sharing links should always be easy.
HaloURL helps you shorten your lengthy links to tiny URLs that are easier to manage.
Also, these shortened links will never break or expire.
''', font=("Trebuchet MS", "16"), fg="#2E4053", bg="#3498DB")

quit_btn = Button(window, text="EXIT", bg="#1e3d59", fg="#ff6e40", font=("Montserrat", "20", "bold"),
                  command=window.quit)
quit_btn.grid(row=19, column=6, pady=5)


def popup():
    messagebox.showinfo("Why HaloURL Shortener?", '''Tired of pasting long URLs?
Creating, Shortening & Sharing links should always be easy.

HaloURL helps you shorten your lengthy links to tiny URLs that are easier to manage.
Also, these shortened links will never break or expire. ''')


info_btn = Button(window, text="Why HaloURL?", command=popup, bg="#1e3d59", fg="#ff6e40", font=("Montserrat", "22"))
info_btn.grid(row=18, column=6, padx=4, pady=8)

window.mainloop()