import os
import pygame
from tkinter import *
from tkinter import filedialog

# Initialize pygame mixer
pygame.mixer.init()

# Main window
root = Tk()
root.title("🎵 CodeClause Music Player")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f0f0f0")  # light gray background

playlist = []
current_song = 0
paused = False

# Functions
def load_music():
    global playlist
    folder = filedialog.askdirectory()
    if folder:
        playlist = []
        song_listbox.delete(0, END)
        for file in os.listdir(folder):
            if file.endswith(".mp3"):
                playlist.append(os.path.join(folder, file))
                song_listbox.insert(END, os.path.basename(file))
        if playlist:
            status_label.config(text=f"🎵 Loaded {len(playlist)} songs")
        else:
            status_label.config(text="⚠️ No MP3 files found")

def play_music():
    global paused
    if not playlist:
        status_label.config(text="⚠️ Load music first")
        return
    global current_song
    selected = song_listbox.curselection()
    if selected:
        current_song = selected[0]
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()
    paused = False
    status_label.config(text=f"▶ Playing: {os.path.basename(playlist[current_song])}")
    song_listbox.selection_clear(0, END)
    song_listbox.selection_set(current_song)

def pause_music():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
        status_label.config(text="⏸ Paused")
    else:
        pygame.mixer.music.unpause()
        paused = False
        status_label.config(text="▶ Resumed")

def stop_music():
    pygame.mixer.music.stop()
    status_label.config(text="⏹ Stopped")

# Frames
button_frame = Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

listbox_frame = Frame(root, bg="#f0f0f0")
listbox_frame.pack(pady=10)

# Buttons
Button(button_frame, text="Load Folder", width=15, command=load_music, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="Play", width=15, command=play_music, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5, pady=5)
Button(button_frame, text="Pause / Resume", width=15, command=pause_music, bg="#FFC107", fg="black").grid(row=1, column=0, padx=5, pady=5)
Button(button_frame, text="Stop", width=15, command=stop_music, bg="#F44336", fg="white").grid(row=1, column=1, padx=5, pady=5)

# Listbox to show songs
song_listbox = Listbox(listbox_frame, width=60, height=10, bg="white", fg="black", selectbackground="#2196F3")
song_listbox.pack()

# Status label
status_label = Label(root, text="🎶 Welcome to Music Player", bg="#f0f0f0", font=("Helvetica", 10))
status_label.pack(pady=10)

# Run app
root.mainloop()
