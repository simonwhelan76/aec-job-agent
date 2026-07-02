import requests

url = "https://autodesk.wd1.myworkdayjobs.com/en-US/Ext"

response = requests.get(url)

print("Status:", response.status_code)

print(response.text[:5000])