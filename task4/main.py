import sys


def count_steps(nums_list):
    count_steps = 0
    mediana_index = int((len(nums_list)-1)/2)
    mediana = nums_list[mediana_index]
    for item in nums_list:
        count_steps += abs(item - mediana)
    return count_steps  


def create_nums_list(args):
    nums = []

    with open(args, 'r') as file:
        for line in file.readlines():
            num = line.splitlines()
            nums.append(num)
    
    nums_list = [x for l in nums for x in l]
    nums_list = list(map(int, nums_list))
    nums_list.sort()
    
    return nums_list
    

def main(args):
    nums_list = create_nums_list(args)
    print(count_steps(nums_list))

if __name__ == "__main__":
    main(args=sys.argv[1])
