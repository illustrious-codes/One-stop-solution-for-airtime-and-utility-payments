# print("What ever you do consistency with your life became your habit")
# print(20 % 6)
# number = 44
# number2 = str(number)
# print(type(number2))
# print(f"I am David, in am {number2} years old")
# bag = "Cas"
# watch = "Elun Musk"
# food = "Cas"

# age = input("How old are you    ")

# if age == 40:
#     print(age + 10)
    
# else:
#     while True:
#         print("Enter a number...")
#         age = input("How old are you    ")

# def get_age():
#     while True:
#         try:
#             age = int(input("Enter your age  "))
#             return age + 10
#         except ValueError:
#             print("your age must a number")

# print(get_age())


def fibonacci(length):
    initial_status = 1
    initial_state = 1
    for i in range(length):
        initial_state = initial_state + initial_status
        initial_status = initial_state - initial_status
        num = initial_status
        print(num, end=" ")

num = int(input("Enter number range  "))
fibonacci(num)