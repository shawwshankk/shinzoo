import google.generativeai as genai
import os
import asyncio
import edge_tts

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-3.6-flash")

async def bolo(text):
    voice = "en-IN-PrabhatNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("output.mp3")
    os.system("mpg123 output.mp3")

print("Shinzo activate ho gaya! (bahar nikalne ke liye 'exit' likho)")

while True:
    user_input = input("Master: ")
    if user_input.lower() == "exit":
        print("Shinzo: Bye bye!")
        asyncio.run(bolo("Bye bye!"))
        break
    response = model.generate_content(user_input)
    print("Shinzo:", response.text)
    asyncio.run(bolo(response.text))
