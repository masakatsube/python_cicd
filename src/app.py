# src/app.py

def calculate_sum(a, b):
    """二つの数の和を計算する関数"""
    return a + b

# 👇 【変更点1】既存のファイルに新しい関数を追加
def is_even(number):
    """数が偶数であるか判定する関数"""
    if number % 2 == 0:
        return True
    else:
        return False

def calculate_sum2(a, b):
    return a - b
