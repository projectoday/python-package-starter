# I have to say: python 的模块系统没有 javascript 的好。。。

## Goal:

在 src 目录下：

* 执行main.py(其中import了各个pkg的module): `python main.py`
* 单独执行pkg下的某个module: `python -m pkg1.mod1`
* 兄弟pkg间可以相互import module
* 能够单独执行test下的某个module的test用例: `python -m test.testmod1`
* 能够一次执行test下的所有module的test用例: `python -m unittest discover test`

## Thanks:

https://docs.python.org/2/tutorial/modules.html

http://tonybai.com/2013/01/24/the-module-import-way-under-python-package/
