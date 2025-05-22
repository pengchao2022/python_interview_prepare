
try:
    with open("mytestfile.txt", "r") as f:
        content = f.read()
        print(content)

except Exception as e:
    print(f"错误类型：{type(e).__name__}")
    print(f"错误消息：{str(e)}")