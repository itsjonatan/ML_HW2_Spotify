import kagglehub
import shutil
import os

# Create data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Download latest version
print("Downloading dataset...")
path = kagglehub.dataset_download("salvatorerastelli/spotify-and-youtube")

print("Path to dataset files:", path)

# Move the CSV file to the data directory
csv_file = os.path.join(path, "Spotify_Youtube.csv")
if os.path.exists(csv_file):
    shutil.copy2(csv_file, "data/Spotify_Youtube.csv")
    print("Dataset has been copied to data/Spotify_Youtube.csv")
else:
    print("Error: Could not find Spotify_Youtube.csv in the downloaded files") 