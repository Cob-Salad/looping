

def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    new_list = []
    i = 0
    while i <= len(a) - 1:
        new_list.append(a[i] * b[i])
        i += 1
    return new_list



def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] * b[i])
    return new_list



def main():
    a = [-1, 3, 0]
    b = [1, 4, 3]

    print(f"{list_multiply_while(a, b)}")
    print(f"{list_multiply_for(a, b)}")
    
    
main()