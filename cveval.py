from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

load_dotenv()
Key = os.environ["API_KEY"]

client = genai.Client(api_key=Key)
prompt = open("prompt.md", "r", encoding='utf-8').read()

def CheckCV(CV = "", num = 0):
    global client
    global JD
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{JD}{prompt}{CV}",
        config=types.GenerateContentConfig(
            temperature=0.2
        )
    )
    with open(f"/output/cv{num}.json", "w", encoding="utf-8") as file:
        file.write(response)
    MDresponse = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Make this JSON file into md file : {response}",
        config=types.GenerateContentConfig(
            temperature=0.2
        )
    )
    with open(f"/output/cv{num}.md", "w", encoding="utf-8") as file:
        file.write(MDresponse)


with open("/sample_inputs/jd.txt", "r", encoding="utf-8") as file:
    global JD
    JD = file.read()

for i in range(1, 3):
    with open(f"/sample_input/cv{i}.txt", "r") as file:
        CheckCV(CV = file.read(), num = i)

