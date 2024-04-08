from tkinter import Tk
from tkinter.filedialog import askopenfilename
import unittest
from unittest.mock import patch
import builtins

def upload_files_from_desktop():
    """
    Opens a file dialog that allows the user to select a file from their desktop.

    Returns:
        str: The path of the selected file. If no file is selected, returns None.
    """
    root = Tk()
    root.withdraw()
    file_path = askopenfilename()
    return file_path

class TestUploadFilesFromDesktop(unittest.TestCase):
    @patch.object(builtins, 'input', lambda _: 'test_file.txt')
    def test_upload_file_from_desktop(self):
        """
        Tests if the function returns the correct file path when a file is selected.
        """
        with patch('tkinter.filedialog.askopenfilename', return_value='C:/Users/User/Desktop/test_file.txt'):
            self.assertEqual(upload_files_from_desktop(), 'C:/Users/User/Desktop/test_file.txt')

    @patch.object(builtins, 'input', lambda _: '')
    def test_no_file_selected(self):
        """
        Tests if the function returns None when no file is selected.
        """
        with patch('tkinter.filedialog.askopenfilename', return_value=''):
            self.assertIsNone(upload_files_from_desktop())

if __name__ == "__main__":
    file_path = upload_files_from_desktop()
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")
