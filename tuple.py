# # my_list = [1,2,3,4,5]
# # my_list[0]=99
# # print(my_list)

# # my_tuple = [99,8,1,2,3,4,5]
# # my_tuple2 = [1,3,4,5,]
# # print(my_tuple+my_tuple2)
# # count_1 = my_tuple
# # print(my_tuple)

# # new_tuple = sorted(my_tuple, reverse=True)
# # print(new_tuple)
# # print(type(new_tuple))
# # print(type(tuple(new_tuple)))
# # print(min(new_tuple))
# # print(max(new_tuple))

# # my_tuple = (10, 20, "a", "b", True)
# # print(my_tuple)
# # print(my_tuple[3])
# # tuple_1 = [1, 2, 3]
# # tuple_2 = ['x', 'y', 'z']
# # conc_tuple = (tuple_1+tuple_2)
# # print(conc_tuple)
# # repeated_tuple= ((my_tuple)*3)
# # print(repeated_tuple)
# # print(len(conc_tuple))
# # sliced_tuple = my_tuple[2:5]
# # print(sliced_tuple)

# my_dist = {
#     "Name" : "Shradeep",
#     "Age" : "17",
#     "Address" : {
#         "Address1":"Bhaktapur", 
#         "Address2":"Suryabinayak"
#     }
# }
# # print(my_dist)
# # print(my_dist["Address"])

# # print(my_dist["Age"])
# # del my_dist["Age"]
# # print(my_dist)
# print(my_dist["Name"] ["Age"])

#WAP to show multiplication of first 20 prime numbers using nested for loop
# def prime_num(a):
# def mult_num(b):
#     for i in range (2,25):
#         for i in range(2,int(a/2)+1):
#             if a%i==0:
#                 print("not prime")

#                 return False
#         if prime_num():
#             print("prime")
#         print(f"{b}*{i}={b*i}")
#     print("----------------------") 
# mult_num()

# def is_prime(number):
    
#     if number < 2:
#         return False
#     for i in range(2, int(number**0.5) +1):
#         if number % i == 0:
#             return False
#     return True

# count=0
# number=1
# prime_list=[]
# while count<20:
#     if is_prime(number):
#         prime_list.append(number)
#         count=count+1
#     number=number+1
# print(prime_list)
# def mult_num(number):
#     for i in range (1,11):
#         print(f"{prime_list}*{i}={prime_list*i}")
#     print("--------------------") 
# mult_num(prime_list)






#number = int(input("Enter a number: "))


# if is_prime(number):
#     print(number, "is a prime number.")
# else:
#     print(number, "is not a prime number.")
 

# list=[]
# for j in range(2,30):
#     prime=1
#     for i in range(2,j):
#         if j%i==0:
#             prime=0
#             break
#     if prime==1:
#         list.append(j)
# print(list)

#WAP to find perimeter of rectangular ground.
#WAP to find volume of irregular body.
#WAP to find simple interest.
#WAP to calculate volume of a cube.
#WAP to find square root of a number.
#WAP to find error percentage.
#take a string from a user as a input and check weather the string is Shraddha khatri or not.

#Simple interest:
# p = int(input("Enter a number:"))
# t = int(input("Enter another number:"))
# r = float(input("Enter a number:"))
# Si_int = (p*t*r)/100
# print("The simple interest is:",Si_int)

#rectangular
# l = int(input("Enter a number:"))
# b = int(input("Enter a number:"))
# perimeter = 2*(l+b)
# print("The perimeter of rectangular ground is:",perimeter)

#Irregular body
initial_vol = int(input("Enter a number:"))
final_vol = int(input("Enter a number:"))
volume = initial_vol - final_vol

print("volume of irregular body is:",volume)





