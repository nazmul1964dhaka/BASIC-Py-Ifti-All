# if condition:
#     statement
# else:
#     statement    

#nested if exampal( if within "if")
user=input('Enter user name : ')
passward=input('Enter passward : ')
if user.upper()=='Ifte'.upper():
    if passward=='123':
        print('wellcome') 
    else:
        print('invalid passward')
else:
    print('invalid user name')        
