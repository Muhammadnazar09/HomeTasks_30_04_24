# Сикли беохир, ёфтани ҳарфу рақам, манъ кардани сикли беохир.
#while True:
#     m=input()
#     print(m)


# while True:
#     m=input()
#     if m=="25":
#         break
#     print(m)


# while True:
#     m=input()
#     try:
#         # int(m)
#         float(m)
#         print("Number")
#     except:
#         print("String")


# def TextOrNumber(m):
#     try:
#         int(m)
#         print("Number")
#     except:
#         print("Erorr")
# while True:
#     n=int(input())
#     if n=="25":
#         break
#     TextOrNumber(n)


# def is_number(m):
#     try:
#         int(m)
#         return True
#     except:
#         return False
# cnt=0
# while True:
#     n=input()
#     if is_number(n):
#         cnt+=int(n)
#     else:
#         print("Error")
#     if n=="25":
#         break
# print(cnt)


while True:
    m=input()
    if m>="A" and m<="Z" or m>="a" and m<="z":
        print(f"{m} is a alfabit")
    else:
        print(f"{m} is a number")