import xml.etree.ElementTree as ET
from lxml import etree
import mysql.connector

class XMLProcessor:
    def __init__(self, xml_file, xsd_file):
        self.xml_file = xml_file
        self.xsd_file = xsd_file
        self.db_config = {'host':'localhost','user':'root','password':'','database':'ecommerce_db'}
    
    def kiem_tra(self):
        """Kiem tra XML voi XSD"""
        try:
            with open(self.xsd_file, 'r', encoding='utf-8') as f:
                schema = etree.XMLSchema(etree.fromstring(f.read().encode()))
            with open(self.xml_file, 'r', encoding='utf-8') as f:
                valid = schema.validate(etree.fromstring(f.read().encode()))
            print("XML hop le" if valid else "XML khong hop le")
            return valid
        except Exception as e:
            print(f"Loi: {e}")
            return False
    
    def hien_thi_du_lieu(self, cursor):
        """Hien thi du lieu tu database"""
        cursor.execute("SELECT * FROM Categories")
        print("\n📁 Categories:")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[1]}")
        
        cursor.execute("SELECT * FROM Products")
        print("\n📦 Products:")
        for row in cursor.fetchall():
            print(f"  {row[0]}: {row[1]} - ${row[2]} - Ton kho: {row[4]}")
    
    def xu_ly(self):
        """Xu ly chinh"""
        if not self.kiem_tra():
            return
        
        try:
            conn = mysql.connector.connect(**self.db_config)
            cursor = conn.cursor()
            
            cursor.execute("CREATE TABLE IF NOT EXISTS Categories (id VARCHAR(10) PRIMARY KEY, name VARCHAR(255))")
            cursor.execute("""CREATE TABLE IF NOT EXISTS Products (
                id VARCHAR(10) PRIMARY KEY, name VARCHAR(255), price DECIMAL(10,2), 
                currency VARCHAR(10), stock INT, categoryRef VARCHAR(10),
                FOREIGN KEY (categoryRef) REFERENCES Categories(id))""")
            
            tree = etree.parse(self.xml_file)
            
            # Dung XPath de lay du lieu
            for cat_id, cat_name in zip(
                tree.xpath('//categories/category/@id'),
                tree.xpath('//categories/category/text()')
            ):
                cursor.execute("INSERT INTO Categories VALUES (%s, %s) ON DUPLICATE KEY UPDATE name=VALUES(name)", 
                             (cat_id, cat_name))
            
            for prod_id, category_ref, name, price, currency, stock in zip(
                tree.xpath('//products/product/@id'),
                tree.xpath('//products/product/@categoryRef'),
                tree.xpath('//products/product/name/text()'),
                tree.xpath('//products/product/price/text()'),
                tree.xpath('//products/product/price/@currency'),
                tree.xpath('//products/product/stock/text()')
            ):
                cursor.execute("""INSERT INTO Products VALUES (%s, %s, %s, %s, %s, %s) 
                    ON DUPLICATE KEY UPDATE name=VALUES(name), price=VALUES(price), 
                    currency=VALUES(currency), stock=VALUES(stock), categoryRef=VALUES(categoryRef)""",
                    (prod_id, name, float(price), currency, int(stock), category_ref))
            
            conn.commit()
            print("Da luu du lieu thanh cong")
            
            # Hien thi du lieu
            self.hien_thi_du_lieu(cursor)
            
        except Exception as e:
            print(f"Loi: {e}")
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

if __name__ == "__main__":
    XMLProcessor('buoi6_HuynhDangKhoa/products.xml', 'buoi6_HuynhDangKhoa/schema.xsd').xu_ly()