import tkinter as tk

def on_button_click():
    label.config(text="You clicked the button!")

root = tk.Tk()  # Create the main window
root.title("Simple Tkinter Example")
root.geometry("300x150")  # Width x Height

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)  # Add label to window with padding

button = tk.Button(root, text="Click me", command=on_button_click)
button.pack(pady=10)

root.mainloop()  # Start the GUI event loop

