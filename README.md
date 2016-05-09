# I have to say: python 的模块系统没有 javascript 的好。。。

## Goals:

在 src 目录下：

* 执行 main.py (其中 import 了各个 pkg 的 module): `python main.py`
* 单独执行 pkg 下的某个 module (其中 import 了其它 pkg 的 module): `python -m pkg1.mod1`
* 能够单独执行 test 下的某个module的test用例: `python -m test.testmod1`
* 能够一次执行 test 下的所有module的test用例: `python -m unittest discover test`


## Questions:

### 关于 module 和 package：

A **module** is a file containing Python definitions and statements.

**Packages** are a way of structuring Python’s module namespace by using “dotted module names”.

The `__init__.py` files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package or set the `__all__ `variable


## Thanks:

https://docs.python.org/2/tutorial/modules.html

http://tonybai.com/2013/01/24/the-module-import-way-under-python-package/
