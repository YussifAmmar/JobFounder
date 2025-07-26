import demo
import customtkinter as ctk
from tkinter import messagebox

def find_clicked(job_title,location):
    title = job_title.get()
    loc = location.get()
    demo.scrape_jobs(title,loc)
    messagebox.showinfo("Done", f"✅ Jobs offers for {title} saved in Jobs.csv!")
    

def toggle_mode():
    if switch.get() == 0:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

app = ctk.CTk()
app.title("Linkedin ML Jobs")

warning = ctk.CTkLabel(
    app,
    text="Make sure your JSON file is named: cookies.json",
    text_color="#FFA500",
    font=ctk.CTkFont(size=12, weight="bold", family="Arial")
)
warning.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="n")


job_title = ctk.CTkEntry(app, placeholder_text="Job Title")
JobTitle= job_title.get()
job_title.grid(row=1, column=0, padx=20, pady=20)

location = ctk.CTkEntry(app, placeholder_text="Job Location")
Location=location.get()
location.grid(row=1, column=1, padx=20, pady=20)


Find_button = ctk.CTkButton(app, text="Find Now", command= lambda : find_clicked(job_title,location))
Find_button.grid(row=2, column=0, columnspan=2, pady=10)

switch = ctk.CTkSwitch(app, text="Light Mode", command=toggle_mode)
switch.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()