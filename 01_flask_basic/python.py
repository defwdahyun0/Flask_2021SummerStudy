#nested function
# 중첩 함수

def outer_func():
    print("call outer_func function")
    def inner_func():
       return ' call inner_func function'
    print(inner_func())

# first-class function
# 함수 자체를 변수에 저장

