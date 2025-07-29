import os
import subprocess

# Directory where the website will be saved
save_dir = os.path.expanduser("~/javascript_info_offline")

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

# wget command to mirror the website
command = [
    "wget",
    "--mirror",                 # Mirror the whole site
    "--convert-links",         # Convert links for offline use
    "--adjust-extension",      # Save files with .html extension
    "--page-requisites",       # Download all necessary files (CSS, images, etc.)
    "--no-parent",             # Don't ascend to parent directory
    "--no-check-certificate",  # Skip certificate check (optional, can remove)
    "--directory-prefix=" + save_dir,  # Save directory
    "https://javascript.info/"
]

# Run the command
try:
    print("📥 Downloading JavaScript.info for offline use...")
    subprocess.run(command, check=True)
    print(f"✅ Download complete! Open: {save_dir}/javascript.info/index.html in your browser.")
except subprocess.CalledProcessError:
    print("❌ Failed to download the site. Please check your internet connection or wget installation.")

