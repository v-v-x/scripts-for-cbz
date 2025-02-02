import os
import zipfile

def zip_jpeg_files():
    # Get the current working directory
    folder_path = os.getcwd()
    
    # Create a zip file with compression
    zip_filename = os.path.join(folder_path, 'images.zip')
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg'):
                    zipf.write(os.path.join(root, file), file)
    
    # Rename the zip file to .cbz
    cbz_filename = zip_filename.replace('.zip', '.cbz')
    os.rename(zip_filename, cbz_filename)
    
    # Delete all jpeg files
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.jpeg') or file.lower().endswith('.jpg'):
                os.remove(os.path.join(root, file))

# Execute the function
zip_jpeg_files()