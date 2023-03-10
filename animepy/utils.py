import re, typing, aiohttp

async def Request(url: str, params: dict = {}, headers: dict = {}, like: str = 'json'):
    try:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(url=url, params=params) as r:
                if r.status != 200 and r.status != 201:
                    return None
                if like.lower() == 'json':
                    return await r.json()
                elif like.lower() == 'text':
                    return await r.text()
                elif like.lower() == 'read':
                    return await r.read()
                else:
                    raise SyntaxError('Invalid like method provided in request')
    except:
        return None

def camel_to_snake(s) -> str:
    return re.sub("([A-Z]\w+$)", "_\\1", s).lower()

def to_snake(d) -> typing.Union[dict, list]:
    """
    Converts a dict or list to snake case from camel case
    """
    if isinstance(d, list):
        return [to_snake(i) if isinstance(i, (dict, list)) else i for i in d]
    return {
        camel_to_snake(a): to_snake(b) if isinstance(b, (dict, list)) else b
        for a, b in d.items()
    }
    