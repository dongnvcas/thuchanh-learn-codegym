# Bước 1:  Khai báo hàm lấy thông tin sản phẩm bằng id sản phẩm
def get_info(product_list, product_id):
    if product_id in product_list:
        print(f'The product with ID {product_id} is {product_list[product_id]}')
    else:
        print("The product is not in the list")

# Bước 2: Khai báo hàm cập nhật danh sách sản phẩm
def update_info(product_list, product_id, product_name):
    product_list[product_id] = product_name


# Bước 3: Sử dụng print() để in ra danh sách sản phẩm hiện tại
def print_info(product_list):
    print("Current product list is: ", product_list)

# Bước 4: Khởi tạo vòng lặp

product_list = dict()
while True:
    print("""
     Please select option as below:
         ------ Menu -----
     1 - Add product to the list
     2 - Edit name of product 
     3 - Delete a product
     4 - Get information of the product
     5 - Quit
     """)
    print('The current product list is:', product_list, "\n")
    while True:
        try:
            option = int(input("Please input your choice: "))
            break
        except ValueError:
            print("Please only input numbers from 1 - 6")

    if option == 1:
        product_id = input("Please input the ID of the product: ")
        if product_id in product_list:
            print('The product is alredy in the list')
        else:
            product_name = input("Please input name of the product: ")
            update_info(product_list, product_id, product_name)

    elif option == 2:
        product_id = input("Please input the ID of the product: ")
        if product_id in product_list:
            product_name = input("Please input name of the product: ")
            update_info(product_list, product_id, product_name)   
        else:
            print('The product is not in the list')

    elif option == 3:
        product_id = input("Please input the ID of the product: ")
        if product_id in product_list:
            del product_list[product_id]   
        else:
            print('The product is not in the list')
 
    elif option ==4:
        product_id = input("Please input the ID of the product: ")
        if product_id in product_list:
            get_info(product_list, product_id)
        else:
            print('The product is not in the list')
    elif option ==5:
        print("The program is end")
        break
    else:
        print("Please only input numbers from 1 - 6")