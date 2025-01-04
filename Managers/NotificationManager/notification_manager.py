#pylint: disable=missing-docstring
#pylint: disable=unspecified-encoding
import tracemalloc
import discord

tracemalloc.start()


def get_token_id():
    with open('discord_token_id.txt', 'r') as token_file: # bot's token
        return token_file.read()

def get_channel_id():
    with open('discord_channel_id.txt', 'r') as channel_file: # Target chanel
        return channel_file.read()

def get_user_id():
    with open('discord_user_id.txt', 'r') as user_file: #Target user
        return user_file.read()

#Some fuctions in this class use 'await' so that other tasks
# can be excuted in the background while the function completes
#~/1.Repos/sxv-projects/Managers/NotificationManager/

class MyClient(discord.Client):

    TOKEN = get_token_id()
    CHANNEL_ID = get_channel_id()
    USER_ID = get_user_id()

    async def send_channel_message(self, message='Empty Message', channel_id=CHANNEL_ID):
        #print(f'Logged in as {self.user}')
        channel = self.get_channel(channel_id)
        if channel:
            await channel.send(message)
        await self.close()  # Close the bot after sending the message

    #user
    async def send_user_message(self, message='Empty Message', user_id=USER_ID):
        #print(f'Logged in as {self.user}')
        user = await self.fetch_user(user_id)
        if user:
            await user.send(message)
        await self.close()  # Close the bot after sending the message

if __name__ == "__main__":
    test_client = MyClient(intents=discord.Intents.default())
    test_client.run(get_token_id())

    test_client.send_user_message('Test message sent by Raspberry Pi via Notification Manager')
    test_client.send_channel_message('Test message sent by Raspberry Pi via Notification Manager')
    