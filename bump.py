import requests
import time

l = [
    ["토큰", "818676562949308438"],
    ["토큰", "818676562949308438"],
    ["토큰", "818676562949308438"]
]

while True:
    for i in l:
        try:
            requests.post("https://discord.com/api/v8/channels/" + i[1] + "/messages", json={"content": "!d bump"}, headers={
                "Authorization": i[0], "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15"})
        except:
            pass
    time.sleep(7210)
