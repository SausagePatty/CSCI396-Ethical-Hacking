import requests

meta_ip = "10.0.2.5"
target_website = "http://" + meta_ip + "/mutillidae"

# Open the dirs.txt file
with open('dirs.txt', 'r') as file:
    # Loop through each line in the file
    for directory in file:
        # Remove any leading/trailing whitespace characters
        directory = directory.strip()
        # Construct the URL
        url = target_website + "/" + directory
        # Make the GET request
        response = requests.get(url)
        # Print only if the request was successful (status code 200)
        if response.status_code == 200:
            print(f"Directory found: {url}")
        #else:
            #print(f"Directory not found: {url}") (status code 404)

