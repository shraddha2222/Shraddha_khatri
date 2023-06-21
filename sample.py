# # #Wap to print even numbers between between 2 and 50 also perform the addition of those even numbers
# # #def even_numbers():
# #     #for i in range(2,50)
# #     #if i%2==0:
# #         #sum= i+1
# #         #print
# #         #print(sum)


# # sum_even = 0
# # for i in range(2, 50 + 1):
# #     if i % 2 == 0:
# #         print(i)
# #         sum_even += i

# # print("Sum of even numbers:", sum_even)

# # sum_odd = 0
# # for i in range(2, 50+1):
# #     if i % 2 != 0:
# #         print(i)
# #         sum_odd += i
# # print("Sum of odd numbers:", sum_odd) 

# # #write a program to check if a number is prime number or not
# # #def prime_num():
# #    # a=int(input("Enter a number:"))
# #     #for i in range(2,a):
# #         #if a % i == 0:
# #            # print(a, "is not a prime number")   
# #         #else:
# #             #print(a, "is a prime number")
# #             #break
# # #prime_num()
            
# # def is_prime(num):
    
# #     if num <= 1:
# #         return False

   
# #     for i in range(2, num):
# #         if num % i == 0:
# #             return False

# #     return True


# # number = int(input("Enter a number: "))


# # if is_prime(number):
# #     print(number, "is a prime number.")
# # else:
# #     print(number, "is not a prime number.")


# # def check_prime(a):
# #     for i in range(2,int(a/2)+1):
# #         if a%i==0:
# #             print("not prime")
# #             return False
# # if check_prime(11):
# #     print("prime")
 
# #WAP to give the multiplication table of 5,10,17
# # def mult_num(a):
# #    for i in range (1,11):
# #      print(f"{a}*{i}={a*i}")
# #    print("--------------------") 
# # mult_num(5)
# # mult_num(10)
# # mult_num(17) 
 

# # my_string = "This is python programming"
# # print(my_string[::-1])

# # user_inp = input("Enter your name : ")
# # print(type(user_inp))
# # print("Hi {},How are you?".format(user_inp))

# # print(f"Hi {user_inp}, your name has {len(user_inp)} characters")
# # print(f"Hi {user_inp.lower()}, your name has {len(user_inp)} characters")
# # print(f"Hi {user_inp.upper()}, your name has {len(user_inp)} characters")

# # message = "Hi Shraddha"
# # msg = message.replace("Hi","Hello")
# # print(msg)

# #1
# # user_name = input("Enter a name:")
# # fav_col = input("Enter your Favourite colour:")
# # print(f"Hi {user_name}, your favourite colour is {fav_col}")

# #2
# # user_inp = input("Enter a sentence:")
# # splitted = user_inp.split(" ")
# # print(splitted)
# # print(f"Your sentence has {len(splitted)} characters.")

# #3
# # full_name = input("Enter your full name:")
# # fname,lname = full_name.split(" ")
# # print(f"{lname.upper()}, {fname.upper()}")

# #4
# # user_in = input("Enter a sentence:")
# # rep_word = input("Enter a word to be replaced:")
# # word_rep = input("Enter the replacement word:")
# # message = user_in.replace(rep_word, word_rep)
# # print(message)

# #LIST
# my_list = ["Mango", "Litchi", "Tomato", "Onion"]
# #print(my_list[-4])
# #my_list[0]="Coffee"
# #print (my_list)
# #my_list.append("Coffee")
# #my_list.insert(4,"Coffee")
# #my_list.remove(my_list[3])
# #my_list[3]= "Milk"
# #my_list.insert(5,"Chocolate")
# #my_list.append("Chocolate")
# #forgot = my_list.pop(2)
# #print(f"I forgot : {forgot}")
# #my_list.sort(reverse=True)
# #my_listl = ["Noodle", "Biscuit", "Cake", "Bread"]

# #print (my_list+my_listl)
# #forgot = my_list.pop[1]
# #print (my_list)

# #1
# num_list = [1, 2, 3, 5, 7, 9]
# print(num_list)



# #2
# print(num_list[3])

# #3
# num_list[3]=10
# print(num_list)

# #4

# num_list.insert(7, 12)
# print(num_list)

# #5
# num_list.remove(num_list[4])
# print(num_list)

# #6
# sliced_list= num_list[2:5]
# print(sliced_list)

# #7
# combined_list = (num_list+sliced_list)
# print(combined_list)

# #8
# print(8 in num_list)

# #9
# combined_list.sort()
# print(combined_list)

# #To remove repeated items from list
# combined_list = list(dict.fromkeys(combined_list))
# print(combined_list)
















     















 


