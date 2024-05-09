fun_list1 = []
for i in range(5):
	def fun1(e):
		return e+i
	fun_list1.append(fun1)

fun_list2 = []
for i in range(5):
	def fun2(e, iv=i):
		return e+iv
	fun_list2.append(fun2)

fun_list3 = [lambda e: e+e for i in range(5)]

fun_list4 = [lambda e, iv=i: e+iv for i in range(5)]

i=55
#list1 through list4
print([f(10) for f in fun_list1])
print([f(10) for f in fun_list2])
print([f(10) for f in fun_list3])
print([f(10) for f in fun_list4])
