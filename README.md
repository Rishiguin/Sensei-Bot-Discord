# Simple discord music discord bot
This bot was made with python (3.8.0) and discord.py@rewrite. It includes:
- Chat commands (!poke, !clear, !roll, !toss, !help, !poll, !meme)
- Music commands (!join, !skip, !pause, !play, !remove)

# About the music module
This bot includes :
- A youtube videos support (even ones from public playlists)
- A queue system (per server queue, add and remove songs from queue)
- A youtube search system (search from links or key-words)
- A pretty message system (automatic current song display and deletion)

# About the twitch command:
It allows you to search streams according to their game and title.<br>
To use it, you **must** follow those steps:
- Create a new [twitch app](https://dev.twitch.tv/console)
- Create a [OAuth token](https://dev.twitch.tv/docs/authentication/getting-tokens-oauth/)
- Change [those lines](https://github.com/MrSpaar/discord-bot/blob/master/cogs/chat.py#L54-L55) with you client-id and token

# Libraries' version:
- discord.py → 1.3.4
- discord → 1.0.1
- youtube-dl → 2020.6.16.1
- async-timeout → 3.0.1
- lxml → 4.5.1
- PyNaCl → 1.4.0
- wheel → 0.34.2
- websockets → 8.1
- FFmpeg → 4.2.3

Add FFmpeg to path when you download it (https://www.youtube.com/watch?v=a_KqycyErd8).
