import requests
from bs4 import BeautifulSoup
import urllib.parse

# Base URL
base_url = 'https://gentoo.osuosl.org/distfiles/'

# Function to recursively fetch files from directories
def fetch_files(url):
    
    file_names = []
    
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        x = soup.find_all()

        # Loop through all the <a> tags (hyperlinks) and only process files and folders
        for link in soup.find_all('a'):
            href = link.get('href')
            full_url = urllib.parse.urljoin(url, href)

            # if  : check if it's a directory
            # elif: check if it's a file
            # else: Ignore all other cases
            if href[:-1].isalnum() and href[-1] == '/':
                # Build the full URL for the directory
                files = fetch_files(full_url)
                if files:
                   file_names += files
                print(full_url)
            elif href.find('/') == -1 and href.find('?') == -1:
                file_names.append(f'file_name: {full_url}')
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
    
    return file_names

# Start fetching files from the base URL
file_names = fetch_files(base_url)
with open('fetch_file_names_log.txt', 'w') as f:
    for name in file_names:
        f.write(f"{name}\n")