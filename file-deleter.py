import os
from collections import Counter


# TODO: add subfolder name reporting and statistics
# TODO: auto create backup for data recovery

def report_changes(num_files, size_files, type_files):
    print(str(num_files) + ' files (' + str(size_files/1000) + ' kb) were removed.\n' +
          'The files were of the following type: ')

    for ext in type_files:
        print(*ext, sep=':')

def ext_counter(extensions):
    output = []
    for unique_ext in set(extensions):
        output.append([unique_ext, extensions.count(unique_ext)])

    # sorts by freq using second item in each nested ext:count pair
    output = sorted(output, key = lambda x: int(-x[1]))
    return output

def file_info(path):
    file_size = os.stat(path).st_size
    extension = os.path.splitext(path)[1]
    return file_size, extension

def delete_files(path):
    # Var to display total number of files
    num_files = 0
    size_files = 0
    extensions = []
    for root, _, files in os.walk(path, topdown=False):
        num_files += len(files)
        
    # Constructs file path and removes the file from the subdirectory
        for name in files:
            file_path = os.path.join(root, name)            
            file_size, extension = file_info(file_path)

            size_files += file_size
            extensions.extend([extension])

            os.remove(file_path)
    type_files = ext_counter(extensions)

    return num_files, size_files, type_files

def deletion_manager(path, folder):     
    while True:
        confirmation = input('Are you sure you want to delete the files from' +
                             ' every subfolder in "' + folder + '" ? Y/N ').lower()
        
        if confirmation == 'y': 
            num_files, size_files, type_files = delete_files(path)
            report_changes(num_files, size_files, type_files)
            break

        elif confirmation == 'n': 
            print('No files will be deleted. Goodbye!')
            break

        else:
            print('Invalid command. Restarting...')

def path_checker():
    while True:
        path = input('Paste the file path to the desired folder here or press e to exit: ')
        verification = os.path.isdir(path)

        if verification:
            folder_pointer = path.rfind('/')
            folder_name = path[folder_pointer: ]
            deletion_manager(path, folder_name)
            break

        elif path == 'e':
            print('Goodbye!')
            break

        else:
            print('Invalid path. restarting...')

if __name__ == "__main__":
    
    print('================FILE DELETER================')
    path_checker()
