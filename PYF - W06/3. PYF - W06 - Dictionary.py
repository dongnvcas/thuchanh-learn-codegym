tuDien = dict()
while True:
    print("""
     Vui lòng lựa chọn theo menu sau:
         ------ Menu -----
     1 - Thêm một từ vựng mới vào từ điển (kèm theo nghĩa)
     2 - Tra cứu ý nghĩa của một từ vựng
     3 - Cập nhật ý nghĩa cho một từ vựng
     4 - Xóa một từ vựng trong từ điển
     5 - Xóa toàn bộ từ vựng trong từ điển
     6 - Kết thúc chương trình
     """)
    print(tuDien, "\n")
    while True:
        try:
             n = int(input("Nhập vào lựa chọn của bạn: "))
             break
        except ValueError:
            print("Vui lòng chỉ nhập lựa chọn theo menu")
    if n == 1:
        x = input("Nhập vào từ tiếng Anh: ")
        y = input("Nhập vào nghĩa tiếng Việt: ")
        tuDien.update({x:y})
        print( )
    elif n==2:
        x = input("Nhập vào từ bạn muốn tra cứu: ")
        if x in tuDien:
            print("Nghĩa của từ", x, "là:", tuDien[x])
        else:
            print("Không có từ", x, "trong từ điển")
    elif n==3:
        x = input("Nhập từ tiếng Anh muốn đổi nghĩa:")
        y = input("Nhập nghĩa tiếng Việt mới: ")
        if x in tuDien:
            tuDien.update({x:y})
            print("Đã cập nhật từ điển")
        else:
            print("Không có từ bạn vừa nhập để cập nhật nghĩa")
    elif n==4:
        x = input("Nhập vào từ tiếng Anh mà bạn muốn xóa: ")
        if x in tuDien:
            tuDien.pop(x)
            print("Đã xóa từ", x, "khỏi từ điển")
        else:
            print("Từ bạn vừa nhập không có trong từ điển")
    elif n==5:
        tuDien.clear()
        print("Đã xóa toàn bộ từ điển")
    elif n==6:
        print("Chương trình đã kết thúc")
        break
    else:
        print("vui lòng nhập đúng lựa chọn theo menu")