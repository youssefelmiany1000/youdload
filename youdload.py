from pafy import new
url = input('enter your link here: ')
video = new(url)
stream = video.streams
dl = video.getbest()
dl.download()
