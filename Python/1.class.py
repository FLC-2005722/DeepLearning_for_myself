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
        print(f"{self.name} is making a sound.")

# 2.创建对象
dog = Animal("Dog", 5)
print(dog.name)  # 输出: Dog
print(dog.age)   # 输出: 5
dog.speak()      # 输出: Dog is speaking

# 3.继承类
class Dog(Animal):
    '''
    Dog类继承自Animal类
    可以重写父类的构造函数
    '''
    def speak(self):
        print(f"{self.name} says Woof!")

# 4.调用父类的方法
class Dog(Animal):
    '''
    Dog类继承自Animal类
    可以调用父类的构造函数和方法
    '''
    def speak(self):
        super().speak()  # 调用父类的speak方法

dog = Dog("Buddy", 3)
dog.speak() 