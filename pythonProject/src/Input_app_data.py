# from pythonProject.src.test import Path

class Input_phone_data(object):
    """用户输入手机数据"""
    desired_caps = {
        "platformName":"",
        "platformVersion":"",
        "deviceName":"",
        "appPackage":"",
        "appActivity":"",
        "unicodeKeyboard":"",
        "resetKeyboard":""
    }
    for (key, value) in desired_caps.items():
        result = input("请输入" + key + ":")
        desired_caps[key] = result

    print(desired_caps)
        
    
