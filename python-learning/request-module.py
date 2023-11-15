import requests
# response = requests.get("https://www.google.com")
# print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": 1,
    "body": "bar",
    "userId": 100
}
headers = {
    'Content-type': 'application/json; charset=UTF-8',
  }
respone = requests.post(url, headers=headers, json=data)