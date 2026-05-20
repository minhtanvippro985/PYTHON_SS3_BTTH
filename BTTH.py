

active = True
choice = ""
while active != False:
    max_employees = int(input("Nhập số lượng nhân viên"))
    for employee in range(1,max_employees+ 1):
        print(f"Nhân viên {employee}")
        employee_name = input("Nhập tên nhân viên ")
        work_days = int(input("Nhập ngày công "))

        attendance_status = "Nhân viên chuyên cần tốt" if work_days >= 20 else "Cần cải thiện chuyên cần"
        
        print(f"""
            ------------
            Thông tin nhân viên
            Tên nhân viên : {employee_name}
            Số ngày đi làm : {work_days}
            {attendance_status}
                """)
        
        choice = input("Tiếp tục chuong trình? (y/n)")
        if choice == "y":
            print("\n tiếp tục chương trình")
        elif choice == "n":
            print("\n Dừng chương trình")
            active = False
            break

       