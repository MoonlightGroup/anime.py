from pprint import pp
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

pp(gif_res)
pp(search_res[0]["attributes"]["titles"])