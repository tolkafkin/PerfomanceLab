import sys


def path_found(n, m):
    start_list = m*[num for num in range(1, n + 1)]
    middle_list = []
    end_list = []
    
    finish = False
    count = 0
    while not finish:
        for item in range(count, count + m):
            middle_list.append(start_list[item])
            count += 1
        
        end_list.append(middle_list[0])    
        count -= 1
        
        if middle_list[-1] == start_list[0]:
            finish = True
            
        middle_list.clear()    
    return "".join(map(str, end_list))    


def main():
    n, m = int(sys.argv[1]), int(sys.argv[2])
    print(f"{path_found(n, m)}\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
