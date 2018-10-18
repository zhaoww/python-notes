# -*-coding:utf-8-*-

class Test:
	lv = 11
	def __init__(self, name, age, sex):
		self.name = name # public
		self._age = age
		self.__sex = sex # private
	def get_sex(self): # getter
		return self.__sex
	@classmethod
	def get_name(self):
		return self.name
	@property
	def get_age(self):
		return self._age
t = Test('tom', 23, 1)
print(t.name)
print(t._age)
print(t.get_sex())
# 直接使用类名类调用，而不是某个对象
print(Test.lv)
# 像访问属性一样调用方法
print(t.get_age)


# 继承 支持多继承 class ClassName(Base1,Base2,Base3):
# 可重写父类方法
class childTest(Test):
	pass

ct = childTest('child', 24, 0)
print(ct.get_sex())
