# Anime.py
The best package in Python to get anime information and anime gifs!

## Installation:
```
pip install anime.py
```

## Example Usage:
```py
```py
```py
```py
import asyncio

from animepy import (
    AnimeGif, AnimeSearch,
    SfwGif, SearchType
)

gif_res = AnimeGif(
    bucket=SfwGif.KISS,
    as_dict=True
)

search_res = asyncio.run(
    AnimeSearch(
        query="Naruto Shippuuden",
        type=SearchType.ANIME
    )
)

print(gif_res) # Anime Gif Result

print(search_res[0]["attributes"]["titles"]) # Anime Search Result```
