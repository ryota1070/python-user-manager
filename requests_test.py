import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    with open("posts.txt", "w") as file:
        for post in posts[:5]:
            file.write(f"{post['id']}: {post['title']}\n")

    print("posts.txt に保存しました")
else:
    print("データ取得に失敗しました")