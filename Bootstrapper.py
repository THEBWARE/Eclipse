import requests
import zipfile
import io
from colorama import init, Fore

init()

eclipse_art = f"""
{Fore.BLUE}
 _____     _ _                
| ____|___| (_)_ __  ___  ___ 
|  _| / __| | | '_ \/ __|/ _ \
| |__| (__| | | |_) \__ \  __/
|_____\___|_|_| .__/|___/\___|
              |_|             
{Fore.RESET}
"""

def download_and_extract(url, extract_to='.'):
    print(f"{Fore.BLUE}\nDownloading file from {url}...{Fore.RESET}")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        print(f"{Fore.BLUE}Extracting files...{Fore.RESET}")
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            zip_ref.extractall(extract_to)
        
        print(f"{Fore.BLUE}Download and extraction completed successfully!{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Fore.RESET}")

if __name__ == "__main__":
    print(eclipse_art)
    download_url = "https://github.com/THEBWARE/Saturngg/releases/download/Setup/Saturn.gg-V1.1.4.zip"
    download_and_extract(download_url)
    print("\nOperation completed.")
