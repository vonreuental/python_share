from wxpy import *


class WxBot:

    def __init__(self):
        self.bot = Bot(login_callback=self.login, logout_callback=self.login_out, cache_path='login.pkl',
                       qr_path='login_qr.png')
        self.bot.auto_mark_as_read
        self.bot.enable_puid(path='wxpy_puid.pkl')

    def login(self):
        print('状态:登录成功  ', end='')

    def login_out(self):
        print('微信已退出!')

    def get_menber_name(self, group):
        self.bot.groups(update=True)
        my_groups = self.bot.groups().search(group)[0]
        members = my_groups.members
        name_list = []
        for member in members:
            name_list.append(member.name)
        return name_list


if __name__ == '__main__':
    bot = WxBot()
    print(bot.get_menber_name('金控科技平台'))
