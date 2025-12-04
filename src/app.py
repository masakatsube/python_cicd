def get_message(name):
    """
    引数に応じてメッセージを返す関数
    """
    if name:
        return f"Hello, {name}!"
    else:
        # この行は意図的にテストから外し、カバレッジの不足を表現
        return "Hello, World!"

if __name__ == "__main__":
    print(get_message("User"))
