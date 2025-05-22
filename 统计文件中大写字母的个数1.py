
def count_uppercase_letter(file_path):
    '''
    统计文件中大写字母的数量
    :param file_path 文件路径
    : return 大写字母数量 (若出错返回错误信息)
    
    '''
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            #初始化计数器
            count = 0
            #逐行读取文件内容
            for line in file:
                count += sum(1 for char in line if char.isupper())
            return count
        
    except FileExistsError:
        return "错误：文件不存在"
    except PermissionError:
        return "错误：没有文件读取权限"
    except UnicodeDecodeError:
        return "错误：文件编码格式不支持"
    except Exception as e:
        return f"未知错误：{str(e)}"
    
if __name__ == "__main__":
    file_path = input("请输入文件路径：")
    result = count_uppercase_letter(file_path)

    if isinstance(result, int):
        print(f"文件中大写字母数量为：{result}")

    else:
        print(result)