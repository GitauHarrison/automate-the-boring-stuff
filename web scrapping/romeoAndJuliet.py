import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunck in res.iter_contents(100000):
    playFile.write(chunck)

playFile.close()