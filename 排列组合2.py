#小朋友走楼梯， 总共有34 阶楼梯，小朋友一次可以走1 阶， 2阶， 3阶， 走完有多少种方式

#i 表示1阶 i最大 34
#j 表示2 阶 j 最大 17
#k 表示3 阶 k 最大11
nu_count = 0
for i in range(35):
    for j in range(18):
        for k in range(12):
            if(i*1 + j*2 +k*3 == 34):
                nu_count += 1
                print(i,j,k)
print(f"总共有{nu_count}种组合方式")

