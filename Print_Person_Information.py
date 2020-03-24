def guest_list(guests):
    for i in guests:
        for j in i:
            print("{} is {} years old and works as {}".format(j[0],j[1],j[2])

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])