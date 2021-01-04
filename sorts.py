def main():
    test = [43, 67, 92, 44, 39, 98, 36, 44, 36, 76, 5, 36, 8, 22, 75]
    bubble(test)
    print(test)

"""
HELPER FUNCTIONS
"""
#check if a list is sorted (only needed for bogo sort)
def sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

"""
SORT FUNCTIONS
"""
#bogo sort (Run at your own risk!)
def bogo(nums):
    while not sorted(nums):
        shuffle(nums)

#selection sort
def selection(nums):
    #for each element in the list
    for i in range(len(nums)):

        #find the minimum value and its index in the remaining unsorted list
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[min_index] > nums[j]:
                min_index = j

        #swap the minimum value with the first value in the unsorted list
        nums[i], nums[min_index] = nums[min_index], nums[i]

#insertion sort
def insertion(nums):
    #for each element in the list (except the first)
    for i in range(1, len(nums)):
        key = nums[i]

        #while there are numbers larger than the key to its left, move each of these larger numbers one space to the right
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        
        #finally, put the key into the position in which it belongs
        nums[j + 1] = key

#bubble sort
def bubble(nums):
    #initialize swapped to true
    swapped = True

    #while at least one swap was performed in the last pass, perform another pass
    while swapped:
        #set swapped to false
        swapped = False

        #loop through the list and compare adjacent values
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

if __name__ == "__main__":
    main()
