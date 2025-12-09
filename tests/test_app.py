# tests/test_app.py
from src.app import calculate_sum, is_even # is_evenをインポートしておく

def test_calculate_sum():
    # 既存のテストを修正せず、そのままにする
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(-1, 1) == 0
