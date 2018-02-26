##Spanish 1-38 Vocab Quiz
import sqlite3

words = sqlite3.connect("wordandans.db")
cursor = words.cursor()

def insertwords():
    espimport = str(input("Enter spanish word --> "))
    engimport = str(input("Enter english word --> "))
    cursor.execute("INSERT INTO words VALUES (?, ?)", (espimport, engimport))
    words.commit()
    insertwords()

insertwords()
