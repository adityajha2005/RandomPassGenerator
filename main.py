#Way-1
import random
password="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}|:/.,abcdefghijklmnopqrstuvwxyz"
length_password=int(input("Enter the length of password : "))
a="".join(random.sample(password,length_password))
print(f"Your random password is : {a}")

#Way-2

# import random
# #import string
# import string
#
# if __name__=="__main__":
#     s1=string.ascii_lowercase
#     s2=string.ascii_uppercase
#     s3=string.digits
#     s4=string.punctuation
#     length_password=int(input("Enter the length of password : "))
#     s=[]
#     s.extend(list(s4))
#     s.extend(list(s1))
#     s.extend(list(s3))
#     s.extend(list(s2))
#     a="".join(random.sample(s,length_password))
#     print(f"Your random password is : {a}")
#
