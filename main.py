from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
import shutil


def download():
    videoPath = urlEntry.get()  # Video source
    filePath = pathLabel.cget("text")  # Video destination
    print("Downloading......")
    mp4 = YouTube(videoPath).streams.get_highest_resolution().download()  # Download video
    videoClip = VideoFileClip(mp4)  # Convert to video file
    # Code for mp3
    audioFile = videoClip.audio
    audioFile.write_audiofile("Audio.mp3")
    audioFile.close()
    shutil.move("Audio.mp3", filePath)
    # Code for mp3
    videoClip.close()
    shutil.move(mp4, filePath)
    print("Download Complete")


def getPath():
    path = filedialog.askdirectory()  # Get the target folder path on PC
    pathLabel.config(text=path)  # Change path Label text to directory path

root = Tk()
root.title("Video Downloader")
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# App Label
appLabel = Label(root, text="Video Downloader", fg='blue', font=('Arial', 20))
canvas.create_window(200, 20, window=appLabel)

# Entry to accept video URL
urlLabel = Label(root, text="Enter video URL", fg='blue', font=('Arial', 10))
urlEntry = Entry(root, width=50)
canvas.create_window(200, 80, window=urlLabel)
canvas.create_window(200, 100, window=urlEntry)

# Path to download videos
pathLabel = Label(root, text="Select path to Download", fg='blue', font=('Arial', 10))
pathButton = Button(root, text="Select", command=getPath)
canvas.create_window(200, 150, window=pathLabel)
canvas.create_window(200, 170, window=pathButton)

# Download button
downloadButton = Button(root, text="Download", command=download)
canvas.create_window(200, 250, window=downloadButton)

root.mainloop()
