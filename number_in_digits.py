if __name__ == '__main__':

    divBy = 1
    modBy = 10
    arr = []
    
    for i in range(4):
        x = 647
        print(x)
        v = x % modBy
        v = v // divBy
        print(v)
        divBy = divBy * 10
        modBy = modBy * 10
        arr.insert(0,v)

    print(arr)