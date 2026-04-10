import requests
name=input("Enter name: ")

url=f"https://api.agify.io/?name={name}"

response=requests.get(url)

print(response.json())