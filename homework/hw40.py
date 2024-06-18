import sqlite3

gpu_list = [
    ("RTX 4060", 38000, 34),
    ("RTX 4070", 70000, 25),
    ("RTX 4080", 140000, 20),
    ("RX 7600XT", 40000, 73),
    ("RX 7700XT", 50000, 41),
    ("RX 7800XT", 65000, 50),
    ("RX 7900XT", 90000, 22)
]


def read_img(n):
    try:
        with open(f"{n}", "rb") as f:
            return f.read()
    except IOError as e:
        print(e)
        return False


with sqlite3.connect("gpu.db") as con:
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.executescript("""
    CREATE TABLE IF NOT EXISTS gpus(
    gpu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    model TEXT,
    price INTEGER,
    quantity INTEGER
    )
    """)

    cur.executemany("INSERT INTO gpus VALUES(NULL, ?, ?, ?)", gpu_list)


# gpu_list = [
#     ("RTX 4060", 38000, "GPU/RTX4060.png"),
#     ("RTX 4070", 70000, "GPU/RTX4070.png"),
#     ("RTX 4080", 140000, "GPU/RTX4080.png"),
#     ("RX 7600XT", 40000, "GPU/RX7600XT.png"),
#     ("RX 7700XT", 50000, "GPU/RX7700XT.png"),
#     ("RX 7800XT", 65000, "GPU/RX7800XT.png"),
#     ("RX 7900XT", 90000, "GPU/RX7900XT.png")
# ]


# def read_img(n):
#     try:
#         with open(f"{n}", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False


# for x, y, z in gpu_list:
#     img = read_img(z)
#     binary = sqlite3.Binary(img)
#     cur.executemany("INSERT INTO gpus VALUES(NULL, ?, ?, ?)", (x, y, binary))