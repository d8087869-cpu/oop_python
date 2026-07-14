#1 it ensuer that a class has exactly one instance . and that instance is shaerd 
#2# only one because if will be few what will be the True one , and all are connected to one 
#3  any part of the program can ask for the singleton and get back the same object
#4 because its over rides the first calling and return existing info 
#5 it could be change by other and evry thing depends on the singletone

#1
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new Logger instance...")
            cls._instance = super().__new__(cls)
        return cls._instance

logger1 = Logger()
logger2 = Logger()

print("Logger1:", id(logger1))
print("Logger2:", id(logger2))
print("Same object?", logger1 is logger2)
#2
class AppSettings:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.theme = "dark"
        return cls._instance
settings1 = AppSettings()
settings2 = AppSettings()
settings1.theme = "light"
print("Theme from second object:", settings2.theme)
