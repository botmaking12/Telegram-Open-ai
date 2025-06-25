from pyrogram import Client, filters
import openai
from config import BOT_TOKEN, OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

app = Client("ai_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.private & filters.text)
async def gpt_reply(client, message):
    user_text = message.text

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_text}
            ]
        )
        reply = response.choices[0].message.content.strip()
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    await message.reply_text(reply)

app.run()
