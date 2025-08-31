import requests
import sys

# A new, verified URL for the song metadata file.
url = "https://static.turi.com/datasets/millionsong/song_data.csv"
file_name = "song_data.csv"

print(f"Downloading {file_name} from a new source...")
print("This may take a few minutes. Please be patient.")

try:
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        total_size = int(response.headers.get('content-length', 0))
        bytes_downloaded = 0
        
        with open(file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                # --- Progress Bar ---
                bytes_downloaded += len(chunk)
                progress = (bytes_downloaded / total_size) * 100
                sys.stdout.write(f"\rDownloading... {progress:.1f}% complete")
                sys.stdout.flush()
        
        print("\n\nDownload complete!")
        print(f"File saved successfully as '{file_name}'.")
    else:
        print(f"\nError: Failed to download file. The server responded with status code: {response.status_code}")

except Exception as e:
    print(f"\nAn error occurred: {e}")