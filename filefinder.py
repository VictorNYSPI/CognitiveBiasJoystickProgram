"""
import os

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

filepath = findfile("001_negative_ratings.txt", "C:/Users/vanos/Desktop/SURCResearch")
print(filepath)
#Above code only works for specific file path names, not keywords

#filepath = findfile("001_", "C:/Users/vanos/Desktop/SURCResearch") 
#See, code does not work for 

"""

#1-> Make sure image ratings are consistently named for patients 001 - 999 (ie for rate.html, type "001" as the patient number for Patient #1) //DONE
#2-> Do positive image ratings, put in Image Ratings folder of Assets Folder, name file (ie "001_positive_ratings.txt") //DONE
#3-> Do negative image ratings, put in Image Ratings folder of Assets Folder, name file (ie "001_negative_ratings.txt") //DONE
#4-> Create a function that loops through patient files 001-999 to find the correspinding negative image ratings and positive image ratings in Assets folder for each individual patient number
#5-> Create an (empty) file  and place in Participants Folder, name file (ie "001_images.txt") during loop through patient numbers, incorporate break in loop for already completed patient numbers
#6-> Combine the positive and negative images for a single patient number (without ratings) and write that information to the empty file in Participants Folder (ie "001_images.txt") //DONE


###############################################    Step 4 Attempt Below    ###########################################################################################


#function to find specific file paths of a specific file name within a directory

import os

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
        else:
            continue

#Function to remove some unneeded symbols from {}_positive_ratings.txt and {}_negative_ratings.txt. Will be used later once {}_positive_ratings.txt and {}_negative_ratings.txt are found through loop.
#Code taken from trialscript.py

replacables = ["{", "}", '"ratings":']
def replaceSymbols(old_string):
    for symbol in replacables:
        new_string = old_string.replace(str(symbol), "").replace(",", ",\n")
        old_string = new_string
        
    for num in range(100,0,-1):
        new_string = old_string.replace('.jpg":{}'.format(num), '.jpg"') #.replace('.jpg"00', '.jpg"')
        old_string = new_string

    return old_string


#Loop Used to find the file paths for the {}_positive_ratings.txt and {}_negative_ratings.txt. If file paths for both {}_positive_ratings.txt and {}_negative_ratings.txt are found, they are assigned
#to variables. 

for ParticipantNumber in range(0, 999, 1):
     ParticipantNumber = str(ParticipantNumber).rjust(3, '0')
     filename_positive = "{}_positive_ratings.txt".format(ParticipantNumber)
     filename_negative = "{}_negative_ratings.txt".format(ParticipantNumber)
     if (findfile(filename_positive, "C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Assets/Image Ratings")):
        filepath_positive = findfile(filename_positive, "C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Assets/Image Ratings")
        #print(filepath_positive)
     else:
        continue

     if (findfile(filename_negative, "C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Assets/Image Ratings")):
        filepath_negative = findfile(filename_negative, "C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Assets/Image Ratings")
        #print(filepath_negative)
     else:
        continue

    #if filepath_positive and filepath_negative contain the patient number for a string, then, check to see if {}_images.txt exists for that specific number in the participants file
    #if it does not exist, then create {}_images.txt in the Participants folder
    #if it does exist, skip that number iteration and continue the loop

     if ((ParticipantNumber in filepath_positive) and (ParticipantNumber in filepath_negative)):
        if (findfile("{}_images.txt".format(ParticipantNumber), "C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Participants")):
            continue
        else:
            #create a new {}_images.txt file in the Participants Folder
            new_images_file = open("C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Participants/{}_images.txt".format(ParticipantNumber), "w")

            #Use trialscript.py function
            with open (filepath_positive, "r") as p:
                old_pos = p.read()
            new_pos = replaceSymbols(old_pos)

            with open (filepath_negative, "r") as n:
                old_neg = n.read()
            new_neg = replaceSymbols(old_neg)


            combined_string = "[" + new_pos + new_neg +"]"
            final_string = combined_string.replace('][', '],\n[')
            new_images_file.write(final_string)
        
     else:
        continue












        

        
     
     
     









"""

Testing rjust() for leading zero placement https://www.delftstack.com/howto/python/python-leading-zeros/

a = [1, 10]
for num in a:
    print (str(num).rjust(2, '0'))

Leading number of leading zeros changes based on the amount of number places a number has (Which means less work!)

"""
