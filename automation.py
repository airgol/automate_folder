import time
import os
# Moving to Download directory
directory_download = "/home/cloud/Downloads" 
os.chdir(directory_download)

files = os.listdir(os.getcwd())

# Time right now
time_now = time.time()
# 30 days calculated in seconds
days = 30*24*60*60

# We check every item in list; if it is a directory we do nothing 
# If it is a file, we check if we used it in the last 30 days,
# We delete the files that we did not use in 30 days
for file_name in files:
    if not os.path.isdir(file_name):
        access_time = os.stat(file_name).st_atime

        if access_time < (time_now - days):
            os.remove(file_name)
            print(file_name + "was remove")

# Organizing files in Downloads Directory
list = ['pdf', 'zip', 'gz','docx','xlsx','xls','csv','db','deb','png','jpg','jpeg']
for file_name in files:
    if not os.path.isdir(file_name):
        for lista in list:
            # Lista folder will have he name of the extension
            lista_f = lista 
            # If we want to specify the folder name for specific files extension
            # we rename them here in groups
            if lista == 'xlsx' or lista == 'xls':
                lista_f = "csv"
            if lista == 'xz':
                lista_f = "gz"
            if lista == 'png' or lista == 'jpg' or lista == 'jpeg':
                lista_f = "images"
            
            if file_name.endswith("." + lista):
                # Checking if the pdf directory exist
                if not os.path.isdir(lista_f):
                    os.system('mkdir ' + lista_f)
                os.system('mv "'+ file_name + '" ./' + lista_f + '/')





