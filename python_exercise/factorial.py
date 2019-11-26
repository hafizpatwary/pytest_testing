
def factorial(num):
    divide = 2
    negative = False
    if num < 0:
        num *= -1
        negative = True

    try:
        if num == 1 or num == 0:
            print(1)
        elif num > 1 and type(num) is int:
            while num > 1:
                num /= divide
                divide += 1
            if num == 1:
                if negative:
                    divide *= -1
                    return divide+1
                return(divide-1)
            else:
                return("none")
    except:
        print("none")
