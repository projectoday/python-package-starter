import pkg2.mod2

def sayHi():
    print 'Hi, I am inside mod1 of pkg1!'
    pkg2.mod2.sayHi()

print '单独执行时只有我'
