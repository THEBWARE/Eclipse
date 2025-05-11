import requests
import zipfile
import io

eclipse_art = """
 _____     _ _                
| ____|___| (_)_ __  ___  ___ 
|  _| / __| | | '_ \/ __|/ _ \
| |__| (__| | | |_) \__ \  __/
|_____\___|_|_| .__/|___/\___|
              |_|              
"""

def download_and_extract(url, extract_to='.'):
    print("\nDownloading file from {}...".format(url))
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        print("Extracting files...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(extract_to)
        
        print("Download and extraction completed successfully!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print(eclipse_art)
    download_url = "https://github.com/THEBWARE/Saturngg/releases/download/Setup/Saturn.gg-V1.1.4.zip"
    download_and_extract(download_url)
    print("\nOperation completed.")
