# _*_ coding:utf-8 _*_
__author__ = "ZingP"

menu = {
    '四川省': {
        '成都市': ['锦江区', '武侯区', '高新区'],
        '绵阳市': ['三台县', '北川县', '江油县'],
        '宜宾市': ['长宁县', '兴文县', '高县'],
    },

    '河北省': {
        '唐山市': ['滦南县', '玉田县', '滦县'],
        '邯郸市': ['永年县', '广平县', '武安县'],
        '秦皇岛市': ['青龙县', '卢龙县', '昌黎县'],
    },

    '江苏省': {
        '南京市': ['江宁县', '江浦县', '高淳县'],
        '苏州市': ['昆山县', '吴江县', '太仓县'],
        '徐州市': ['铜山县', '丰县', '沛县'],
    },
}

current_layer = menu
father_layer = []                                # 保存所有父级目录， 最后一个元素永远是父亲级
while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:
        continue
    elif choice in current_layer:
        father_layer.append(current_layer)       # 进入下一层目录时，把当前层（就是下一层的父亲级）添加到列表
        if len(father_layer) < 3:
            current_layer = current_layer[choice]   # 改为子层
        else:                                   # 如果用户想查看县下面的镇，这里就会告诉他，县就是最后一级了。不写这句会报错！
            print("\033[31;1m已经是最后一层菜单,b返回上级。\033[0m")
            father_layer.pop()
    elif choice == 'b':
        if father_layer:
            current_layer = father_layer.pop()   # 用户选择b返回时，直接取最后一个元素，就是父亲级目录(并且删除了最后一个元素)
    else:
        print("\033[31;1m没有此项！\033[0m")



