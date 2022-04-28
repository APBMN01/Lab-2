def display_main_menu():
    print("Enter some numbers separated by commas e.g. 5, 67, 32")

def get_user_input():
    x = input()
    nums=[float(val) for val in x.split(', ')]
    return nums

def calc_average(number_list):
    return sum(number_list) / len(number_list)

def find_min_max(nums):
    return [round(min(nums)), round(max(nums))]

def sort_temperature(nums):
    return sorted(nums)

def calc_median_temperature(nums):
    import statistics
    return statistics.median(nums)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    number_list=get_user_input()
    print(calc_average(number_list))
    print(find_min_max(number_list))
    print(sort_temperature(number_list))
    print(calc_median_temperature(number_list))
if __name__ == "__main__":
    main()
