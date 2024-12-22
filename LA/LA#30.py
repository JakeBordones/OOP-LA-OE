
import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("500x400")
root.configure(bg="white")

anime_title = "Kaiju"
counter = 0
def display_text():
    global counter
    print(f"{counter} My Favorite Anime is {anime_title}")
    counter += 1

frame = tk.Frame(root)
frame.pack(pady=20)

button = tk.Button(root, text="Run", command=display_text)
button.pack(pady=10)

root.mainloop()
