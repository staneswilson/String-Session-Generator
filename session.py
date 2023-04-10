from pyrogram import Client

#Recieving api_id and api_hash to create a session.
api_id=input("Enter the API ID: ")
api_hash=input("Enter API HASH: ")

#generating session
app = Client("my_account",api_id=api_id, api_hash=api_hash, in_memory=True)

string_session = ""

#To export String Session and send to saved messages.
async def main():
    async with app:
        string_session = await app.export_session_string()
        print(string_session)
        await app.send_message("me", f"**Here is Your Session:-**\n\n<code>{string_session}</code>")

app.run(main())