#pylint: disable=missing-docstring
#pylint: disable=unspecified-encoding
import tracemalloc
import os
import discord

tracemalloc.start()




#Some fuctions in this class use 'await' so that other tasks
# can be excuted in the background while the function completes
#~/1.Repos/sxv-projects/Managers/NotificationManager/

class MyClient(discord.Client):

    def __init__(self):
        self.instents = discord.Intents.default()
        super().__init__(intents=self.instents)

        self.TOKEN = self.get_token_id()
        self.CHANNEL_ID = self.get_channel_id()
        self.USER_ID = self.get_user_id()

        self.user_message = None
        self.channel_message = None

    def get_token_id(self):
        result = os.environ.get('DISCORD_TOKEN_ID')
        return result

    def get_channel_id(self):
        result = os.environ.get('DISCORD_CHANNEL_ID')
        return result

    def get_user_id(self):
        result = os.environ.get('DISCORD_USER_ID')
        return result


    async def on_ready(self):
        print(f'Logged in as {self.user}')
        if self.user_message:
            await self.send_user_message(self.user_message)
        elif self.channel_message:
            await self.send_channel_message(self.channel_message)

    async def send_channel_message(self, message='Empty Message', channel_id=''):
        #print(f'Logged in as {self.user}')
        try:
            if not channel_id:
                channel_id = self.CHANNEL_ID
            channel = await self.fetch_channel(channel_id)
            if channel:
                await channel.send(message)
            else:
                print(f"Channel with ID {channel_id} does not exist.")
            await self.close()  # Close the bot after sending the message
        except discord.Forbidden:
            print("Bot lacks permission to send messages in the target channel.")
        except discord.NotFound:
            print(f"Channel with ID {self.CHANNEL_ID} does not exist.")
        except discord.HTTPException as hexc:
            print(f"Failed to send message due to an HTTP exception: {hexc}")

    #user
    async def send_user_message(self, message='Empty Message', user_id=''):
        #print(f'Logged in as {self.user}')
        if not user_id:
            user_id = self.USER_ID
        user = await self.fetch_user(user_id)
        if user:
            await user.send(message)
        await self.close()  # Close the bot after sending the message

if __name__ == "__main__":

    test_client = MyClient()
    test_client.user_message = 'TEST'
    test_client.run(test_client.TOKEN)
