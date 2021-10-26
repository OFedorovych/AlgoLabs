import math
import sys

def main():
    num_of_bugs = int(sys.argv[1])
    height = int(sys.argv[2])
    width = int(sys.argv[3])

#find an area of one list for bag
    area_of_paper = height * width
    min_area_of_square = area_of_paper * num_of_bugs
    
#find min length of one side of the square
    min_side = math.ceil(math.sqrt(min_area_of_square))
    print("start : ", min_side)

    while True:
        lists_in_width = int(min_side / width)
        lists_in_height = int(min_side / height)
        num_of_lists = lists_in_width * lists_in_height
        if num_of_lists >= num_of_bugs:
            break
        min_side += 1

    print(min_side)



if __name__ == "__main__":
    main()