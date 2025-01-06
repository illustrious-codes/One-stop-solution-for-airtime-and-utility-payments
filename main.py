def fibonacci(length):
    init = 1
    state = 1
    print(end=" ")
    for _ in range (length):
        state = state + init
        init = state - init
        print(init, end=" ")

num = int(input("How long do you want to run this ? "))
fibonacci(num)
print("Happy New Year Famz")