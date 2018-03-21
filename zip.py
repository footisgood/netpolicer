import os
fo='d:\\'
all=os.walk(fo)
n=0
for foldername , sub , filenames in all :
    for filename in filenames :
        if filename[-3:].upper() == 'JPG':
            print (filename)
            n +=1

print ('found total %d files.'%n)

os.get