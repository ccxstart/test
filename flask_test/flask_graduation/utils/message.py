status_msg = {
    200: '成功',
    10005: '用户名或密码错误',
    10000: '数据不完整',
    10011: '用户名不合法',
    10012: '密码不合法',
    10013: '两次输入密码不一致',
    10014: '手机号格式不正确',
    10015: '邮箱格式不正确',
    10016: '请登录后操作',
    10017: 'token不可使用',
    10018: '修改用户错误',
    10019: '删除错误',
    10020: '修改的角色不存在',
    10021: '用户名已存在',
    20000: '异常错误',
    20001: '无数据'
}
# 100010-100019  用户名错误


def to_dict_msg(status=200, data=None, msg=None):
    return {
        'status': status,
        'data': data,
        'msg': msg if msg else status_msg.get(status)
    }


def to_dict_msg_min_max(status=200, data=None, msg=None, min=None, max=None):
    return {
        'status': status,
        'data': data,
        'min': min,
        'max': max,
        'msg': msg if msg else status_msg.get(status)
    }


if __name__ == '__main__':
    print(to_dict_msg(200))
