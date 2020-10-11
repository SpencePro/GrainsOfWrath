import sqlite3


def delete_entry():
    conn = sqlite3.connect("Brewery.db")
    c = conn.cursor()

    c.execute("""
        DELETE FROM brew WHERE id=?
    """)
    conn.commit()
    conn.close()

delete_entry()
