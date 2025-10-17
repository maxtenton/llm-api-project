from dotenv import load_dotenv
from google import genai
from google.genai import types
from SampleReader import ReadFile, WriteOutput
import os

load_dotenv()
Key = os.environ["API_KEY"]
print(os.listdir("sample_inputs"))

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
    WriteOutput(f"cv{num}.json", response.text)
    MDresponse = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Make this JSON file into md file : {response} Only output md file content. No other markdown syntax needed.",
        config=types.GenerateContentConfig(
            temperature=0.2
        )
    )
    WriteOutput(f"cv{num}.md", MDresponse.text)


with open("sample_inputs/jd.txt", "r", encoding="utf-8") as file:
    global JD
    JD = file.read()

for i in range(1, 4):
    CheckCV(ReadFile(f"cv{i}.txt"), i)

