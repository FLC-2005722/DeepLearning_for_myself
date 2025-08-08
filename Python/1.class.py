# 1.class的定义
class Animal:
    '''
    Animal类的定义
    __init__方法是类的构造函数，用于初始化对象的属性
    self表示对象本身，访问属性和方法必须通过self
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def speak(self):
        print(f"{self.name} is speaking")
