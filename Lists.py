if __name__ == "__main__":
    n = int(input("Enter number:"))
    cmd=[]
    list=[]
    for i in range(n):
        command = input().split()
        cmd = command[0]
        val = command[1:]

        if(cmd=="print"):
            print(list)
        else:
            cmd += "("+",".join(val)+")"
            #print(cmd)
            eval("list."+cmd)