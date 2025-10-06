from lxml import etree

import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
# Đọc file XML từ file thực tế
def test_xpath(xml_file, xpath_expression, description):
    try:
        # Parse XML từ file
        tree = etree.parse(xml_file)
        result = tree.xpath(xpath_expression)
        print(f"{description}:")
        print(f"XPath: {xpath_expression}")
        print(f"Kết quả: {result}")
        print("-" * 60)
    except Exception as e:
        print(f"Lỗi với {description}: {e}")

# File XML
xml_file = "buoi5_HuynhDangKhoa/quanlybanan.xml"

print("=== KIỂM TRA QUANLYBANAN.XML ===")

# Test các biểu thức XPath đơn giản hơn
test_xpath(xml_file, "//BAN", "1. Lấy tất cả bàn")
test_xpath(xml_file, "//NHANVIEN", "2. Lấy tất cả nhân viên")
test_xpath(xml_file, "//TENMON/text()", "3. Lấy tất cả tên món")
test_xpath(xml_file, "//NHANVIEN[MANV='NV02']/TENV/text()", "4. Lấy tên nhân viên có mã NV02")
test_xpath(xml_file, "//NHANVIEN[MANV='NV03']/TENV/text()", "5a. Lấy tên nhân viên NV03")
test_xpath(xml_file, "//NHANVIEN[MANV='NV03']/SDT/text()", "5b. Lấy số điện thoại nhân viên NV03")
test_xpath(xml_file, "//MON[GIA > 50000]/TENMON/text()", "6. Lấy tên món có giá > 50,000")
test_xpath(xml_file, "//HOADON[SOHD='HD03']/SOBAN/text()", "7. Lấy số bàn của hóa đơn HD03")
test_xpath(xml_file, "//MON[MAMON='M02']/TENMON/text()", "8. Lấy tên món có mã M02")
test_xpath(xml_file, "//HOADON[SOHD='HD03']/NGAYLAP/text()", "9. Lấy ngày lập của hóa đơn HD03")
test_xpath(xml_file, "//HOADON[SOHD='HD01']//CTHD/MAMON/text()", "10. Lấy tất cả mã món trong hóa đơn HD01")
test_xpath(xml_file, "//HOADON[SOHD='HD02']/MANV/text()", "12. Lấy mã nhân viên lập hóa đơn HD02")
test_xpath(xml_file, "count(//BAN)", "13. Đếm số bàn")
test_xpath(xml_file, "count(//HOADON[MANV='NV01'])", "14. Đếm số hóa đơn lập bởi NV01")
test_xpath(xml_file, "//HOADON[SOBAN='2']//CTHD/MAMON/text()", "15. Lấy mã món trong hóa đơn của bàn số 2")
test_xpath(xml_file, "//NHANVIEN[MANV=//HOADON[SOBAN='3']/MANV]", "16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3")
test_xpath(xml_file, "//HOADON[MANV=//NHANVIEN[GIOITINH='Nữ']/MANV]", "17. Lấy tất cả hóa đơn mà nhân viên nữ lập")
test_xpath(xml_file, "//NHANVIEN[MANV=//HOADON[SOBAN='1']/MANV]", "18. Lấy tất cả nhân viên từng phục vụ bàn số 1")
test_xpath(xml_file, "//HOADON[SOHD='HD02']/SOBAN/text()", "20a. Lấy số bàn của HD02")
test_xpath(xml_file, "//HOADON[SOHD='HD02']/NGAYLAP/text()", "20b. Lấy ngày lập của HD02")

# Để lấy món được gọi nhiều hơn 1 lần, cần xử lý riêng
print("19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn:")
tree = etree.parse(xml_file)
all_dishes = tree.xpath("//CTHD/MAMON/text()")
from collections import Counter
dish_count = Counter(all_dishes)
popular_dishes = [dish for dish, count in dish_count.items() if count > 1]
print(f"Kết quả: {popular_dishes}")
print("-" * 60)
