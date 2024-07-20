import requests
import os
import zipfile

download_uris = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]


def main():
    downloads_folder = os.path.join(os.path.expanduser('.'), 'Downloads')
    # os.mkdir(downloads_folder)   
    os.makedirs(downloads_folder, exist_ok=True)
    # your code here
    def download_file(url, folder):
    # Extract the file name from the URL
        file_name = os.path.basename(url)
        file_path = os.path.join(folder, file_name)
    # Check if csv file is existed 
        if os.path.exists(os.path.splitext(file_path)[0]+'.csv'):
            print(f'{file_name} already existed Skillping downloading')
            return 
    # Download the file
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            print(f'{url} is not found ')
            return  # Check for request errors

    # Write the content to a file
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Downloaded {file_name} to {file_path}')

        unzip_file(file_path=file_path,folder=folder)
        delete_file(file_path=file_path)
        return 
    

    def unzip_file(file_path,folder):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(folder)
        print(f'Extracted {file_path} to {folder}')


    def delete_file(file_path):
        os.remove(file_path)
        print(f'Deleted {file_path}')
     
    for i in download_uris:
        download_file(url=i,folder=downloads_folder)
        # unzip_file(zip_path,downloads_folder)
        # delete_file(zip_path)
    
    pass


if __name__ == "__main__":
    main()
    print(f'Script is finished')