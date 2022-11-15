import pymongo
import pro1

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client.project        #project is the database name 
mycol = db.links           #links is the collection name (table name in sql)
print(db.mycol)
while True:
    print("enter 1:If you want to increase playlist")
    print("enter 2:If you want to delete a link")
    print("enter 3:If you want to replace a link")
    print("enter 4:If you want to view all the links")
    print("any number other than 1-4 to play a random video")
    h = int(input("enter ur choice:"))
    if h == 1:
        b = int(input("how many you want to insert?"))
        for i in range(b):
            lin = input("insert link")
            db.links.insert_one({'ytname':lin})
        print("inserted")
    elif h == 2:
        dels = int(input("how many"))
        for i in range(dels):
            ent=int(input("enter the id to delete"))
            db.links.delete_one({'ytname':ent})
        print("deleted")
    elif h == 3:
        rep = int(input("how many"))
        for i in range(rep):
            first_link = input("enter link you want to replace")
            second_link = input("enter replacing link")
            db.links.find_one_and_replace({'ytname':first_link},{'ytname':second_link},upsert=True)
        print("replaced")
    elif h==4:
        g=db.links.find({},{"_id":0})
        for i in g:
            print(i)
    else:
        print("want to listen to a random song")
        pro1.main()   #this takes us to the other python file (it act as a module)
        break