import datetime

x = datetime.datetime.today()
day=x.strftime("%d")
month=x.strftime("%B")
year=x.strftime("%Y")
date = day+"_"+month+"_"+year
print(x.strftime("%x")) 
print(date)


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "a")
f.write("\n")
f.write("Now the file has more content! AGAIN2")
f.close()