import os
from fitparse import FitFile

FIT_FILES_DIR = "fit_files"

def rename_fit_files():
    for filename in os.listdir(FIT_FILES_DIR):
        # Check if its already renamed
        if filename.endswith('.fit') and not filename.count('2') == 3:              
            filepath = os.path.join(FIT_FILES_DIR, filename)
            try:
                fitfile = FitFile(filepath)
                sessions = list(fitfile.get_messages('session'))
                if sessions:
                    session = sessions[0]
                    start_time = session.get_value('start_time')
                    
                    # Format the new filename
                    new_filename = f"{start_time.strftime('%Y-%m-%d')}.fit"
                    new_filepath = os.path.join(FIT_FILES_DIR, new_filename)
                    
                    # Rename the file
                    os.rename(filepath, new_filepath)
                    print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")
