
resume_data={
    "ziwopingjia":"本人性格开朗......",
    "lianxifangshi":{
           "telephone":"021-65878999",
           "mobile-phone":"18510656167",
           "email":"allen.ma@gmail.com"   
     },
    "jiaoyubeijing":"peking univrsity",
    "zhuanyejineng":["skill1", "skill2", "skill3", "skill4"],
    "experience":[
        
        {"company":"bmw",
         "date":"2015-2017",
         "payment":12000,
         "city":"beijing"},

         {"company":"volvo",
         "date":"2017-2018",
         "payment":15000,
         "city":"shanghai"},

         {"company":"ibm",
         "date":"2021-2024",
         "payment":23000,
         "city":"shanghai"}]
}

#获得以往公司的信息
for i in resume_data.get("experience"):
    print(i.get('company'))

#获得手机号码
print(resume_data["lianxifangshi"]["mobile-phone"]) 

#获取邮箱
print(resume_data["lianxifangshi"]["email"])

#获取专业技能
for i in resume_data.get("zhuanyejineng"):
    print(i)
    
#获取自我评价
print(resume_data.get("ziwopingjia"))