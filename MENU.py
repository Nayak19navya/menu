menu={
    'Pizza':457,
    'Dalgona Coffee':975,
    'Burger':865,
    'wow brunch':64368,
    'chilling chill fresh':855764
}
print(" WELCOME HOME ")
print("Pizza: Rs-457\nDalgona Coffee: Rs-975\nBurger: Rs-865\nwow brunch: Rs-64368\nchilling chill fresh: Rs-855764")

Order_total = 0
item_1 = input("Enter Dish Of ur choice:\n")
if item_1 in menu:
    Order_total += menu[item_1]
    print(f"your dish {item_1} is on the way")
else:
    print("Sorry to dissaponit u ..please give new Order")

i_2=input("How about ordering another dish???(Yes/No)")

if i_2=="Yes":
    i_2=input("Enter ur choice")
    if i_2 in menu:
        Order_total+=menu[i_2]
        print("your dish{item1}is on the way")
    else:
        print("Sorry to dissaponit u ..please give new Order")
print(f"TOTAL=  {Order_total}")
