import math
import sys

def main():
    num_of_bugs = int(sys.argv[1])
    height = int(sys.argv[2])
    width = int(sys.argv[3])


#find an area of one list for bag
    area_of_paper = height * width
    min_area_of_square = area_of_paper * num_of_bugs

    if height > width:
        max_side = height * num_of_bugs
    else:
        max_side = width * num_of_bugs
    
    min_side = math.ceil(math.sqrt(min_area_of_square))
    mid_of_search = int((min_side + max_side) / 2)

    while True:
        lists_in_width = int(mid_of_search / width)
        lists_in_height = int(mid_of_search / height)
        num_of_lists = lists_in_width * lists_in_height
        print (min_side, mid_of_search,max_side, num_of_lists)
        if max_side - min_side <= 1:
            break
        if num_of_lists >= num_of_bugs:
            max_side = mid_of_search            
        else:
            min_side = mid_of_search
        mid_of_search = int((min_side + max_side) / 2)
    


    if num_of_lists>=num_of_bugs:
        print(min_side)
    else:
        print(max_side)

if __name__ == "__main__":
    main()