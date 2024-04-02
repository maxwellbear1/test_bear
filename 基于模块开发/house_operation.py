# @Version : 1.0
# @Author  : Max
# @File    : house_operation.py
# @Time    : 2024/3/31 15:00
"""
    说明：提供对房屋的各种操作
"""

from my_tools import *


def main_menu():
    """
    显示主菜单，让用户选择
    :return:
    """
    print()
    print("房屋出租系统菜单".center(32, "="))
    print("\t\t\t1 新 增 房 源")
    print("\t\t\t2 查 找 房 屋")
    print("\t\t\t3 删 除 房 屋 信 息")
    print("\t\t\t4 修 改 房 屋 信 息")
    print("\t\t\t5 房 屋 列 表")
    print("\t\t\t6 退       出")


# 1.使用字典来存储房屋信息
# 2.一个字典对象就对应一个房屋信息
# 3.多个字典/房屋信息，就放到list中进行管理
# 4.设计 houses_list=[{"id":2,"name":tim,"phone":"113",
# "address":"海淀","rent":800,"state":"未出租"}，{其他多个信息}...]

# 全局变量即 houses 存放所有的房屋信息
# 为了测试方法，老师放了一个测试数据到该列表
houses = [{"id": 1, "name": "tim", "phone": "113",
           "address": "海淀", "rent": 800, "state": "未出租"}]
# 全局变量id_counter 记录当前房屋的id
id_counter = 1


# 新增方法 find_by_id(find_id) 为了解决功能: 找到对应id
def find_by_id(find_id):
    """
    根据输入的find_id 返回对应的房屋信息(字典)
    如果没有就返回None
    :param find_id:
    :return:
    """
    # 遍历houses列表
    for house in houses:
        if house["id"] == find_id:
            return house
    # 如果没有return,默认就是返回None 可以不写return None
    # return None


def list_houses():
    """
    显示房屋列表
    :return:
    """
    print("房屋列表".center(60, "="))
    # 打印表头信息
    print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（为出租/已出租）")
    # 遍历houses这个列表
    # 取出的house就是一个字典对象
    #
    for house in houses:
        # 取出house的values,并进行遍历显示
        for value in house.values():
            print(value, end="\t\t")
        # 输出一个完成的house信息后，换行
        print()
    print("房屋列表显示完毕".center(60, "="))


#    (3).添加房屋信息的功能
def add_house():
    """
    完成添加房屋信息
    :return:
    """
    print("添加房屋".center(32, "="))
    name = input("姓名：")
    phone = input("电话：")
    address = input("地址：")
    rent = int(input("租金："))
    state = input("状态：")
    # 由系统分配添加的房屋id
    global id_counter  # 全局变量id_counter
    id_counter += 1
    # 构建房屋信息对应的字典,加入到全局houses列表中
    house = {"id": id_counter, "name": name, "phone": phone,
             "address": address, "rent": rent, "state": state}

    houses.append(house)  # 加入到全局houses列表
    print("添加房屋成功".center(32, "="))


# (4).删除房屋信息功能
def del_house():
    """
    根据id删除房屋信息
    :return:
    """
    print("删除房屋信息".center(32, "="))
    del_id = int(input("请输出待删除房屋的编号（-1退出）："))
    if del_id == -1:
        print("放弃删除房屋信息".center(32, "="))
        return
    # 让用户确认删除(Y/N)
    # while循环   如果输入的不是y/n 就一直提示输入
    # while True:
    #     key = input("请输入你的选择（Y/N),请确认选择：")
    #     if key.lower() == "y" or key.lower() == "n":
    #         break

    choice = read_confirm_select()

    if choice == "y":  # 如果真的要删除
        print("真的要删除id=", del_id)
        # 根据del_id 去 houses列表中查找是否存在该房屋[字典]
        house = find_by_id(del_id)
        if house:  # if 对象 :不是空的，就是True
            # 执行删除
            houses.remove((house))
            print("删除房屋信息成功".center(32, "="))
        else:
            print("房屋编号不存在，删除失败".center(32, "="))


    else:  # 说明不是 y 那就是n
        print("放弃删除房屋信息".center(32, "="))


# (5) 完善退出确认功能
def exit_sys():
    """
    完成退出系统，并确认（Y/N）
    :return:如果确认退出返回True,否则返回False
    """

    choice = read_confirm_select()
    if choice == "y":
        return True
    else:
        return False


# (6) 根据id查找房屋信息
def find_house():
    """
    查找房屋信息
    :return:
    """
    print("查找房屋信息".center(32, "="))
    find_id = int(input("请输入要查找的id："))
    # 调用函数，返回对应的房屋信息
    house = find_by_id(find_id)
    if house:
        # 打印表头
        print("编号\t\t房主\t\t电话\t\t地址\t\t月租\t\t状态（为出租/已出租）")
        for value in house.values():
            print(value, end="\t\t")
    else:
        print(f"查找房屋信息id {find_id}不存在")


# (7)修改房屋信息的功能

def update():
    """
    修改房屋信息
    :return:
    """
    print("修改房屋信息".center(32, "="))
    update_id = int(input("请选择待修改的房屋编号（-1表示推出）:"))
    if update_id == -1:
        print("放弃删除房屋信息".center(32, "="))
        return
    # 根据id查找对应的房屋信息
    house = find_by_id(update_id)
    if not house: #没有查找到房屋信息
        print("没有要修改的房屋信息".center(32,"="))
        return
    # 注意：如果用户直接回车，表示布修改当前这个信息，保留原来的值
    # 先按照简单的方式完成，后面优化-->将输入新数据封装成函数

    # name = input(f"姓名({house['name']}):")
    # if len(name) > 0: #如果用户输入的有内容，len（name)>0
    #     # 表示将接收到的name 赋给house字典对应的key='name' 对应的值
    #     house['name'] = name
    house['name'] = read_str(f"姓名({house['name']}):", house['name'])

    # phone = input(f"电话({house['phone']}):")
    # if len(phone) > 0:
    #     house['phone'] = phone
    house['phone'] = read_str(f"电话({house['phone']}):", house['phone'])

    # address = input(f"地址({house['address']}):")
    # if len(address) > 0:
    #     house['address'] = address
    house['address'] = read_str(f"地址({house['address']}):", house['address'])

    # rent = input(f"租金({house['rent']}):")
    # if len(rent) > 0:
    #     house['rent'] = int(rent)
    house['rent'] = int(read_str(f"租金({house['rent']}):", house['rent']))


    # state = input(f"状态({house['state']}):")
    # if len(state) > 0:
    #     house['state'] = state
    house['state'] = read_str(f"状态({house['state']})", house['state'])

    print("修改房屋信息成功".center(32, "="))