# import requests

# response = requests.get("https://api.github.com/users/rudrashukla1507")
# print(response.status_code)

# data = response.json()
# print(data["login"])
# print(data["public_repos"])


import requests
response = requests.get("https://api.github.com/users/rudrashukla1507/repos")
repos = response.json()

if response.status_code == 200:
    print ("Got your repo, getting info...")
    for repo in repos:
        print(repo["name"],repo["language"])


else:
    print("Cannot get your repo, try again!")
    print(response.status_code)

