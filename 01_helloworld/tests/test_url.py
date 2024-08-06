import requests

response = requests.get("http://127.0.0.1:8000")
print("Ststus Code: ",response.status_code)
print("Message: ", response.text)
print("JSON: ", response.json())
print("Header: ", response.headers)

print("\n")

response = requests.get("http://127.0.0.1:8000/ak")
print("Ststus Code: ",response.status_code)
print("Message: ", response.text)
print("JSON: ", response.json())
print("Header: ", response.headers)