# 读取文件并提取第一行数据（转换为数字列表）
with open('A.txt', 'r') as f:
    line = f.readline().strip()  # 读取第一行并去除首尾空白
    a = list(map(int, line.split())) if line else []

with open('B.txt', 'r') as f:
    line = f.readline().strip()
    b = list(map(int, line.split())) if line else []

# 合并并排序
combined = a + b
combined.sort()

# 写入文件（按空格分隔）
with open('C.txt', 'w') as f:
    f.write(' '.join(map(str, combined)))