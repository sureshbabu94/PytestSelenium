from jproperties import Properties
#class
configs = Properties()
with open('./webelements/web.properties', 'rb') as config_file:
            configs.load(config_file)

def geturl():
    return configs.get("URL").data

def getimplicitwait():
    return configs.get("IMPLICIT_WAIT").data

def getlocator(webelement):
    return configs.get(webelement).data







