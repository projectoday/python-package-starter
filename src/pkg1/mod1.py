import pkg2.mod2

def sayHi():
    print 'Hi, I am inside mod1 of pkg1!'
    pkg2.mod2.sayHi()

print 'Always get excuted in mod1.'
