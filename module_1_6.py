my_dict={'Lena':1999,'Egor':2002,'Alina':2001}
print(my_dict)
print(my_dict['Egor'])
print(my_dict.get('Anya'))
my_dict['Vasya']=1998
my_dict['Petya']=2000
print(my_dict)
a=my_dict.pop('Egor')
print(a)
print(my_dict)

my_set={1,2,3,'raspberry',12.125}
print(my_set)
print(my_set.add(6))
print(my_set.add('Apple'))
print(my_set)
print(my_set.remove(6))
print(my_set)