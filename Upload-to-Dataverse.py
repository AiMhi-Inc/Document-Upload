import requests

def upload_files_from_desktop():
    """
    Opens a file dialog that allows the user to select a file from their desktop.

    Returns:
        str: The path of the selected file. If no file is selected, returns None.
    """
    root = Tk()
    root.withdraw()
    file_path = askopenfilename()

    if file_path:
        # Define the necessary parameters for the Dataverse API
        dataverse_server = 'https://your_dataverse_server'
        api_key = 'your_api_key'
        dataset_id = 'your_dataset_id'

        # Define the headers for the API request
        headers = {
            'X-Dataverse-key': api_key
        }

        # Define the parameters for the API request
        params = {
            'description': 'Uploaded file',
            'categories': '["Data"]'
        }

        # Open the file in binary mode
        with open(file_path, 'rb') as file:
            # Define the files for the API request
            files = {
                'file': file
            }

            # Make the API request to upload the file to Dataverse
            response = requests.post(f'{dataverse_server}/api/datasets/:persistentId/add?persistentId={dataset_id}', headers=headers, files=files, data=params)

            # Check if the API request was successful
            if response.status_code == 201:
                print('File uploaded successfully to Dataverse.')
            else:
                print('Failed to upload file to Dataverse.')

    return file_path
