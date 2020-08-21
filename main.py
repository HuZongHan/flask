from flask import Flask
from flask import request
from flask import render_template


USERS = {
    1: {'name': '郭德纲', 'gender': '男', 'city': '北京', 'desc': '班长', },
    2: {'name': '陈乔恩', 'gender': '女', 'city': '上海', 'desc': None, },
    3: {'name': '赵丽颖', 'gender': '女', 'city': '北京', 'desc': '班花'},
    4: {'name': '王宝强', 'gender': '男', 'city': '重庆', 'desc': '超爱吃火锅'},
    5: {'name': '赵雅芝', 'gender': '女', 'city': '重庆', 'desc': '全宇宙三好'},
    6: {'name': '张学友', 'gender': '男', 'city': '上海', 'desc': '奥林匹克总'},
    7: {'name': '陈意涵', 'gender': '女', 'city': '上海', 'desc': None, },
    8: {'name': '赵本山', 'gender': '男', 'city': '南京', 'desc': '副班长'},
    9: {'name': '张柏芝', 'gender': '女', 'city': '上海', 'desc': None, },
    10: {'name': '吴亦凡', 'gender': '男', 'city': '南京', 'desc': '大碗宽面'},
    11: {'name': '鹿晗', 'gender': '保密', 'city': '北京', 'desc': None, },
    12: {'name': '关晓彤', 'gender': '女', 'city': '北京', 'desc': None, },
    13: {'name': '周杰伦', 'gender': '男', 'city': '台北', 'desc': '小伙人才啊'},
    14: {'name': '马云', 'gender': '男', 'city': '南京', 'desc': '一个字：贼'},
    15: {'name': '马化腾', 'gender': '男', 'city': '上海', 'desc': '马云死对头'},
}


app = Flask(__name__)


@app.route('/')
def home():
    user_list = []
    for uid, info in sorted(USERS.items()):
        item = [uid, info['name']]
        user_list.append(item)

    return render_template('home.html', user_list=user_list)


@app.route('/user/info')
def user_info():
    uid = int(request.args.get('id'))
    user_data = USERS[uid]

    lst = [222222, 'bbb', 444444, 'ddd']

    return render_template('info.html', user=user_data, lst=lst)


@app.route('/menu')
def menu():
    # menu_items = ['炒鸡蛋', '酸菜鱼', '麻辣烫', '葱油拌面', '鱼香肉丝']
    menu_items = []
    return render_template('menu.html', menu_items=menu_items)


if __name__ == "__main__":
    app.run(debug=True)
