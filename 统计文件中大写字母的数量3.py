def count_uppercase_letters(file_path):
    """
    统计文件中大写字母的数量
    :param file_path: 文件路径
    :return: 大写字母数量 (若出错返回错误信息)
    """
    try:
        # 使用 with 语句安全打开文件
        with open(file_path, 'r', encoding='utf-8') as file:
            # 初始化计数器
            count = 0
            
            # 逐行读取文件内容 (适合大文件)
            for line in file:
                # 统计每行的大写字母数量
                count += sum(1 for char in line if char.isupper())
                
            return count
            
    except FileNotFoundError:
        return "错误：文件不存在"
    except PermissionError:
        return "错误：没有文件读取权限"
    except UnicodeDecodeError:
        return "错误：文件编码格式不支持"
    except Exception as e:
        return f"未知错误：{str(e)}"

# 使用示例
if __name__ == "__main__":
    file_path = input("请输入文件路径：")
    result = count_uppercase_letters(file_path)
    
    if isinstance(result, int):
        print(f"文件中的大写字母数量为：{result}")
    else:
        print(result)