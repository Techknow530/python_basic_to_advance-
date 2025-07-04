def main():
    #traditional way to take value 
    # a = int(input("enter value for first number :"))
    # b = int(input("enter value for Second number :"))
    
    #advance and diffrent way to take values

    a , b = map(int , input("Enter two values which saprate by space ").split())


    print("-------------------------------------------")

    print("Enter 1 or '+' sign for addition \n Enter 2 or '-' sign for subtractions \n Enter 3 or '*' sign for multiplication \n Enter 4 or '/'  for divison \n ---------------------------- \n Enter yout choice :" ,end="")

    operor = input().strip()

    if (operor == '+' or operor == '1'):
        ans = add_sum(a,b) 
    elif(operor == '-' or operor == '2'):
        ans =sub(a,b)
    elif(operor == '*' or operor =='3'): 
        ans =mul(a,b)
    elif(operor== '/' or operor == '4'):
        ans =div(a,b)
    else:
        print("----------------------------------------- \n Please enter Valid choice ")
        main()
        


def add_sum(num1,num2):
    sm = int(num1) + int(num2)
    print(f"{num1} + {num2} is = {sm}") 
    return sm 

def sub(num1 ,num2):
    sb = int(num1-num2)
    print(f"{num1} - {num2} is = {sb}")

    return sb

def mul(num1,num2):
    ml = int (num1*num2)
    print(f"{num1} X {num2} is = {ml}")
    return ml

def div(num1,num2):
    if num2 != 0:

        dv = float(num1/num2)
        print(f"{num1} / {num2} is = {dv}")
        return dv 
    else:
        print("number is not divide by zero Please enter valid number ")
        main()

        







if __name__ == "__main__" :
    main()