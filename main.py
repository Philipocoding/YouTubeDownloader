import tkinter
import customtkinter
from pytube import YouTube 


def beginDownload():
    try:
        FinishedDownload.configure(text = "", text_color = "white")
        link = url.get()
        ytObject = YouTube(link, on_progress_callback=on_progress)
        request = ytObject.streams.get_highest_resolution()
        FinishedDownload.configure(text = "")
        request.download()
        FinishedDownload.configure(text = "Download Complete", text_color="green")
    except:
        FinishedDownload.configure(text = "Download Failed", text_color="red")

    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_complete = bytes_downloaded / total_size * 100
    per = str(int(percentage_complete))
    percentage.configure(text = per + '%')
    percentage.update()

    progressbar.set(float(percentage_complete / 100))

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")

app.title("Yt Downloader")

title = customtkinter.CTkLabel(app, text = "Insert Youtube link!")
title.pack(padx=10,pady=10)

url = tkinter.StringVar()
entry = customtkinter.CTkEntry(app, width = 400, height=30, textvariable= url)
entry.pack()

download = customtkinter.CTkButton(app,text = "Download", command = beginDownload, height = 40)
download.pack(padx = 10, pady = 15)

FinishedDownload = customtkinter.CTkLabel(app, text = "")
FinishedDownload.pack()

app.mainloop()