
try:
    with open("nonexistent.txt", "r") as f:
        content = f.read()
except Exception as e:
    print(f"错误类型: {type(e).__name__}")  # 输出: 错误类型: FileNotFoundError
    print(f"错误消息: {str(e)}")           # 输出: 错误消息: [Errno 2] No such file or directory...