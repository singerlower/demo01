"""
1、“双色球”每注投注号码由6个红色球号码和1个蓝色球号码组成。
2、 红色球号码从1--33中选择；蓝色球号码从1--16中选择。
3、 选民手动输入号码
4、 选民可以复选或者依次选多张
5、 打印双色球显示结果，红球按顺序排序
6、 打印选中结果
7、 打印获奖等级
"""
import random
import time


# 人类
class Person(object):
    def __init__(self, init_name, init_age, init_gender):
        self.name = init_name
        self.age = init_age
        self.gender = init_gender


# 用户类
class User(Person):
    users = []

    def __init__(self, init_name='admin', init_age=20, init_gender='男'):
        Person.__init__(self, init_name, init_age, init_gender)
        self.choices = []  # 选择的双色球
        self.wins = []  # 选中存储列表

    # 用户登录
    def login(self):
        """
        用户登录
        :return: 如果登陆成功返回True, 反之为False
        """
        self.name = input("请输入用户名：").strip()
        self.age = int(input("请输入用户年龄：").strip())
        self.gender = input("请输入用户性别：").strip()
        User.users.append(self)
        return True

    # ===============================   选民选票   ===============================
    def choice_balls(self):
        # 存储选民选择的所有票
        while True:
            # 存储选民一票选票信息
            your_balls = {'红球': [], '蓝球': [], '注数': 1}
            # 存储选民红球
            choice = 1
            while True:
                your_red = int(input('请输入你选择的第%d个红球数字：' % choice).strip())
                if your_red in your_balls['红球']:
                    print('已经输入过%d,请重新输入' % your_red)
                    continue
                else:
                    your_balls['红球'].append(your_red)
                    choice += 1

                if choice >= 7:
                    break

            # 存储选民蓝球
            your_bule = int(input('请输入你选择的蓝球数字：'))
            your_balls['蓝球'].append(your_bule)
            # 存储选民注数
            your_numbers = int(input('请输入你选择加注数：'))
            your_balls['注数'] = your_numbers

            # 存储选民一张票到所有票列表
            self.choices.append(your_balls)
            print("您的双色球为：", your_balls)
            # 是否继续选票
            flag = input('是否继续选择？（y/n）:')
            if flag == 'n':
                print('\033[1;33;44m', end='')
                print('您的所有双色球选票为:', end='')
                print('\033[0m')
                print(self.choices)
                break  # 退出选票

    def __str__(self):
        return self.name


# 系统生成双色球类
class SystemBall(object):
    def __init__(self):
        self.double_balls = {'红球': [], '蓝球': []}  # 系统自动生成的票

    def auto_balls(self):
        # ===============================   系统双色球   ===============================
        reds = [red for red in range(1, 34)]  # 所有红球
        blues = [blue for blue in range(1, 17)]  # 所有蓝球

        # 生成双色球红球号码
        for number in range(6):
            red_ball = random.choice(reds)
            self.double_balls['红球'].append(red_ball)
            reds.remove(red_ball)

        # 对双色球中红球升序排序
        for n in range(5):
            for j in range(5-n):
                if self.double_balls['红球'][j] > self.double_balls['红球'][j+1]:
                    self.double_balls['红球'][j], self.double_balls['红球'][j+1] = \
                        self.double_balls['红球'][j+1], self.double_balls['红球'][j]

        # 生成双色球蓝球号码
        blue_ball = random.choice(blues)
        self.double_balls['蓝球'].append(blue_ball)
        blues.remove(blue_ball)

        time.sleep(3)    # 延时显示
        print('\033[1;33;41m', end='')
        print('双色球结果:', end='')
        print('\033[0m')
        print(self.double_balls)

    def compare_balls(self, user):
        # ===============================   对比选票与系统生成票   ===============================
        # 获取每一张选票
        for user_one in user.choices:
            # 存储选民选中票的信息
            win_balls = {'红球': [], '蓝球': [], '注数': 1}
            # 存储选民选中红球
            for red in user_one['红球']:
                if red in self.double_balls['红球']:
                    win_balls['红球'].append(red)
            # 存储选民选中蓝球
            if self.double_balls['蓝球'] == user_one['蓝球']:
                win_balls['蓝球'] = user_one['蓝球']
            # 存储选民选中注数
            win_balls['注数'] = user_one['注数']

            # 添加到选民选中票列表
            user.wins.append(win_balls)

        time.sleep(3)    # 延时显示
        print('\033[1;33;45m', end='')
        print('{}最后选中球:'.format(user.name), end='')
        print('\033[0m')
        print(user.wins)   # 打印结果

    @staticmethod
    def win(user):
        """  依据获奖结果打印获奖等级 """
        num_ball = 0  # 标记是第i注彩票
        for lottery in user.wins:
            num_ball += 1
            red_num = len(lottery['红球'])
            blue_num = len(lottery['蓝球'])
            if red_num == 6:
                if blue_num:
                    print('祝贺{}买中第{}注彩票，获得一等奖!'.format(user.name, i))
                else:
                    print('祝贺{}买中第{}注彩票，获得二等奖!'.format(user.name, i))
            elif red_num == 5:
                if blue_num:
                    print('祝贺{}买中第{}注彩票，获得三等奖!'.format(user.name, i))
                else:
                    print('祝贺{}买中第{}注彩票，获得四等奖!'.format(user.name, i))
            elif red_num == 4:
                if blue_num:
                    print('祝贺{}买中第{}注彩票，获得四等奖!'.format(user.name, i))
                else:
                    print('祝贺{}买中第{}注彩票，获得五等奖!'.format(user.name, i))
            elif red_num == 3 and blue_num:
                print('祝贺{}买中第{}注彩票，获得五等奖!'.format(user.name, i))
            elif blue_num:
                print('祝贺{}买中第{}注彩票，获得六等奖!'.format(user.name, i))
            else:
                print("{}的第{}注彩票未中奖".format(user.name, i))
                print('谢谢惠顾！祝您下次中奖！')


if __name__ == '__main__':
    # 生成三个用户
    print('*******双色球开始*******')
    for i in range(2):
        print('欢迎第{}个用户登录'.format(i+1))
        user = User()
        if user.login():
            user.choice_balls()  # 选球
        else:
            print('登陆失败')
    # 系统生成双色球
    system_ball = SystemBall()
    system_ball.auto_balls()
    # 对比结果
    for u in User.users:
        system_ball.compare_balls(u)
        system_ball.win(u)
    print('*******END*******')
