
# json的方法
`json.dumps`方法可以将Python对象转换为一个表示JONS数据的字符串
```
dumps(obj: Any, skipkeys: bool=..., ensure_ascii: bool=..., check_circular: bool=..., allow_nan: bool=..., cls: Optional[Type[JSONEncoder]]=..., indent: Union[None, int, str]=..., separators: Optional[Tuple[str, str]]=..., default: Optional[Callable[[Any], Any]]=..., sort_keys: bool=..., **kwds: Any) 
```

`json.loads`方法可以将包含了一个JSON数据的str, bytes或者bytearray对象, 转化为一个Python Dictionary.
```
loads(s: _LoadsString, encoding: Any=..., cls: Optional[Type[JSONDecoder]]=..., object_hook: Optional[Callable[[Dict[Any, Any]], Any]]=..., parse_float: Optional[Callable[[str], Any]]=..., parse_int: Optional[Callable[[str], Any]]=..., parse_constant: Optional[Callable[[str], Any]]=..., object_pairs_hook: Optional[Callable[[List[Tuple[Any, Any]]], Any]]=..., **kwds: Any)
```

# 数据类型转换

JSON可以表示四种主类型数据

1.字符串 string

2.数字 number

3.布尔类 boolean

4.空值 null

以及两结数据结构

1.对象 object

2.数组 array

默认实现中, JSON和Python之间的数据转换对应关系如下表:

Python编码为JSON类型转换对应表

|  Python   | JSON  |
|  ----  | ----  |
| dict  | object |
| list,tuple  | array |
| str  | string |
| int, float, int- & float-derived Enums  | number |
| True  | true |
| False  | false |
| None  | null |

JSON解码为Python类型转换的对应表

|   JSON  | Python  |
|  ----  | ----  |
| object  | dict |
| array  | list |
| string  | str |
| number(int)  | int |
| number(real)  | float |
| true  | True |
| false  | False |
| null  | None |