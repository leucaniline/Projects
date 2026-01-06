class ChatParser:
    def __init__(self, keywords):
        self.keywords = keywords

    def parse_message(self, message: str):
        message_lower = message.lower()
        found_keywords = [keyword for keyword in self.keywords if keyword in message_lower]
        return found_keywords if found_keywords else None