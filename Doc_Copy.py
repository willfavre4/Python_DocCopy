import time
start_time = time.time()

#FIND DOCUMENTS PATH
import ctypes.wintypes
CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

print(buf.value)


#COPY DOCUMENTS PATH TO TEMPORARY FOLDER

import shutil
import os

#create directory to copy files to
#os.makedirs('Program Files\TempPy')

SOURCE = buf.value
BACKUP = "Program Files\TempPy\ddd"


# create a backup directory
print 'about to start copying directory'
shutil.copytree(SOURCE, BACKUP)

print (os.listdir(BACKUP))
print 'backup complete'

#ZIP THE FILE
import random
import zipfile
import sys

print 'about to zip the file'
output_path = 'Program Files'
folder_path = 'Program Files\TempPy\Documents'

def zipfolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED, allowZip64 = True)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

output_filename = str(random.randint(1, 1000))
zipfolder(output_filename, 'Program Files')

print 'zip complete'



#UPLOAD TO GOOGLE DRIVE
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

print 'now to upload to google drive'
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

f = drive.CreateFile({'title': output_filename})
f.SetContentFile(output_filename + ".zip") # Read local file
f.Upload() # Upload it
print 'upload started/complete'

print 'Done! This upload took --- %s seconds ---' % float((time.time() - start_time()))

# remove it
#shutil.rmtree(BACKUP)

#print (os.listdir(BACKUP))
