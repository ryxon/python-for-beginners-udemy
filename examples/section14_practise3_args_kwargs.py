def targs(*args):
    print(args)

def tkwargs(**kwargs):
    print(kwargs)

def dblArgs(*args, **kwargs):
    print('args:', args)
    print('kwargs', kwargs)

#use of * and ** in the function is to recognize and 'catch':
# either single seperated values (1,2,3,4)
# or dictionality values (name:'ryan', age:'38')
# but when calling the function as dblArgs(*numbers,**dict1)
# the * and ** serve the purpose of setting the right structure of data

targs(123213,12312,312,312,3,123,12,312,3)
tkwargs(name="ryan",test='12312321')

numbers = [123123,12312312,312312312,31212]
dict1 = {'firstname':'john','lastname':'cena','professions':'pythonprogrammer'}

dblArgs(*numbers,**dict1)