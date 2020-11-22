import sqlite3

db_path = "static/db/documents.db"


def get_cursor():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_table(cursor)
    return conn, cursor


def create_table(cursor):
    sql = "CREATE TABLE IF NOT EXISTS MYDOC(name CHAR(50) PRIMARY KEY NOT NULL,content TEXT,size INT)"
    cursor.execute(sql)


def get_doc_from_sqlite(doc_name):
    conn, cursor = get_cursor()
    cursor.execute(f"SELECT content FROM MYDOC WHERE name='{doc_name}'")
    doc = cursor.fetchone()[0]
    return doc


def save_html_to_sqlite(html_dict):
    conn, cursor = get_cursor()
    for name, html in html_dict.items():
        cursor.execute(f"SELECT * FROM MYDOC WHERE name='{name}'")
        result = cursor.fetchone()
        if result and result[-1] != len(html):
            cursor.execute(f"UPDATE MYDOC SET content='{html}', size={len(html)} WHERE name='{name}'")
        elif result is None:
            cursor.execute("INSERT INTO MYDOC VALUES (?,?,?)", (name, html, len(html)))
        else:
            print(f"{name} NO UPDATE")
    conn.commit()
