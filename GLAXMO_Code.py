from tkinter import *
from tkinter import PhotoImage
import google.generativeai as genai

genai.configure(api_key="your api key")
model = genai.GenerativeModel('gemini-2.0-flash')


root = Tk()
root.geometry("520x400")
root.configure(background='#f4e7e2')
root.resizable(False, False)
root.title("GLAXMO")


logo = PhotoImage(file="Path to logo")  
# Set the window's icon to the logo
root.iconphoto(False, logo)

canvas = Canvas(root, bg="#f4e7e2", width=500, height=400)
canvas.config(highlightthickness=0, borderwidth=0)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollable_frame = Frame(canvas, bg="#f4e7e2")

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

y_offset = 10
command_labels = []

def on_key_release(event):
    global y_offset
    entry = event.widget

    p = entry.get("1.0", "end-1c")
    entry.config(state="normal")  
    entry.config(bg="#f4e7e2")
    entry.config(state="disabled")

    
    prompt = f"""
    Generate response to this.{p}. make sure 2 not answers questions which aren't student related,
    or related to future career choices. If u are given one which isn't, simply say 'Sorry, I wasn't built to answer such questions.'
    Also try not 2 make it 2 long, they shold be long enuf, but not 2 long 2 bor some1 out. ok?
    P.S: JUST GIVE ME THE TEXT, NOTHING ELSE!!!!!!!!!!!!!!!! AND DON'T MAKE ANY TEXT IN BOLD, ITALIC, JUST NORMAL!!!!!!!!
    """

    answer = model.generate_content([prompt], stream=False)
    response = answer.text.strip()
    Label(scrollable_frame, text=f"{response}", bg='#f4e7e2', font=("Courier", 11), justify=LEFT, wraplength=500).pack(anchor=W, padx=10, pady=2)

    add_command_line()
    canvas.yview_moveto(1)

def add_command_line():
    frame = Frame(scrollable_frame, bg="#f4e7e2", width=100, height =50)
    frame.pack(anchor=W, padx=8, pady=10)
    Label(frame, text="- Next Question: ", font=("Courier", 11), bg='#f4e7e2').pack(side=LEFT)

    # Create a Text widget instead of Entry for better control
    entry = Text(frame, font=("Courier", 11), bg="#f4e7e2", bd=0, highlightthickness=0,  height=1, width=38, wrap='word')
    entry.pack(side=LEFT, fill=X, expand=True)
    entry.bind("<Return>", on_key_release)
    entry.focus_set()
    
    command_labels.append(frame)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack canvas and scrollbar
canvas.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.pack(side=RIGHT, fill=Y)

label = Label(scrollable_frame, text='- Hi, I am GLAXMO! A bot built to help in your ever-so\nstressful life as a student. What questions would\nu like to ask me?',font=("Courier", 11), justify=LEFT, bg='#f4e7e2')
label.pack(anchor=W, padx=10, pady=5)

entry = Text(scrollable_frame, font=("Courier", 11), bg='#f4e7e2', insertbackground="black", bd=0, highlightthickness=0,  height=2, width=52, wrap='word')
entry.pack(anchor=W, padx=10, pady=5)
entry.focus_set()
entry.bind("<Return>", on_key_release)



root.mainloop()