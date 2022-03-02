from datetime import datetime
def decofun(fun):
    def subfun():
        fun()
        t = datetime.now()
        print("t:" + str(t))
        p = t.strftime("%d-%m-%Y-%H-%M-%S-%f")
        self.driver.save_screenshot("C:/PythonProjects/scr/flipkarthome-" + p + ".png")
        print("Took Screenshots..........")
    return subfun

@decofun
def furios():
    print("fun")

