# tests/test_app.py
import pytest
# src/app.py から get_message をインポートする
from src.app import get_message 

def test_get_message_with_name():
    assert get_message("Alice") == "Hello, Alice!"

def test_get_message_with_empty_name():
    assert get_message(None) == "Hello, World!"
