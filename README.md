# Toppr
A Telegram and media-processing experiment that turns a subreddit's top post into a narrated video.

## Source layout
- `bot.py` — Telegram commands, including `/sub`.
- `telerun.py` — workflow orchestration.
- `req.py` — Reddit request helpers.
- `telebot.py` — image, text-to-speech, and video-processing functions.
- `requirements.txt` — original dependencies.

## Status
Historical prototype from 2022. The source depends on the original Telegram, Reddit, MoviePy, and audio/video tooling behavior. It also expects working directories for generated assets and a configured bot token.

The scripts have not been modernized or validated as a reproducible deployment. They remain available as a record of early Python automation work.

## License
See [LICENSE](LICENSE).

[Steven Brigham / SJData](https://sjdata.net)
