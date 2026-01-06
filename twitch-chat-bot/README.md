# Twitch Chat Bot

This project is a Python-based bot designed to read and parse Twitch chat messages, looking for specific keywords and responding accordingly.

## Project Structure

```
twitch-chat-bot
├── src
│   ├── bot.py          # Main entry point for the bot
│   ├── parser.py       # Contains the ChatParser class for message parsing
│   ├── responder.py     # Contains the ChatResponder class for sending responses
│   └── config.py       # Configuration settings for the bot
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Setup Instructions

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/twitch-chat-bot.git
   cd twitch-chat-bot
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Configure your Twitch API credentials and settings in `src/config.py`.

## Usage

To run the bot, execute the following command:

```
python src/bot.py
```

## Functionality

- The bot connects to a specified Twitch channel and listens for chat messages.
- It uses the `ChatParser` class to analyze incoming messages for specific keywords.
- Based on the parsed information, the `ChatResponder` class sends appropriate responses back to the chat.

## Acknowledgement

Artificial Intelligence was used in the creation of this tool.
