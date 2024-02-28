def char_count_while(target: str, char: str) -> int:
    char_count = 0
    i = 0
    while i < len(target):
        if target[i] == char:
            char_count += 1
        i += 1
    return char_count
    

def char_count_for(target: str, char: str) -> int:
    char_count = 0
    for i in range(len(target)):
        if target[i] == char:
            char_count += 1
    return char_count

def char_count_foreach(target: str, char: str) -> int:
    char_count = 0
    for i in target:
        if i == char:
            char_count += 1
    return char_count





def main():
    target = "hello world!"
    char = "l"

    print(char_count_while(target, char))
    print(char_count_for(target, char))
    print(char_count_foreach(target, char))





main()