from typing import Dict,Tuple,Set,List,Union


list_one : List[str] = ["hello", "world"]
tuple_one: Tuple[str]= ("hello","world" )
tuple_two:Tuple[int] = (3,10,25)
set_one:Set[str]=("hello","world" )
dict_one:Dict[int,str|int]={"name":"sultan","age":20,"home":"manikganj"}

merged_tuple:Union[str,int]=tuple_one+tuple_two
print( type(merged_tuple))

num :int=5
name:str="sultan"

def sum (num1:int, num2:int) -> int: 
  sum= num1 + num2
  print(sum)
  return sum


sum(5 , 2)

dict_1 = {"name": "sultan","age":"25"}
dict_2={"home":"maninganj","phone number":"123"}

merged_dict = dict_1 | dict_2
print(type(merged_dict))