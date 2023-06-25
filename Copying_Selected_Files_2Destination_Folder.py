
'''
This code recursively searches for image files with a specific extension in a given root directory
and copies them to a destination folder. Specifically, it looks for files ending with "FLAIR.nii.gz"
in the provided root directory and its subfolders, and copies them to the specified destination folder.

Instructions:
1. Set the root directory path where the image files are located.
2. Set the destination folder path where the selected image files will be copied.
3. Run the code.

'''

# Function to copy files with a specific extension from a root directory to a destination folder
def copy_files(root, ext, dest):
    # Traverse through the directory tree starting from the root directory
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            # Check if the file has the desired extension
            if filename.endswith(ext):
                # Create the source path by joining the root directory and the file name
                source_path = os.path.join(dirpath, filename)
                
                # Create the destination path by joining the destination folder and the file name
                destination_path = os.path.join(dest, filename)
                # Copy the file from the source path to the destination path
                shutil.copyfile(source_path, destination_path)
