
str1 = "k:1 |k1:2|k2:3|k3:4"

d = {key: int(value) for items in str1.split('|') for key, value in (items.split(':'),)}

print(d)