from _typeshed import Self
from pythonProject.src.Driver import Drvier

class Quit_close(Drvier):
    """app关闭或驱动关闭"""
    driver = Drvier().driver

    def app_close(self):
        """退出app"""
        self.driver.close_app()

    def driver_close(self):
        """关闭确app驱动"""
        self.driver.quit()