
def count_uppercase(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            return uppercase_count
    except FileNotFoundError:
        return "文件不存在"
    except Exception as e:
        return f"发生错误: {str(e)}"

# 使用示例
file_path = '/Users/pengchaoma/myfile12.txt'  # 替换为你的文件路径
result = count_uppercase(file_path)
print(f"文件中的大写字母数量为: {result}")

