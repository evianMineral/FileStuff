import simplejson as json
import os


if os.path.isfile("FileStuff/StuffFile/ages.json") and os.stat("FileStuff/StuffFile/ages.json").st_size !=0:
    old_file = open("FileStuff/StuffFile/ages.json", "r+")
    data = json.loads(old_file.read())
    print("current age is", data["age"], "--adding a year.")
    data["age"] = data["age"] + 1
    print("new age is ", data["age"])
else:
    old_file = open("FileStuff/StuffFile/ages.json", "w+")
    data = {"name" : "Nick", "age" : 27}
    print("no file found, settin default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))






# newfile = open("FileStuff\\StuffFile\\newFile.txt","w+")

# string = "this is the content will be wrtitten to the text file"

# newfile.write(string)