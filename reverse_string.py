def reverse_while(s):
    n = ""
    i = 0
    while len(n) < len(s):
        if i >= -len(s):
            i -= 1
            n += s[i]
    return n



def main():
    print(f"{reverse_while('hello')}")

if __name__ == "__main__":
    main()
