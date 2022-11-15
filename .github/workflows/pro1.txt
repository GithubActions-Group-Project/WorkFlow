import random  #generates a random link in my program
import pymongo
import pafy  #used to load the content of the yt video into a variable
import vlc   #used to play the video
from time import sleep

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.project
def main():                                 #used to run when called
    c = db.links.find({},{"ytname":1})   #finds all the values of the ytname key (using projection)
    link2=[]                #creating empty list
    for i in c:
        link2.append(i['ytname'])
    url=random.choice(link2)
    print(url)
    video=pafy.new(url)          #loads the content of url into video var(pafy object)
    best=video.getbest()          #gives the best quality of video (method)
    media=vlc.MediaPlayer(best.url)      #creating vlc object
    media.play()                      #starts playing video
    sleep(5) #  however long you expect it to take to open vlc
    while media.is_playing():
        sleep(5)       #after playing the time taken to close
    #while True:
     #   pass
if __name__ == "__main__":
    main()                 #this is used to not run the program when it is imported(calling the function)