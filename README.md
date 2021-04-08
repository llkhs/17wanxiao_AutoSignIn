# 💧广东水利电力学院 Perfect校园 签到

- 

**😀2021.02.11 添加QQ邮箱推送，请在qqmail.py文件修改邮件发送方**

**😁2021.02.05 没时间解释了，快上车！！！！！**

**😡2021.01.29 完校服务器把github的ip给ban了，解决办法是代码加入http代理**

😀**2021.01.26 修复了Server酱微信推送出错的问题.**

😀**2021.01.22 打卡信息自动填写为上一次打卡的信息，Secret部分只需要填[账号和密码]即可**

😀**2021.01.07 对应学校的模板更新，添加寒假去向三项**

😀**2020.12.01 需要指定监护人名字，请从Secret字段添加监护人信息，格式看下面。**

😁**2020.11.29 修改了提交接口。**

**💧在[原Project](https://github.com/srcrs/Perfect_Campus_AutoSignIn)的基础下添加对[广东水利电力学院](https://www.gdsdxy.edu.cn/)的可用性，对 [srcrs](https://github.com/srcrs)的贡献表示感谢。**

欢迎大家 fork 测试使用，如果可用的话，可以开 [issue](https://github.com/llkhs/Perfect_Campus_AutoSignIn/issues) 让更多人知道

感谢 [@zhongbr](https://github.com/zhongbr) 的完美校园逆向登录分析代码的分享：[完美校园模拟登录](https://github.com/zhongbr/wanmei_campus)



# 简介

广东水利电力学院Perfect校园每日自动签到，从此让你解放双手，支持多用户批量签到。
基于Github Actions，无需服务器或设备。


# 功能

- 完美校园签到

- 支持多用户批量签到

- 支持推送运行结果至微信(使用`server`酱)

- 随机温度，随机经纬度(在合适的范围内)

# 使用方法

## 准备

- 完美校园`APP`账号(需要手机号和密码,若未使用过，需在App修改密码并手动打一次卡)

- 模拟器用验证码的方式登录一遍完美校园，获取模拟器的IMEI码，在 [campus.py 第45行](https://github.com/llkhs/17wanxiao_AutoSignIn/blob/56bf0f3400bd2138b9899c2622020d3a31a44296/campus/campus.py#L45) 填入值(很重要)

- 若需推送至微信，请注册 [server酱](http://sc.ftqq.com/)，并获取其`SCKEY`

## 1.Fork本项目



## 2.开启Antions(默认你的Actions是处于禁用状态)




## 3.将个人信息添加至Secrets

Name | Value
-|-
USERS | 手机号,密码,通知方邮箱,发件方授权码,SCKEY

多用户的`Value`格式如下：

```sh
手机号1,密码1,通知方邮箱1,发件方授权码,SCKEY
手机号2,密码2,通知方邮箱2,,
手机号3,密码3,通知方邮箱3,,
手机号4,密码4,,,
手机号5,密码5,,,
手机号6,密码6
```
`,` 是英文逗号

有缺省项注意行后面`,`的个数，`发件方授权码`登录QQ邮箱账户设置获取

如需使用 [server酱](http://sc.ftqq.com/) 推送至微信，按照官网教程注册，获取其`SCKEY`。只需要在第一个用户的后面添加即可。

如不需请留空，注意不要将其前面的`,`删除了。



## 4.第一次运行actions

只需要一个`push`操作就会触发`actions`运行

将项目`poinMe.txt`文件中的`flag`值由`0`改为`1`即可。

```patch
- flag: 0
+ flag: 1
```



## 大功告成

以后每天会在6:00进行自动签到。(会延迟20分钟)


## ~~如果你来自其它学校，可能某些参数不一样而打卡失败，可以试着抓包看看打卡时请求的表单，再修改对应的参数。~~
## 也不用抓包了，支持自动填写，其他学校的自测。
(抓包抓得好，🍚牢饭少不了)

 <img src="assets/img/E7537C28-185B-4E55-887D-1B56BD78C7F0.jpeg" width="300" alt="抓包结果" title="抓包抓得好，牢饭少不了"/><br/>


## About
- 免责声明：此仓库仅用于我个人储存17wanxiao打卡记录，仅供个人研究/学习/欣赏，他人可参考，请勿用于商业用途，否则产生的一切后果将由您自己承担，例如他人盗用本仓库代码用于商业用途或侵犯国家、社会、企业利益和公民的合法权益等。再次我本人不承担任何责任，此仓库仅用于我个人储存代码，仅此而已）




## 参考项目

[HAUT_autoCheck](https://github.com/YooKing/HAUT_autoCheck)

[wanmei_campus](https://github.com/zhongbr/wanmei_campus)

[Perfect_Campus_AutoSignIn](https://github.com/srcrs/Perfect_Campus_AutoSignIn)

[17wanxiaoCheckin-Actions](https://github.com/ReaJason/17wanxiaoCheckin-Actions)
