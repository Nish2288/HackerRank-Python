if __name__ == "__main__":
    val = map(int, input().split())
    t = tuple((val))
    print(hash(t))