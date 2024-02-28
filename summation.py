

def summation_while(n):
    m = 0
    i = 0
    while i <= n:
        m += i
        i += 1
    return m



def summation_for(n):
    m = 0
    for i in range(n):
        i += 1
        m += i
    return m

        
def main():
    
    print(f"{summation_while(10)}")
    print(f"{summation_while(5)}")
    
    print(f"{summation_for(3)}")


if __name__ == "__main__":
    main()

