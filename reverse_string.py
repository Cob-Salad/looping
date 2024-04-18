def reverse_while(s):
    n = ""
    i = 0
    while len(n) < len(s):
        if i >= -len(s):
            i -= 1
            n += s[i]
    return n

def reverse_for_each(s):
    n = ""
    for char in s:
        n = char + n
    return n

def reverse_for(s):
    string = ""
    for i in range(len(s)):
        string = s[i] + string

    return string



def main():
    print(f"{reverse_while('hello')}")
    print(f"{reverse_for('hey there')}")
    print(f"{reverse_for_each('hello world')}")



if __name__ == "__main__":
    main()
