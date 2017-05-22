'''
模块定义一个函数库，包括两个函数供其它函数使用
函数yanghui(n)用于输出n阶杨辉三角
函数hannuota(n)用于完成n阶汉诺塔移动模拟
模块具有自测试功能，当直接运行模块时，可输出10阶杨辉三角和完成3层汉诺塔移动模拟
'''

###杨辉三角yanghui()代码开始###
def yanghui(n):
    if not str(n).isdecimal() or n<2 or n>25:
        print('杨辉三角函数yanghui(n),参与n必须是不小于2且不大于25的正整数')
        return False

        #以下为使用列表生成杨辉三角
     #else:

    x=[]
    for i in range(1,n+1): #生成初试的杨辉三角不规则矩阵
            x.append([1]*i)

        #计算杨辉三角矩阵的其他值
    for i in range(2,n):
            for j in range(1,i):
                x[i][j]=x[i-1][j-1]+x[i-1][j]
        #输出杨辉三角
    for i in range(n):
            if n<=10:print(' '*(40-4*i),end=' ')
            for j in range(i+1):
                print('%-8d'%x[i][j],end='')
            print()
###杨辉三角函数代码结束###

###汉诺塔游戏模拟代码开始###
_times=0  #用于统计移动次数
def hannuota(nlist,mfrom,mpass,mto):
    global _times
    n=len(nlist)
    if n==1:
        _times+=1
        print('%-8d'%_times,':',mfrom,'--------->',mto)
    else:
        hannuota(nlist[:n-1],mfrom,mto,mpass)
        hannuota([nlist[-1]],mfrom,mpass,mto)
        hannuota(nlist[:n-1],mpass,mfrom,mto)
###汉诺塔游戏模拟代码结束###
    





###独立运行测试代码开始###
if __name__=='__main__':
    print('模块独立自运行测试输出：')
    print('一，10阶杨辉三角如下：')
    yanghui(10)

    print('二，3阶汉诺塔模拟过程如下：')
    print('step num:from------>to')
    hannuota([0,1,2],'A','B','C')