marks = [2,46,67,99]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 2):
#         print("Prince Awesome")
# index += 1

#BETTER WAY


for index, mark in enumerate(marks):
    print(mark)
    if(index == 2):
        print("Prince Awesome")
index += 1