from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import os
import json

gauth = GoogleAuth()
drive = GoogleDrive(gauth)




def create():
    #Create File
    folder = drive.ListFile({'q': "title = 'ClubData' and trashed=false"}).GetList()[0] # get the folder we just created
    file = drive.CreateFile({'title': "Hello.txt", 'parents': [{'id': folder['id']}]})
    file.SetContentString('Hello World!') # Set content of the file from given string.
    file.Upload()


def show(place):
    #File List
    # Auto-iterate through all files that matches this query
    file_list = drive.ListFile({'q':str("fullText contains '"+place+"' and trashed=false")}).GetList()
    count = 1
    lets = {}
    for file in file_list:
        lets[count] = file['title']
        count += 1
    
    return(json.dumps(lets))


def delete():
    #Delete File
    file1 = drive.CreateFile({'id': '1s_dyOCVw1IOHamcA9cD_zzLI8Kk8oNoe'})
    file1.Delete()


def createfol():
    #Creating a Folder
    folder = drive.CreateFile({'title': 'ClubData', "mimeType": "application/vnd.google-apps.folder"})
    folder.Upload()


def down(search):
    #Downloading Files
    path = '/home/college/Documents/Sem-5/hallothon/'+search
    if (os.path.exists(path) == True ):
        return 1
    else:
        folder = drive.ListFile({'q':str( "title contains '"+search+"' and trashed=false")}).GetList()[0]
        file_id = folder['id']
        file = drive.CreateFile({'id': file_id})
        file.GetContentFile(search) # downloads 'My Awesome File.txt' as 'my-awesome-file.txt'

def upload():
    #Upload files
    folder = drive.ListFile({'q': "title = 'ClubData' and trashed=false"}).GetList()[0]
    cool_image = drive.CreateFile({'parents': [{'id': folder['id']}]})
    cool_image.SetContentFile('haha22.pdf') # load local file data into the File instance
    cool_image.Upload() # creates a file in your drive with the name: my-awesome-file.txt

def downfol(lessgoo):
    lessgoo = str(lessgoo)
    folder = drive.ListFile({'q':str( "title contains '"+lessgoo+"' and trashed=false")}).GetList()[0]
    file_id = folder['id']
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(lessgoo) 



# Using the special variable 
# __name__
if __name__=="__main__":
    v ="Declare"
    show(v)
