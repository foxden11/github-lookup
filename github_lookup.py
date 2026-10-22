import requests

username = input("GitHub username: ")

try:
    response = requests.get("https://api.github.com/users/" + username)
    data = response.json()

    if "name" in data:

        if data["name"] is None:
            print("No name listed")
        else:
            print(data["name"])

        if data["location"] is None:
            print("No location listed")
        else:
            print(data["location"])

        print("Repos:", data["public_repos"])
        print("Followers:", data["followers"])
        print("Profile:", data["html_url"])

    else:
        print("User not found")

except requests.exceptions.RequestException as e:
    print("Network problem:", e)