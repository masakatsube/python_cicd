# tests/test_app.py の追記

from src.app import greet, check_age # check_age をインポート

def test_greet_success():
    assert greet("Alice") == "Hello, Alice!"

# ⬇️ 新しく追加するテスト ⬇️

def test_check_age_adult():
    # 成人 (>= 20) のパスをテスト
    assert check_age(25) == "Adult"
