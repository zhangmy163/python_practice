# ex1

```
|__
   |__module1.py
   |__run.py

run.py调用module1.py中的方法
```
调用其他py文件的方法(同级目录)  
`from 文件名 import 方法名`下面可以直接使用该方法   
`import 文件名`下面使用方式时需要带上文件名，如<文件名.方法名>

# ex2

```
|__
   |__module1.py
   |__run.py

run.py调用module1.py中的类
```
调用其他py文件的类(同级目录)
`from 文件名 import 类名`下面可以直接使用该类   
`import 文件名`下面使用方式时需要带上文件名，如<文件名.类名>

# ex3

```
|__
   |__M1
        |__module1.py
   |__run.py

run.py调用module1.py中的方法
```
`from 文件夹.文件名 import 方法名`下面可以直接使用该类   
`import 文件夹.文件名`下面使用方式时需要带上文件名，如<文件夹.文件名.方法名>

# ex4

```
|__
   |__M1
        |__module1.py
   |__M2
        |__module2.py
   run.py

module2调用所在目录同级的目录M1的py文件时，M2需要有__init__.py文件，另外需要把ex4目录加到path里

from os import path,sys
d = path.dirname(__file__)
parent_path = path.dirname(d)
sys.path.append(parent_path)

from M1 import module1

```

# ex5

```
|__
   |__M1
        |__module1.py
   |__M2
        |__module2.py
   run.py
利用__init__.py导包，在调用时可以减少路径
通过调M2文件夹下的__init__.py中from M2.module2 import *，下方再使用module2.py的方法，则可以不跟文件名
```
