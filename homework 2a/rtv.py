user_name = input("enter your name")
print(user_name .lower() .capitalize())


sur_name = input("Enter your sur_name")
L = " " .join(sur_name)
print(L)


user_age = input("Enter how old are you?")
print(user_age)
if int(user_age) == 13:
    print(user_age)

 
 


expression = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laudantium nihil
laborum rerum ipsum iure dicta officiis, necessitatibus non vel excepturi minima
quia fugiat hic numquam suscipit harum laboriosam magni quasi veniam voluptas
eius sapiente aperiam vero? Eum ducimus consequuntur, accusamus tempore corporis
numquam animi hic ad voluptatem saepe mollitia voluptate explicabo soluta earum!
Consequatur porro eos minus facilis mollitia alias nesciunt. Molestias explicabo
alias ea praesentium placeat ex ad maxime ipsam non velit architecto, iure
laborum reiciendis pariatur dolorem amet nulla dolor quos a esse atque vel? Fuga
quidem perspiciatis velit iure excepturi. Delectus velit amet distinctio error
temporibus at voluptas suscipit laboriosam rerum ea, quibusdam nesciunt maiores
quas necessitatibus fugit veniam, molestiae inventore dignissimos voluptatum
libero enim natus! Cum, corrupti ad."""

 

print(len(expression))
  
print("ad" in expression)

print(expression.find("ad"))

print(expression[39:41])
 
print(expression.find("Lorem"))

print(expression.replace("Lorem", "hey you"))




