import time
import json
import requests
import datetime
from campus import CampusCard


def main():
    # sectets字段录入
    sckey, success, failure, result, phone, password = [], [], [], [], [], []

    # 多人循环录入
    while True:
        try:
            users = input()
            info = users.split(',')
            phone.append(info[0])
            password.append(info[1])
            sckey.append(info[2])
        except BaseException:
            break
    # 提交打卡
    count, msg, run = 0, "null", False
    print("-----------------------")
    for index, value in enumerate(phone):
        print("开始获取用户%s信息" % (value[-4:]))
        while count < 3:
            try:
                campus = CampusCard(phone[index], password[index])
                token = campus.user_info["sessionId"]
                time.sleep(1)
                res = check_in(token).json()
                strTime = GetNowTime()
                if res['code'] == '10000':
                    success.append(value[-4:])
                    msg = value[-4:] + "-打卡成功-" + strTime
                    result = res
                    run = False
                    break
                else:
                    failure.append(value[-4:])
                    msg = value[-4:] + "-失败-" + strTime
                    count = count + 1
                    print('%s打卡失败，开始第%d次重试...' % (value[-4:], count))
                    result = res
                    time.sleep(60)

            except Exception as err:
                print(err)
                msg = '出现错误'
                failure.append(value[-4:])
                break
        print(msg)
        print("-----------------------")
    fail = sorted(set(failure), key=failure.index)
    title = "成功: %s 人,失败: %s 人" % (len(success), len(fail))
    for _ in range(1):
        try:
            if not (sckey is None) & run:
                print('开始Wechat推送...')
                WechatPush(title, sckey[0], success, fail, result)
                break
        except:
            print("WeChat推送出错！")


# 时间函数
def GetNowTime():
    cstTime = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    strTime = cstTime.strftime("%H:%M:%S")
    return strTime


# 打卡参数配置函数
def GetUserJson(token):
    sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"
    user_json = {
        "jsonData": {
            "templateid": "pneumonia",
            "token": token
        },
        "businessType": "epmpics",
        "method": "userComeApp"
    }
    res = requests.post(sign_url, json=user_json, verify=False).json()
    data = json.loads(res['data'])
    post_dict = {
        "add": data['add'],
        "areaStr": data['areaStr'],
        "businessType": "epmpics",
        "method": "submitUpInfo",
        "jsonData": {
            "deptid": data['deptStr']['deptid'],
            "gpsType": 1,
            "userid": data['userid'],
            "stuNo": data['stuNo'],
            "source": "app",
            "templateid": data['templateid'],
            "token": token,
            "reportdate": round(time.time() * 1000),
            "username": data['username'],
            "phonenum": data['phonenum'],
            "customerid": data['customerid'],
            "deptStr": data['deptStr'],
            "areaStr": data['areaStr'],
            "updatainfo": [{"propertyname": i["propertyname"], "value": i["value"]}
                           for i in data['cusTemplateRelations']],
        }
    }
    # print(post_dict)
    return post_dict


# 打卡提交函数
def check_in(token):
    sign_url = "https://reportedh5.17wanxiao.com/sass/api/epmpics"
    jsons = GetUserJson(token)
    # print(jsons)
    # 提交打卡
    time.sleep(2)
    res = requests.post(sign_url, json=jsons, timeout=10)
    print(res.json())
    return res


# 微信通知
def WechatPush(title, sckey, success, fail, result):
    send_url = f"https://sc.ftqq.com/{sckey}.send"
    strTime = GetNowTime()
    # if not fail:    # 花里胡哨的
    #     fail = ["我见青山多妩媚"]
    #     fail = ''.join(fail)
    page = json.dumps(result, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)
    content = [f"""`{strTime}`
#### 打卡成功用户:
`{success}`
#### 打卡失败用户:
`{fail}`
#### 主用户打卡信息:
```
{page}
```"""]
    data = {
        "text": title,
        "desp": content
    }
    try:
        req = requests.post(send_url, data=data)
        if req.json()["errmsg"] == 'success':
            print("Server酱推送服务成功")
        else:
            print("Server酱推送服务失败")
    except:
        print("Server酱推送异常")


if __name__ == '__main__':
    main()
