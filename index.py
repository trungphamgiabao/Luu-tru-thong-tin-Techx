class HocVien:
    def __init__(self, maHV, tenHV, ngaySinh, khoaHoc):
        self. maHV = maHV
        self. tenHV = tenHV
        self. ngaySinh = ngaySinh
        self. khoaHoc = khoaHoc
    def hienthithongtin(self):
        return f"""
                id:{self.maHV}
                Tên:{self.tenHV}
                Ngày sinh:{self.ngaySinh}
                Khóa Học:{self.khoaHoc}"""

sv1= HocVien("NV001","Nguyen dep trai", 1/1/2000, "cybersoft1") 
print(sv1.hienthithongtin())