from openai import OpenAI


client = OpenAI(
    api_key="Venom",
    base_url="https://venom-ai-apis.vercel.app"
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": '''Hi''',

        },

    ],
    model="gemini-2.5-flash",
)

 
print(chat_completion.choices[0].message.content)
