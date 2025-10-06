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

# File XML của bạn - đảm bảo file sinhvien.xml ở cùng thư mục
xml_file = "buoi5_HuynhDangKhoa/sinhvien.xml"

# print("=== KIỂM TRA SINHVIEN.XML ===")

# Test các biểu thức XPath
test_xpath(xml_file, "//student", "1. Lấy tất cả sinh viên")
test_xpath(xml_file, "//student/name/text()", "2. Liệt kê tên tất cả sinh viên")
test_xpath(xml_file, "//student/id/text()", "3. Lấy tất cả id của sinh viên")
test_xpath(xml_file, "//student[id='SV01']/date/text()", "4. Lấy ngày sinh của SV01")
test_xpath(xml_file, "//enrollment/course/text()", "5. Lấy các khóa học")
test_xpath(xml_file, "//student[1]", "6. Lấy toàn bộ thông tin của sinh viên đầu tiên")
test_xpath(xml_file, "//enrollment[course='VatLy01']/studentRef/text()", "7. Lấy mã SV đăng ký VatLy01")
test_xpath(xml_file, "//enrollment[course='Toan01']/studentRef/text()", "8. Lấy tên SV học môn Toan01")
test_xpath(xml_file, "//student[id='SV01']/date/text()", "10. Lấy ngày sinh của SV01")
test_xpath(xml_file, "//student[contains(date, '2004')]/name/text()", "11. Lấy tên SV sinh năm 2004")
test_xpath(xml_file, "count(//student)", "13. Đếm tổng số sinh viên")
test_xpath(xml_file, "//student[not(id = //enrollment/studentRef)]", "14. Lấy SV chưa đăng ký môn nào")
test_xpath(xml_file, "//student[id='SV01']/name/following-sibling::date[1]", "15. Lấy date sau name của SV01")
test_xpath(xml_file, "//student[id='SV02']/name/preceding-sibling::id[1]", "16. Lấy id trước name của SV02")
test_xpath(xml_file, "//enrollment[studentRef='SV03']/course", "17. Lấy course của SV03")
test_xpath(xml_file, "//student[starts-with(name, 'Nguyễn')]", "18. Lấy sinh viên có họ là Nguyễn")
test_xpath(xml_file, "substring(//student[id='SV01']/date, 1, 4)", "19. Lấy năm sinh của SV01")