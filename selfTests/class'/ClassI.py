# 新建一个名叫User的类
class User:
    def __init__(self,name,id,age,sex):
        self.__name = name
        self.__id = id
        self.__age = age
        self.__sex = sex

    def print_info(self):
        print(f'I am a user:{self.__name}|{self.__id}|{self.__age}|{self.__sex}')

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

    def get_sex(self):
        return self.__sex

    def set_sex(self,sex):
        self.__sex = sex
