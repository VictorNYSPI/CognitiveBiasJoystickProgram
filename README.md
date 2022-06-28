# CognitiveBiasJoystickProgram
This contains the python script "filefinder.py". "filefinder.py" will be used for the Cognitive Bias Project. To use "filefinder.py", rate.html must be completed. The files generated from this script can be used for abm.html and aat.html
READ THIS ENTIRE PAGE BEFORE RUNNING filefinder.py TO AVOID ISSUES!


1. Naming of Positive and Negative Rating Files Downloaded after Completion of rate.html 

All positive rating tests and negative rating tests that are downloaded after the rate.html session is completed must have a three digit number, the word "positive" or "negative" and "ratings", and underscores in their naming conventions. 
Example: "001_positive_ratings.txt" or "025_negative_ratings.txt"
Each participant (ie 001) must complete both a positive ratings test and negative ratings test.
Once named, these files must be put in the user designated Image Ratings Folder (see 2.)
Failure to name these files correctly and failure to have both a negative and positive file for each participant prior to running filefinder.py  will cause the script to fail or cause issues.


2. The Image Ratings Folder and Participant Folder

There are two File Directory Location Paths that need to be kept in mind. These are the Image Ratings Folder and the Participants Folder.

The Image Ratings Folder holds the positive ratings files and negative ratings files (ie "001_positive_ratings.txt" or "025_negative_ratings.txt") once these files are generated from the completion of rate.html.
MAKE SURE THAT AFTER rate.html IS COMPLETED, THE FILES YOU ARE PROMPTED TO DOWNLOAD ARE NAMED CORRECTLY (see 1.) AND PLACED IN THE IMAGE RATINGS FOLDER PRIOR TO RUNNING filefinder.py.
Failure to place those files in the Image Ratings Folder prior to running filefinder.py  will cause the script to fail or cause issues.


The Participants Folder holds the files that have the top ten highly rated positive images and top ten highly rated negative images for a specific participant, without the actual rating number of each picture listed. 
The files in the Participant Folder are named like this example: "001_images.txt"
The purpose of filefinder.py is to generate files in the Participant folder for every participant that completed both the positive ratings test and negative ratings test for rate.html. 
Therefore the Participant Folder should remain untouched.


3.Folder Paths
Once you are sure that the files downloaded after rate.html are named correctly (see 1.), that each participant has a positive ratings file and a negative ratings file (see 1.), and all these files are in the Image Ratings Folder (see 2.), all that is left is to paste the folder directory path of these folders to their corresponding locations in filefinder.py 
On your computer, find the full file path for the Image Ratings Folder and copy and paste it into the " " in filefinder.py  wherever you see ###Image Ratings Folder File Path###. In filefinder.py, it should look similiar this:
"C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Assets/Image Ratings"

On your computer, find the full file path for the Participants Folder and copy and paste it into the " " in filefinder.py wherever you see ###Participants Folder File Path###. In filefinder.py, it should look similiar to this:
"C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Participants"

Find ###Participants Folder File Path IN FRONT OF /{}_images.txt###. Within that line, Copy and paste the Participant Folder file path in front of /{}_images.txt. In filefinder.py, the result should look similiar to this:
"C:/Users/vanos/Desktop/SURCResearch/Personalised-CBM_4.18.22/Participants/{}_images.txt"

Once this is done, double check that everything is spelled correctly. NOW YOU CAN RUN filefinder.py 
The Participants folder will now hold files that can be used to for the abm.html and aat.html protocols in the Cognitive Bias Experiment.


4. File Directory Path Syntax and Common Problems
For file paths, make sure you are using / and not \
Make sure "" are placed correctly
Make sure spelling is correct
Make sure that the  data within the ratings files have .jpg and NOT .JPG





