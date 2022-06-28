#REQUIRED!!
#Read the README.md file prior to starting rate.html or replacing file directory paths in this code.

import os

#Function that searches for files with specific names in a given folder
def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)
        else:
            continue



#Function to remove some unneeded symbols from {}_positive_ratings.txt and {}_negative_ratings.txt. Will be used later once {}_positive_ratings.txt and {}_negative_ratings.txt are found through loop.

replacables = ["{", "}", '"ratings":']
def replaceSymbols(old_string):
    for symbol in replacables:
        new_string = old_string.replace(str(symbol), "").replace(",", ",\n")
        old_string = new_string
        
    for num in range(100,0,-1):
        new_string = old_string.replace('.jpg":{}'.format(num), '.jpg"') 
        old_string = new_string

    return old_string


#Loop Used to find the file paths for the {}_positive_ratings.txt and {}_negative_ratings.txt. If file paths for both {}_positive_ratings.txt and {}_negative_ratings.txt are found, they are assigned
#to variables. 

for ParticipantNumber in range(0, 999, 1):
     ParticipantNumber = str(ParticipantNumber).rjust(3, '0')
     filename_positive = "{}_positive_ratings.txt".format(ParticipantNumber)
     filename_negative = "{}_negative_ratings.txt".format(ParticipantNumber)
     if (findfile(filename_positive, "")): ###Image Ratings Folder File Path###
        filepath_positive = findfile(filename_positive, "") ###Image Ratings Folder File Path###
        
     else:
        continue

     if (findfile(filename_negative, "")):  ###Image Ratings Folder File Path###
        filepath_negative = findfile(filename_negative, "")  ###Image Ratings Folder File Path###
        
     else:
        continue

    #if filepath_positive and filepath_negative contain the patient number for a string, then, check to see if {}_images.txt exists for that specific number in the participants file
    #if it does not exist, then create {}_images.txt in the Participants folder
    #if it does exist, skip that number iteration and continue the loop

     if ((ParticipantNumber in filepath_positive) and (ParticipantNumber in filepath_negative)):
        if (findfile("{}_images.txt".format(ParticipantNumber), "")): ###Participants Folder File Path###
            continue
        else:
            #create a new {}_images.txt file in the Participants Folder
            new_images_file = open(" /{}_images.txt".format(ParticipantNumber), "w") ###Participants Folder File Path IN FRONT OF /{}_images.txt###

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


