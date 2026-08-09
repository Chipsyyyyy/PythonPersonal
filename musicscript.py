import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)


for filename in os.listdir(current_dir):
    filepath = os.path.join(current_dir, filename)
    
    if os.path.isfile(filepath):
        parts = filename.split(" - ", 1)
        
        if len(parts) == 2:
            track_number, remaining_name = parts
            
            new_filepath = os.path.join(current_dir, remaining_name)
            
            print(f"Remaining: '{filename}' --> '{remaining_name}'")
            
            try:
                os.rename(filepath, new_filepath)
                print("Completed")
            except Exception as e:
                print(f"Error remaning file: {e}")