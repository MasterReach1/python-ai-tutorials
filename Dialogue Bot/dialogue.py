from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
barkeepDialogueCompletion = [{"role": "system",
             "content": "You are a jolly barkeep at the Pig's Toe in the town of Jarlsburg speaking to a wandering adventurer."}]

while True:
    user_input = input("What do you want to say? >> ")
    barkeepDialogueCompletion.append({"role": "user",
                                     "content": user_input})
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=barkeepDialogueCompletion
    )

    barkeepDialogueCompletion.append({"role": "assistant",
                                     "content": completion.choices[0].message.content})
    
    print(completion.choices[0].message.content + "\n\n")