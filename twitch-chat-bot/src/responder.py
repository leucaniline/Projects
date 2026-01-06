class ChatResponder:
    def __init__(self, bot):
        self.bot = bot

    async def send_response(self, channel: str, message: str):
        await self.bot.send_message(channel, message)
