from lxml import etree
import sys

sys.stdout.reconfigure(encoding='utf-8')

tree = etree.parse("buoi5_HuynhDangKhoa/quanlybanan.xml")

print("=== KẾT QUẢ QUANLYBANAN.XML ===\n")

# 1. Lấy tất cả bàn
print("1. Tất cả bàn:")
for ban in tree.xpath("//BAN"):
    print(f"   - {ban.xpath('TENBAN/text()')[0]}")

# 2. Lấy tất cả nhân viên
print("\n2. Tất cả nhân viên:")
for nv in tree.xpath("//NHANVIEN"):
    print(f"   - {nv.xpath('TENV/text()')[0]}")

# 3. Lấy tất cả tên món
print("\n3. Tất cả tên món:")
for mon in tree.xpath("//TENMON/text()"):
    print(f"   - {mon}")

# 4. Tên nhân viên NV02
print(f"\n4. Tên NV02: {tree.xpath('//NHANVIEN[MANV=\"NV02\"]/TENV/text()')[0]}")

# 5. Tên và số điện thoại NV03
print(f"\n5. NV03 - Tên: {tree.xpath('//NHANVIEN[MANV=\"NV03\"]/TENV/text()')[0]}")
print(f"   SĐT: {tree.xpath('//NHANVIEN[MANV=\"NV03\"]/SDT/text()')[0]}")

# 6. Món giá > 50,000
print("\n6. Món giá > 50,000:")
for mon in tree.xpath("//MON[GIA > 50000]/TENMON/text()"):
    print(f"   - {mon}")

# 7. Số bàn HD03
print(f"\n7. Số bàn HD03: {tree.xpath('//HOADON[SOHD=\"HD03\"]/SOBAN/text()')[0]}")

# 8. Tên món M02
print(f"\n8. Tên món M02: {tree.xpath('//MON[MAMON=\"M02\"]/TENMON/text()')[0]}")

# 9. Ngày lập HD03
print(f"\n9. Ngày lập HD03: {tree.xpath('//HOADON[SOHD=\"HD03\"]/NGAYLAP/text()')[0]}")

# 10. Mã món trong HD01
print("\n10. Mã món trong HD01:")
for mamom in tree.xpath("//HOADON[SOHD='HD01']//CTHD/MAMON/text()"):
    print(f"   - {mamom}")

# 12. Mã nhân viên lập HD02
print(f"\n12. Mã NV lập HD02: {tree.xpath('//HOADON[SOHD=\"HD02\"]/MANV/text()')[0]}")

# 13. Đếm số bàn
print(f"\n13. Tổng số bàn: {tree.xpath('count(//BAN)')}")

# 14. Số hóa đơn NV01
print(f"\n14. Số hóa đơn NV01: {tree.xpath('count(//HOADON[MANV=\"NV01\"])')}")

# 15. Món trong hóa đơn bàn 2
print("\n15. Món trong hóa đơn bàn 2:")
for mamom in tree.xpath("//HOADON[SOBAN='2']//CTHD/MAMON/text()"):
    print(f"   - {mamom}")

# 16. NV lập hóa đơn bàn 3
print("\n16. NV lập hóa đơn bàn 3:")
for nv in tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='3']/MANV]/TENV/text()"):
    print(f"   - {nv}")

# 17. Hóa đơn nhân viên nữ
print("\n17. Hóa đơn nhân viên nữ:")
for hd in tree.xpath("//HOADON[MANV=//NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()"):
    print(f"   - {hd}")

# 18. NV phục vụ bàn 1
print("\n18. NV phục vụ bàn 1:")
for nv in tree.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='1']/MANV]/TENV/text()"):
    print(f"   - {nv}")

# 19. Món được gọi nhiều hơn 1 lần
from collections import Counter
all_dishes = tree.xpath("//CTHD/MAMON/text()")
dish_count = Counter(all_dishes)
popular_dishes = [dish for dish, count in dish_count.items() if count > 1]
print(f"\n19. Món được gọi nhiều hơn 1 lần: {popular_dishes}")

# 20. Thông tin HD02
soban = tree.xpath("//HOADON[SOHD='HD02']/SOBAN/text()")[0]
ngaylap = tree.xpath("//HOADON[SOHD='HD02']/NGAYLAP/text()")[0]
tenban = tree.xpath(f"//BAN[SOBAN='{soban}']/TENBAN/text()")[0]
print(f"\n20. Thông tin HD02: Bàn {tenban}, Ngày {ngaylap}")