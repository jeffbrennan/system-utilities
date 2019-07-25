import os

print("================FILE DELETER================")

# Get folder path and extract folder name
main_path = input('Paste the file path to the desired folder here: ')
folder_pointer = main_path.rfind('/')
folder_name = main_path[folder_pointer:]

# User confirmation for deletion
confirmation = input('Are you sure you want to delete the files from all subfolders in "' + folder_name + '" ? Y/N ')

# Var to display total number of files
num_files = 0

if confirmation == 'Y': 
    for root, dirs, files in os.walk(main_path, topdown=False):
        
        num_files += len(files)
        
        # Constructs file path and removes the file from the subdirectory
        for name in files:
            file_path = os.path.join(root, name)
            os.remove(file_path)

    # Informs user of how many files were removed
    print(str(num_files) + ' files were removed')

else: 
    print('No files will be deleted.')