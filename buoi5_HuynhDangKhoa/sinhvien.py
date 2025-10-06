from lxml import etree

tree = etree.parse("buoi5_HuynhDangKhoa/sinhvien.xml")

print("=== KẾT QUẢ SINHVIEN.XML ===\n")

# 1. Lấy tất cả sinh viên
print("1. Tất cả sinh viên:")
for student in tree.xpath("//student"):
    print(f"   - {student.xpath('name/text()')[0]}")

# 2. Tên tất cả sinh viên  
print("\n2. Tên sinh viên:")
for name in tree.xpath("//student/name/text()"):
    print(f"   - {name}")

# 3. Tất cả ID
print("\n3. ID sinh viên:")
for id in tree.xpath("//student/id/text()"):
    print(f"   - {id}")

# 4. Ngày sinh SV01
print(f"\n4. Ngày sinh SV01: {tree.xpath('//student[id=\"SV01\"]/date/text()')[0]}")

# 5. Các khóa học
print("\n5. Khóa học:")
for course in tree.xpath("//enrollment/course/text()"):
    print(f"   - {course}")

# 6. Sinh viên đầu tiên
sv1 = tree.xpath("//student[1]")[0]
print(f"\n6. SV đầu tiên: {sv1.xpath('name/text()')[0]}")

# 7. SV học VatLy01
print(f"\n7. SV học VatLy01: {tree.xpath('//enrollment[course=\"VatLy01\"]/studentRef/text()')[0]}")

# 8. SV học Toan01
print("\n8. SV học Toan01:")
for sv in tree.xpath("//enrollment[course='Toan01']/studentRef/text()"):
    print(f"   - {sv}")

# 10. Ngày sinh SV01 (giống câu 4)
print(f"\n10. Ngày sinh SV01: {tree.xpath('//student[id=\"SV01\"]/date/text()')[0]}")

# 11. SV sinh năm 2004
print("\n11. SV sinh năm 2004:")
for name in tree.xpath("//student[contains(date, '2004')]/name/text()"):
    print(f"   - {name}")

# 13. Đếm số SV
print(f"\n13. Tổng số SV: {tree.xpath('count(//student)')}")

# 14. SV chưa đăng ký môn
print("\n14. SV chưa đăng ký môn:")
unregistered = tree.xpath("//student[not(id = //enrollment/studentRef)]/name/text()")
if unregistered:
    for name in unregistered:
        print(f"   - {name}")
else:
    print("   - Không có")

# 15. Date sau name SV01
print(f"\n15. Date sau name SV01: {tree.xpath('//student[id=\"SV01\"]/name/following-sibling::date[1]/text()')[0]}")

# 16. ID trước name SV02
print(f"\n16. ID trước name SV02: {tree.xpath('//student[id=\"SV02\"]/name/preceding-sibling::id[1]/text()')[0]}")

# 17. Course của SV03
print(f"\n17. Course của SV03: {tree.xpath('//enrollment[studentRef=\"SV03\"]/course/text()')[0]}")

# 18. SV họ Nguyễn
print("\n18. SV họ Nguyễn:")
for name in tree.xpath("//student[starts-with(name, 'Nguyễn')]/name/text()"):
    print(f"   - {name}")

# 19. Năm sinh SV01
print(f"\n19. Năm sinh SV01: {tree.xpath('substring(//student[id=\"SV01\"]/date, 1, 4)')[0]}")