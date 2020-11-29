def get_min_max(arr:list, key) -> tuple:
    min = arr[0]
    max = arr[0]
    for num in arr:
        if key(num) < key(min):
            min = num
        elif key(num) > key(max):
            max = num
    return min,max


def counting_sort(arr:list, key) -> list:

    #Get minimum and maximum
    minimum, maximum = get_min_max(arr, key)

    #Generate the table
    counting_table = []
    for _ in range(key(minimum), key(maximum) + 1):
        counting_table.append([])

    #Counting sort the item
    for item in arr:
        counting_table[key(item) - key(minimum)].append(item)
    
    #Put the items back to the original arr
    index = 0
    for lst in counting_table:
        while(len(lst) > 0):
            arr[index] = lst.pop(0)
            index += 1

    return arr

def count_arr(arr:list):

    #Create a new dict
    d = {}

    #Iterate and count the numbers
    for i in arr:
        if not i in d:
            d[i] = 0
        d[i] += 1

    #Return the frequency
    return list(d.items())


"""
Question:
for an arr [1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7]
Print the top k most frequently occuring elements: [1,2]
"""
if __name__ == "__main__":
    #Input arr
    arr = [1,2,3,4,4,3,2,1,4,6,5,3,6,7]

    #K value
    k = 3

    #Get counts
    counts = count_arr(arr)

    #Get the sorted arr
    sorted_arr = counting_sort(counts, lambda x: -x[1])

    print(list(map(lambda x: x[0], sorted_arr[:k])))


    



    