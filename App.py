import openai
import os
from openai import Completion
import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk


# Set up the OpenAI API client
openai.api_key = "YOUR_API_KEY"


# Create the main window
root = tk.Tk()
root.title("ChatGPT-3")        
root.geometry("500x300")
root.minsize(width=600, height=400)
#root.resizable(width=False, height=False)  #disables window resizing

root.configure(bg='sea green')
#root.attributes('-fullscreen', True)     # This will apprear window always full screen

label = tk.Label(root, text="ChatGPT GUI", bg='white',fg='black',borderwidth=2, relief="ridge", font=("Helvetica", 20, "bold"),padx=10, pady=10)
# Position the label at the top of the window
#label.place(x=5,y=2)
label.pack(side="top")


# Create a text entry field and a send button
entry = tk.Entry(root, font=('Arial', 14), bg='white', fg='black')

# Create a text widget to display the conversation
conversation = tk.Text(root, font=('Arial', 14), bg='white', fg='black')

# Create a scrollbar for the conversation widget
scrollbar = tk.Scrollbar(root, orient='vertical', command=conversation.yview)
conversation['yscrollcommand'] = scrollbar.set

# Create a function to clear the conversation widget
def clear_conversation():
    conversation.delete('1.0', 'end')

# Create a function to send a message to ChatGPT and display the response
def send_message():
    # Get the message from the entry field
    message = entry.get()

    # Clear the entry field
    entry.delete(0, "end")

    # Use the OpenAI API to get a response from ChatGPT
    response = Completion.create(
        engine="text-davinci-003",
        #engine="text-davinci-002",
        #engine="davinci",
        prompt = "Welcome to the OpenAI Chatbot! This is a conversation with ChatGPT-3, one of the most advanced language models in the world. Ask me anything and I'll do my best to provide a helpful response. To get started, simply type your message below and hit enter. I'm here to assist you with anything you need, so feel free to ask me anything you like! \nUser->"+message+"ChatGPT->",
        temperature=0.89,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["User, ChatGPT"]
    )

    # Display the message and the response in the conversation widget
    conversation.insert("end", f"User: {message}\n")
    conversation.insert("end", f"ChatGPT: {response.get('choices')[0].get('text')}\n")

# Create the send button
#send_button = tk.Button(root, text="Send", font=('Arial', 14), command=send_message, bg='white', fg='black')


send_button = tk.Button(root, 
                         text="Send", 
                         font=('Arial', 16), 
                         command=send_message, 
                         bg='white', 
                         fg='black', 
                         #width=10, 
                         #height=2, 
                         padx=3, 
                         pady=2, 
                         relief=tk.RAISED)

# Create the clear button
clear_button = tk.Button(root, text='Clear', command=clear_conversation, bg='white', fg='black')


# Create a PhotoImage object
#logo = PhotoImage(file="logo.png")                # Upload image using Tkinter PhotoImage

logo = Image.open("Logo.jpeg")                      # Upload image using PIL
logo = logo.resize((170,140), Image.BILINEAR)           # Set Size of the Logo
img = ImageTk.PhotoImage(logo)                     #convert the PIL Image object to a Tkinter PhotoImage
logo_label = Label(root, image=img, borderwidth=2, relief="sunken")                # Create a Label widget


# Pack and place the widgets into the GUI window
entry.pack()
send_button.pack()
#send_button.place(x=10,y=20)
clear_button.pack()
logo_label.place(x=1,y=2)
conversation.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

# Run the Tkinter event loop
root.mainloop()
