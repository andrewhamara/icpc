def main():
    h,k,v,s = input("Enter 4 integers: ").split()
    h = int(h); k = int(k); v = int(v); s = int(s)
    dist = 0
    while h > 0:
        v += s
        v -= max(1, int(v/10))
        if v >= k:
            h += 1
            if h == 0:
                v = 0
        if v <= 0:
            h = 0; v = 0
        dist += v
        if s > 0:
            s -= 1
    print(dist)

if __name__ == "__main__":
    main()
