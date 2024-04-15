import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    data = {}

    with open(file_path, "r", newline="") as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)
        
        for header in headers:
            data[header] = []

        for row in csv_reader:
            for i, value in enumerate(row):
                data[headers[i]].append(float(value))
    
    return data

def selection_sort(sel_array,direction="vzostupne"):
    """
    """
    for i in range(len(sel_array)-1):
        if direction == "vzostupne":
            min_idx = i
            for j in range(i+1, len(sel_array)):
                if sel_array[j] < sel_array[min_idx]:
                    min_idx = j

            sel_array[i], sel_array[min_idx] = sel_array[min_idx], sel_array[i]
        
        elif direction == "zostupne":
            max_idx = i
            for j in range(i+1, len(sel_array)):
                if sel_array[j] > sel_array[max_idx]:
                    max_idx = j
            
            sel_array[i], sel_array[max_idx] = sel_array[max_idx], sel_array[i]
    return sel_array

def bubble_sort(bubble_arr):
    """
    """
    swapped = True
    while swapped:
        swapped = False

        for i in range(len(bubble_arr)-1):
            if bubble_arr[i] > bubble_arr[i+1]:
                bubble_arr[i], bubble_arr[i+1] = bubble_arr[i+1], bubble_arr[i]
                swapped = True

    return bubble_arr

def insertion_sort():
    ...

    

def main():
    #pass
    file_name = 'numbers.csv'
    data = read_data(file_name)
    print(data)

    bubble_sauce = data['series_1']
    bubble = bubble_sort(bubble_sauce)
    print(bubble)

if __name__ == '__main__':
    main()
