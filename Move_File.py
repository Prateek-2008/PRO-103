import os
import shutil
from_dir="C:/Users/Prateek & Pranjali/Desktop"
to_dir="C:/Users/Prateek & Pranjali/Downloads"
list_of_files=os.listdir(from_dir)
##print(list_of_files)
file_name=""
source=from_dir+'/'+file_name
extension=to_dir+'/'+"documentfile"
destination=to_dir+'/'+"documentfile"+'/'+file_name
if os.path.exists(extension):
    print("Moving"+file_name+".....................................................")
    shutil.move(source,destination)
else:
    os.makedirs(extension)
    print("moving"+file_name+"....................................................................................................")
    shutil.move(source,destination)