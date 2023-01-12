import requests

print(requests.__version__)
print(requests.get("https://raw.githubusercontent.com/kirat21/CMPUT404-lab1/main/lab1.py").text)