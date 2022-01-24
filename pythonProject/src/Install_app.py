import os,sys
sys.path.append(os.getcwd())
from pythonProject.src.Driver import Drvier

class Install_app(Drvier):
    """安装卸载app"""
    Drvier = Drvier()
    driver = Drvier.driver

    if driver.is_app_installed('com.shusheng.qyt'):
        try:
            print("该软件已存在!")
            result = str(input("是否卸载当前版本的软件(y/n):"))
            while(True):
                if "y" == result or "Y" == result:
                    print("正在卸载当前版本....")
                    driver.remove_app('com.shusheng.com')
                    print("卸载已完成")
                    break
                
                elif "n" == result or "Y" == result:
                    print("好的!已保留该软件")
                    while(True):
                        results = str(input("是否退出程序(y/n):"))
                        if "y" == results or "Y" == results:
                            print("正在退出程序....")
                            driver.quit()
                            print("程序已退出!")
                        elif "n" == results or "N" == results:
                            print("抱歉!程序暂时无其他功能,程序正在退出....")
                            driver.quit()
                            print("程序已退出!")
                        else:
                            print("请按规则输入!")
                
                else:
                    print("请按规则输入!")


        except:
            ...
