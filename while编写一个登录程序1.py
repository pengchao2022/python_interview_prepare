user_name = 'allen'
pass_word = '123456'

while True:
    type_name = str(input("请输入您的用户名："))
    type_pass = str(input("请输入您的密码："))
    if type_name == user_name and type_pass == pass_word:
        print("恭喜您！登录成功！")
    elif type_name == user_name and type_pass != pass_word:
        print("密码不正确")
    elif type_name != user_name and type_pass == pass_word:
        print("用户名不正确")
    else:
        print("用户名和密码都不正确")

