menu={'Pizza':80,
      'Pasta':60,
      'Burger':90,
      'Momos':80,
      'Coeffe':120,
      'Cold Coco':150,
      }
print("**Welcome To Python Restaurant**")
print("Pizza:80\nPasta:60\nBurger:90\nMomos:80\nCoeffe:120\nCold Coco:150"
      )
order_total=0
item_1=input("Enter The Name Of Item You Want To Order=")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your Item {item_1} Has Been Added To Your Order")
else:
    print(f"ordered item {item_1} is not available yet")
another_order=input("do you want to add another item?(Yes/No)")
if another_order=="yes":
    item_2=input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print(f"Ordered item {item_2} is not available!:")
print(f"The total amout of item to pay is{order_total}")
