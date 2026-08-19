import requests

username = input("GitHub username: ")
response = requests.get("https://api.github.com/users/" + username)
data = response.json()

if data["name"] == None:
    print("No name listed")
else:
    print(data["name"])

if data["location"] == None:
    print("No location listed")
else:
    print(data["location"])

print("Repos:", data["public_repos"])
print("Followers:", data["followers"])
print("Profile:", data["html_url"])