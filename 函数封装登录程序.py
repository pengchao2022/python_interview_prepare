def login_program():
    user_name = 'allen'
    pass_word = '123456'
    while True:
        type_name = input("请在此输入您的用户名：")
        type_pass = input("请在此输入您的密码：")
        if type_name == user_name and type_pass == pass_word:
            print("恭喜您！登陆成功！")
            break
        elif type_name == user_name and type_pass != pass_word:
            print("密码不正确！请重新输入")
        elif type_name != user_name and type_pass == pass_word:
            print("用户名不正确！请重新输入")
        else:
            print("用户名和密码都不正确！请重新输入")

login_program()