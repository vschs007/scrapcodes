import os
directory = r"D:\cpright"

# Copyright string to be added
copyright = 'Copyright (c) 2023 ORG'
extensions = ['.c', '.java', '.h']
# Iterate over all files in the directory
for filename in os.listdir(directory):
    if any(filename.endswith(ext) for ext in extensions):
        # Open the file in read mode
        with open(os.path.join(directory, filename), 'r') as file:
            # Read the contents of the file
            contents = file.read()

        # Add the copyright string at the top of the file
        contents = f'{copyright}\n\n{contents}'

        # Open the file in write mode
        with open(os.path.join(directory, filename), 'w') as file:
            # Write the modified contents to the file
            file.write(contents)

        # Close the file
        file.close()
