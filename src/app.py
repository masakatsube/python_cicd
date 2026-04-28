# src/app.py の新しい内容
def greet(user_name):
    # 既存のロジック (テスト済みと仮定)
    return f"Hello, {user_name}!"

def check_age(age):
    """
    ユーザーが成人かどうかをチェックする。
    """
    if age >= 20: # <--- 変更行 (新しいロジック)
        return "Adult"
    else:
        return "Minor" # <--- 変更行 (新しいロジック)
