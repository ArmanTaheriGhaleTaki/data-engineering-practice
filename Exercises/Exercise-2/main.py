import requests
import pandas
import re
import zipfile
from bs4 import BeautifulSoup
import os
from collections import defaultdict



def download_file(url, folder):
        file_name = os.path.basename(url)
        file_path = os.path.join(folder, file_name)
        if os.path.exists(os.path.splitext(file_path)[0]+'.csv'):
            print(f'{file_name} already existed Skillping downloading')
            return 
        response = requests.get(url, stream=True)
        if response.status_code != 200:
            print(f'{url} is not found ')
            return
         
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Downloaded {file_name} to {file_path}')

        return                

def main():
    folder_download='download'
    downloads_folder = os.path.join(os.path.expanduser('.'), folder_download)
    os.makedirs(downloads_folder, exist_ok=True)


    url ='https://www.ncei.noaa.gov/data/local-climatological-data/access/2023/'
    download_url='https://www.ncei.noaa.gov/data/local-climatological-data/access/2023/01001099999.csv'
    regex=re.compile(r'\d+-\d+\d-\d+\s\d+:\d+')
    target_date = "2024-01-11 10:58"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('td',align='right')
    for i in links:
        date = i.get_text(strip=True)
        chosen =re.match(regex,date)
        if (chosen!=None):
            if(chosen.group()==target_date):
                # download_file(url+chosen.string, folder_download)
                target=i.parent.find('a').get_text(strip=True)
                download_file(url+target,folder_download)
                # print(chosen.string)
        
            
            

# # Target modification date

# Iterate through the links and find the one with the target modification date
    # for link in links:
    #     href = link.get('href')
    #     if href.endswith('.csv'):
    #     # Check the modification date
    #         file_url = url + href
    #         head_response = requests.head(file_url)
    #         last_modified = head_response.headers.get('Last-Modified')
    #         if last_modified and target_date in last_modified:
    #             print(f"Found the file: {file_url}")
                 

    # your code here


if __name__ == "__main__":
    main()
