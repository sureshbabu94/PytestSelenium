from datetime import datetime
import os
class Invoke:
    def __init__(self, driver):
        self.driver = driver
    #@staticmethod
    def takesnapshot(fun):
        def subfun(self):
            fun(self)
            t = datetime.now()
            #print("t:" + str(t))
            strdate=t.strftime("%d-%m-%Y")
            p = t.strftime("%d-%m-%Y-%H-%M-%S-%f")
            path = "C:/PythonProjects/scr"
            try:
                os.chdir(path)
                NewFolder = 'Results_' + strdate
                os.makedirs(NewFolder)
                self.driver.save_screenshot(NewFolder + '/'+fun.__name__+'.png')
            except FileExistsError:
                self.driver.save_screenshot(NewFolder + '/' + fun.__name__ + '.png')

            print("Took Screenshots..........")

        return subfun