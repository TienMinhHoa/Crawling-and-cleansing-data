if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        cmd = str(input())
        if "insert" in cmd:
            my_list.insert(int(cmd[7]),int(cmd[9:]))
        elif "print" in cmd:
            print(my_list)
        elif "remove" in cmd:
            my_list.pop(my_list.index(int(cmd[7])))
        elif "append" in cmd:
            my_list.append(int(cmd[7]))
        elif "sort" in cmd:
            my_list.sort()
        elif "pop" in cmd:
            my_list.pop()
        else:
            my_list.reverse()
