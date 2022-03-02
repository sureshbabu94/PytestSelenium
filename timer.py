from datetime import datetime
import time
t=None
def test():
    t=datetime.now()
    print("t:"+str(t))
    p=t.strftime("%d-%m-%Y-%H-%M-%S-%f")
    print("p:"+p)


def tester():
    time.sleep(1)
    t = datetime.now()
    print("t:" + str(t))
    p = t.strftime("%d-%m-%Y-%H-%M-%S-%f")
    print("p:" + p)

test()
tester()