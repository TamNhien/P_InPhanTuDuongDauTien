def find_first_positive(lst):
    return next((num for num in lst if num > 0), -1)

def main():
    lst = list(map(int, input("Nhập vào danh sách các số nguyên, cách nhau bởi dấu phẩy: ").split(',')))
    print(find_first_positive(lst))

if __name__ == "__main__":
    main()

