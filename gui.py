import google.generativeai as genai
import os
import customtkinter as ctk

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-3.6-flash")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Shinzo")
app.geometry("500x600")

chat_box = ctk.CTkTextbox(app, width=460, height=480)
chat_box.pack(padx=20, pady=20)
chat_box.configure(state="disabled")

entry = ctk.CTkEntry(app, width=350, placeholder_text="Type your message...")
entry.pack(side="left", padx=(20, 10), pady=10)
entry.bind("<Return>", lambda event: send_message())

def send_message():
    user_text = entry.get()
    if user_text.strip() == "":
        return

    chat_box.configure(state="normal")
    chat_box.insert("end", "Master: " + user_text + "\n")
    entry.delete(0, "end")
    chat_box.see("end")
    app.update()

    chat_box.configure(state="normal")
    chat_box.insert("end", "Shinzo is typing...\n")
    chat_box.configure(state="disabled")
    chat_box.see("end")
    app.update()

    response = model.generate_content(user_text)
    chat_box.insert("end", "Shinzo: " + response.text + "\n\n")
    chat_box.configure(state="disabled")
    chat_box.see("end")

send_button = ctk.CTkButton(app, text="Send", command=send_message)
send_button.pack(side="left", padx=(0, 20), pady=10)

app.mainloop()

