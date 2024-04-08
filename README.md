# Desktop File Selector: A Python Utility for File Uploads and Dataverse Storage

This Python utility allows users to select and upload files from their desktop. It uses the Tkinter library to open a file dialog and return the path of the selected file.

## Usage

To use this utility, simply call the `upload_files_from_desktop` function. This function will open a file dialog that allows you to select a file from your desktop. The selected file path is returned as a string. If no file is selected, the function returns None.

Example:
```python
file_path = upload_files_from_desktop()
if file_path:
    print(f"Selected file: {file_path}")
else:
    print("No file selected.")

Testing
This repository also includes unit tests for the upload_files_from_desktop function. These tests check the function’s behavior when a file is selected and when no file is selected.

To run the tests, use the following command:

python -m unittest discover
