import os

import openai


openai.api_key = os.getenv("OPENAI_APIKEY", "")

messages = [{"role": "system", "content": "You are a writer."}]


def summarize_text(text):
    message = {"role": "user", "content": f"Please summarize this text. {text}"}

    messages.append(message)

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    reply = chat.choices[0].message.content

    return reply
