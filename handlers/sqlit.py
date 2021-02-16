
def reg_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id BIGINT,
        status_start
        ) """)
    db.commit()
    sql.execute(f"SELECT id FROM user_time WHERE id ='{id}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?)", (id, 0))
        db.commit()





def reg_table():
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    sql.execute(""" CREATE TABLE IF NOT EXISTS qwest_1(
            otvet_a BIGINT,
            otvet_b BIGINT,
            otvet_v BIGINT,
            otvet_g BIGINT
            ) """)


    sql.execute(""" CREATE TABLE IF NOT EXISTS qwest_2(
                otvet_a BIGINT,
                otvet_b BIGINT,
                otvet_v BIGINT,
                otvet_g BIGINT
                ) """)

    sql.execute(""" CREATE TABLE IF NOT EXISTS qwest_3(
                    otvet_a BIGINT,
                    otvet_b BIGINT,
                    otvet_v BIGINT,
                    otvet_g BIGINT
                    ) """)
    db.commit()

    sql.execute(f"INSERT INTO qwest_1 VALUES (?,?,?,?)", (0, 0, 0, 0))
    db.commit()
    sql.execute(f"INSERT INTO qwest_2 VALUES (?,?,?,?)", (0, 0, 0, 0))
    db.commit()
    sql.execute(f"INSERT INTO qwest_3 VALUES (?,?,?,?)", (0, 0, 0, 0))
    db.commit()
