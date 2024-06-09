class Student:
    def __init__(self, ma_sinh_vien, ho_ten, ngay_sinh, que_quan, chuyen_nganh, lop):
        self.ma_sinh_vien = ma_sinh_vien
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.que_quan = que_quan
        self.chuyen_nganh = chuyen_nganh
        self.lop = lop
    
    def print_infor(self):
        print(f'''
        Học sinh có Mã sinh viên là: {self.ma_sinh_vien}
        Tên của học sinh đó là: {self.ho_ten}
        Sinh ngày: {self.ngay_sinh}
        Quê quán: {self.que_quan}
        Chuyên ngành: {self.chuyen_nganh}
        Hiện đang học lớp: {self.lop}''')

class Student_List:
    def __init__(self):
        self.list_of_student = []
    
    def view_students(self):
        for student in self.list_of_student:
            student.print_infor()
    
    def add_student(self):
        ma_sinh_vien = input('Vui lòng nhập mã sinh viên: ')
        ho_ten = input('Vui lòng nhập họ và tên: ')
        ngay_sinh = input('Vui lòng nhập ngày sinh: ')
        que_quan = input('Vui lòng nhập quê quán: ')
        chuyen_nganh = input('Vui lòng nhập chuyên ngành: ')
        lop = input('Vui lòng nhập lớp: ')
        new_student = Student(ma_sinh_vien, ho_ten, ngay_sinh, que_quan, chuyen_nganh, lop)
        self.list_of_student.append(new_student)
    
    def update_student(self, ma_sinh_vien):
        for student in self.list_of_student:
            if student.ma_sinh_vien == ma_sinh_vien:
                student.ho_ten = input('Vui lòng nhập họ và tên mới: ')
                student.ngay_sinh = input('Vui lòng nhập ngày sinh mới: ')
                student.que_quan = input('Vui lòng nhập quê quán mới: ')
                student.chuyen_nganh = input('Vui lòng nhập chuyên ngành mới: ')
                student.lop = input('Vui lòng nhập lớp mới: ')
                return
        print(f'Không tìm thấy sinh viên với mã {ma_sinh_vien}')
    
    def delete_student(self, ma_sinh_vien):
        self.list_of_student = [student for student in self.list_of_student if student.ma_sinh_vien != ma_sinh_vien]
        print(f'Đã xóa sinh viên có mã số {ma_sinh_vien} ra khỏi danh sách')
    
    def search_student(self, keyword):
        results = [student for student in self.list_of_student if keyword.lower() in student.ho_ten.lower() or keyword.lower() in student.ma_sinh_vien.lower()]
        for student in results:
            student.print_infor()
    
    def sort_students(self):
        self.list_of_student.sort(key=lambda student: student.ho_ten)

# Ví dụ sử dụng các lớp
student_list = Student_List()
while True:
    print('''
    Vui lòng lựa chọn theo menu sau:
    1 - Thêm sinh viên vào danh sách
    2 - Cập nhật thông tin sinh viên
    3 - Xóa thông tin sinh viên
    4 - Tìm kiếm sinh viên
    5 - Sắp xếp thứ tự sinh viên
    6 - In thông tin sinh viên
    7 - Kết thúc chương trình
        ----------------------
''')
    while True:
        try:
            option = int(input("Nhập vào lựa chọn của bạn: "))
            break
        except ValueError:
            print("Vui lòng chỉ nhập lựa chọn theo menu")
    
    if option == 1:
        student_list.add_student()
    elif option == 2:
        ma_sinh_vien = input("Vui lòng nhập vào mã của sinh viên cần cập nhật: ")
        student_list.update_student(ma_sinh_vien)
    elif option == 3:
        ma_sinh_vien = input("Vui lòng nhập vào mã của sinh viên cần xóa: ")
        student_list.delete_student(ma_sinh_vien)
    elif option == 4:
        keywork = input("Vui lòng nhập vào mã của sinh viên hoặc tên sinh viên cần tìm: ")
        student_list.search_student(keywork)
    elif option == 5:
        student_list.sort_students()
    elif option == 6: 
        print('Danh sách học viên hiện có là:')
        student_list.view_students()
    elif option == 7:
        print("Chương trình đã kết thúc")
        break
    else:
        print("vui lòng nhập đúng lựa chọn theo menu")   
