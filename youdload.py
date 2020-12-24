y("hello world")
print(y)
t("Youdload tool is an Arabic tool for downloading videos from YouTube created by the young engineer 'Youssef Al-Mayani'")
print(t)
from pafy import new
url = input('enter your link here: ')
video = new(url)
stream = video.streams
dl = video.getbest()
dl.download()
