import os
import requests
import zipfile
def Katrina():
    url = "https://data.rda.ucar.edu/ds897.7/Katrina.zip"
    extract_to = "./data"
    local_filename = url.split('/')[-1]
    # Download the file
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    # Extract the file
    with zipfile.ZipFile(local_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    # Clean up the zip file if necessary
    os.remove(local_filename)