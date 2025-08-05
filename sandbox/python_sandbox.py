from enum import Enum, auto

print("hello")

# messages = [
#     "a",
#     "ab",
#     "abcd",
#     "a",
#     ""
# ]

# print(max(messages, key=lambda mes : len(mes)))
# print(len(max(messages, key=lambda mes : len(mes))))

#日本語変数 = "日本語だよ"
#print(日本語変数)

# キャラ = {
#     '舞香': {
#         '右': { '北': [0,0], '東': [16,0], '西': [32,0], '南': [48,0] },
#         '左': { '北': [0,0], '東': [0,16], '西': [0,32], '南': [0,48] }
#     }
# }

# print(キャラ['舞香']['右']['北'])

# class Hoge:
#     def __init__(self, name):
#         self.name = name

#     def call_name(self):
#         print(self.name)

#     def change_name(self, new_name):
#         self.name = new_name

# list = [Hoge("1"), Hoge("2"), Hoge("3")]
# for hoge in list:
#     hoge.call_name()

# for hoge in list:
#     hoge.change_name("new name")
#     hoge.call_name()

# dict ={
#     'うたう': ['まーめいど', 'きあらたすけにきたぞ'],
#     'あいてむ': ['ぬいぐるみ']
# }

# print(max(dict, key=len))

# print({1,2} < {1,2,3})  # True

# print({(1,2)} <={ (0,1),(0,2),(1,0),(1,2)}) # True 
# print({(1,1)} <={ (0,1),(0,2),(1,0),(1,2)}) # False

# dict = {
#     '(0,1),(0,2),(1,0),(1,2)': 0,
#     '(0,2),(0,4),(3,0),(3,5)': 1
# }

# def print1():
#     print("1")
#     print("2")


# dicdic = { '1' : ("hoge", print1)}
# print(dicdic['1'][0])  # Access the first element of the tuple
# dicdic['1'][1]()  # Call the function stored in the tuple

# dicdicdic = { '1' : ("hoge", lambda: print("foo"))}
# print(dicdicdic['1'][0])  # Access the first element of the tuple
# dicdicdic['1'][1]()  # Call the lambda function stored in the tuple

# menu = [
#     ("1", lambda: print(1)),
#     ("2", lambda: print(2)),
#     ("3", lambda: print(3)),
#     ("4", lambda: print(4)),
# ]

# menu[0][1]()  # Call the function associated with the first item

# action = [
#     ("歩く", lambda: print("歩く処理"), lambda: print("歩く描画")),
#     ("立ち止まる", lambda: print("立ち止まる処理"), lambda: print("立ち止まる描画")),
# ]

# for name, process, draw in action:
#     print(f"Action: {name}")
#     process()  # Call the process function
#     draw()     # Call the draw function
#     print("---")

num = [ ("1", None) , ("12", None) , ("123", None) , ("1234", None) ]
print(len(max(num, key=lambda x: len(x[0]))[0]))