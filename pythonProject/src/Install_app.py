from pythonProject.src.Driver import Drvier
from pythonProject.src.Input_app_data import Input_phone_data




class Install_app(Drvier):
    """安装卸载app"""
    Input_phone_data = Input_phone_data()
    driver = Drvier().driver
    print('正在验证手机是否')
    while(True):
        if driver.is_app_installed:
            ...
