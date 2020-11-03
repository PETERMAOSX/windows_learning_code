import sqlite3
books = [("021",25,"大学计算机"),("022",30,"大学英语"),("023",18,"艺术欣赏"),("024",35,"高级语言程序设计")]
Con = sqlite3.connect("M:\sales.db")
Cur = Con.cursor()
Cur.execute("insect into book(id,price,name)")