import datetime
import random


class User:
    def __init__(self, name, email, age, country):
        self.name = name
        self.email = email
        self.age = age
        self.country = country

    def show_profile(self):
        print("-----")
        print(f"名前: {self.name}")
        print(f"メール: {self.email}")
        print(f"年齢: {self.age}")
        print(f"国: {self.country}")

    def is_adult(self):
        return self.age >= 18

def is_blank(text):
    return text.strip() == ""

def parse_age(text):
    try:
        age = int(text)
    except ValueError:
        return "not_number"
    if age < 0 or age > 150:
        return "out_of_range"
    return age
def is_valid_email(email):
    return "@" in email and "." in email
def load_users():
    loaded_users = []
    try:
        with open("users.txt", "r") as file:
            for line in file:
                name, email, age, country = line.strip().split(",")
                loaded_users.append(User(name, email, int(age), country))
    except FileNotFoundError:
        pass
    return loaded_users
def save_users(users):
    with open("users.txt", "w") as file:
        for user in users:
            file.write(f"{user.name},{user.email},{user.age},{user.country}\n")
messages = [
    "今日も少しずつ進めましょう。",
    "エラーは成長のチャンスです。",
    "1行ずつ理解すれば大丈夫です。",
    "昨日の自分より少し進めばOKです。"
    ]
users = load_users()
today = datetime.date.today()
formatted_today = today.strftime("%Y年%m月%d日")
print(f"今日の日付: {formatted_today}")
print(f"今日のメッセージ: {random.choice(messages)}")

while True:
    print("ユーザー管理アプリ")
    print("1: ユーザーを追加")
    print("2: 全ユーザーを表示")
    print("3: 成人ユーザーだけ表示")
    print("4: 終了")

    choice = input("番号を選んでください: ")

    if choice == "1":
        name = input("名前: ")
        if is_blank(name):
            print("名前を入力して下さい。")
            continue
        email = input("メール: ")
        if is_blank(email):
            print("メールを入力して下さい。")
            continue
        if not is_valid_email(email):
            print("有効なメールアドレスを入力してください。")
            continue
        age_text = input("年齢: ")
        age = parse_age(age_text)
        if age == "not_number":
            print("年齢は数字で入力してください。")
            continue
        if age == "out_of_range":
            print("年齢は0〜150の数字で入力してください。")
            continue

        country = input("国: ")
        if is_blank(country):
            print("国を入力して下さい。")
            continue

        user = User(name, email, age, country)
        users.append(user)
        
        print("ユーザーを追加しました。")

    elif choice == "2":
        for user in users:
            user.show_profile()

    elif choice == "3":
        for user in users:
            if user.is_adult():
                user.show_profile()

    elif choice == "4":
        print("終了します。")
        save_users(users)
        break

    else:
        print("正しい番号を入力してください。")
    