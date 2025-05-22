
data = {"temp1":1, "temp2":2, "temp3":3, "temp4":4, "important":200}

removed_keys = ['temp1', 'temp2', 'temp3', 'temp4']

for key in removed_keys:

    data.pop(key, None)

print(data)