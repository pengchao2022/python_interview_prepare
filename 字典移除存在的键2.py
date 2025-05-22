
config = {"theme":"dark", "font_size":14, "auto_save":True}

key_to_remove = "font_size"

if key_to_remove in config:
    config.pop(key_to_remove)

print(config)