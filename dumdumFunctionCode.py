#Prime Number? IDK im stupid so this ones heavily based on the programiz website, i need crutches for now (good god stupidity)

def are_you_prime(n):
    flag = False 
    if n == 1 or n == 0:
        print("Hindi prime numner ang " + str(n) + " pawreigh. Thats an automatic nauurr.")
        return # grabe kaya pala nauulit amp naman 
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                flag = True
                break
    if flag:
        print("Naugwghhh hindi prime ang numerong", n, " bro")
    else:
        print("Iyuhhhhh, prime numbero ang", n, " bro")

are_you_prime(456)
are_you_prime(1)
are_you_prime(13)