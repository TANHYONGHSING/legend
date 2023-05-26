#Tan Hyong Hsing
#20DDT21F1002

time = int(input("Please insert the time in seconds\n"))
minutes= time / 60
# or : minutes= time // 60 (dia ambik int je x ambik poin)
seconds = time % 60
print(int(minutes) , "minutes" , int(seconds) , "seconds") 
