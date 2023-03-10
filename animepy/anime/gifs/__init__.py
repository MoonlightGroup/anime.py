





class AnimeGif:
    
    
    def nsfw(self, bucket: NSFW, with_info: typing.Optional[bool] = True):
        path = f"animepy/anime/gifs/nsfw/{bucket.value}.json"
        with open(path) as Json:
            data = json.load(Json)
        return random.choice(data) if with_info else random.choice(data)["url"]
