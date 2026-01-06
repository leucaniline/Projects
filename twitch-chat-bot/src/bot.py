import os
import asyncio
from twitchio.ext import commands
from parser import ChatParser
from responder import ChatResponder
from config import CHANNEL, TOKEN


class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix="!", initial_channels=[CHANNEL])
        self.parser = ChatParser()
        self.responder = ChatResponder()
        self.user_message_counts = {}
        self.message_window = []
        self.window_duration = 900  # 15 minutes in seconds
        self.window_task = None

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        if not self.window_task:
            self.window_task = asyncio.create_task(self.window_manager())

    async def event_message(self, message):
        if message.author.name.lower() == self.nick.lower():
            return

        parsed_data = self.parser.parse_message(message.content)
        if parsed_data:
            # Count the message for the user in the current window
            user = message.author.name.lower()
            msg = message.content
            self.message_window.append((user, msg, asyncio.get_event_loop().time()))

            if user not in self.user_message_counts:
                self.user_message_counts[user] = {}
            if msg not in self.user_message_counts[user]:
                self.user_message_counts[user][msg] = 0
            self.user_message_counts[user][msg] += 1

            response = self.responder.send_response(message.channel.name, parsed_data)
            if response:
                await message.channel.send(response)

    async def window_manager(self):
        while True:
            await asyncio.sleep(self.window_duration)
            # Remove messages outside the window
            now = asyncio.get_event_loop().time()
            self.message_window = [
                (user, msg, t)
                for (user, msg, t) in self.message_window
                if now - t <= self.window_duration
            ]
            # Count messages per user in the window
            user_counts = {}
            for user, _, _ in self.message_window:
                user_counts[user] = user_counts.get(user, 0) + 1
            if user_counts:
                top_user = max(user_counts, key=user_counts.get)
                count = user_counts[top_user]
                message = f"User '{top_user}' sent the most messages with the keyword in the last 5 minutes: {count} messages."
                # Send to all channels the bot is in
                for channel in self.connected_channels:
                    await channel.send(message)


if __name__ == "__main__":
    bot = Bot()
    bot.run()
