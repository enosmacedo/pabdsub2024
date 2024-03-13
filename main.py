import psycopg2

def connect_database(databe_name, user_name, host_name, pass_, port_name):
    conn = psycopg2.connect(database = databe_name,
            	            user = user_name,
                            host = host_name,
                            password = pass_,
                            port = port_name)
    return conn


def disconnect_dabase(conn):
    conn.close()


def create_table(conn, name_table, params):
    cmd_sql = "CREATE TABLE " + name_table + "("
    for index, p in enumerate(params):
        if index == len(params) -1 :
            cmd_sql = cmd_sql + p[0] + " " + p[1] 
        else:
            cmd_sql = cmd_sql + p[0] + " " + p[1] + ", "
    cmd_sql = cmd_sql + ")"

    cur = conn.cursor()
    try:
        cur.execute(cmd_sql)
    except:
        print("Nao consegui criar a tabela")
    conn.commit()
    cur.close()


#def insert_element(conn, name_table, params):


if __name__ == '__main__':
    conn = connect_database("ticketcontroller", "postgres", "localhost", "postgres", 5432)
    create_table(conn, "teste4", [("id", "SERIAL PRIMARY KEY"), ("rg", "INTEGER")  ])

    import psycopg2

def connect_database(databe_name, user_name, host_name, pass_, port_name):
    conn = psycopg2.connect(database = databe_name,
            	            user = user_name,
                            host = host_name,
                            password = pass_,
                            port = port_name)
    return conn


def disconnect_dabase(conn):
    conn.close()


def create_table(conn, name_table, params):
    cmd_sql = "CREATE TABLE " + name_table + "("
    for index, p in enumerate(params):
        if index == len(params) -1 :
            cmd_sql = cmd_sql + p[0] + " " + p[1] 
        else:
            cmd_sql = cmd_sql + p[0] + " " + p[1] + ", "
    cmd_sql = cmd_sql + ")"

    cur = conn.cursor()
    try:
        cur.execute(cmd_sql)
    except:
        print("Nao consegui criar a tabela")
    conn.commit()
    cur.close()


def insert_element(conn, name_table, params):
    cmd_sql_colunas = "INSERT INTO " + name_table + "("
    cmd_sql_values  = " VALUES ("

    for index_vetor_params, single_param in enumerate(params):
        if index_vetor_params == len(params) - 1:
            cmd_sql_colunas += single_param[0] + ") "
            cmd_sql_values += single_param[1] + ") "
        else:
            cmd_sql_colunas += single_param[0] + ", "
            cmd_sql_values += single_param[1] + ", "

    cmd_sql = cmd_sql_colunas + cmd_sql_values

    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql)
        print(cmd_sql)
        print("Dados inseridos")
    except Exception as e:
        print(f"Falha: {e}")
    finally:
        conn.commit()
        cursor.close()

def update_element(conn, name_table, condicional, params):
    cmd_sql_colunas = "UPDATE " + name_table + " SET "

    for index_vetor_params, single_param in enumerate(params):
        cmd_sql_colunas += single_param[0] + "=" + single_param[1]
        if index_vetor_params != len(params) - 1: #o ultimo elmento
            cmd_sql_colunas += ", "

    cmd_sql = cmd_sql_colunas + " WHERE " + condicional[0] + " = " + condicional[1] 

    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql)
        print(cmd_sql)
    except Exception as e:
        print(f"Falha: {e}")
    finally:
        conn.commit()
        cursor.close()


def select_elements(conn, name_table, condicional, params):
    cmd_sql = "SELECT "
    for index_vetor_params, single_param in enumerate(params):
        cmd_sql += single_param
        if index_vetor_params != len(params) - 1: #nao for o ultimo elmento
            cmd_sql += ", "

    cmd_sql += " FROM " + name_table + " WHERE "  + condicional[0] + " = " + condicional[1] 

    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql)
        print(cmd_sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Falha: {e}")
    finally:
        conn.commit()
        cursor.close()


def select_all_elements(conn, name_table, params):
    cmd_sql = "SELECT "
    for index_vetor_params, single_param in enumerate(params):
        cmd_sql += single_param
        if index_vetor_params != len(params) - 1: #nao for o ultimo elmento
            cmd_sql += ", "

    cmd_sql += " FROM " + name_table

    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql)
        print(cmd_sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Falha: {e}")
    finally:
        conn.commit()
        cursor.close()


def delete_element(conn, name_table, condicional):
    cmd_sql = "DELETE FROM " + name_table + " WHERE "  + condicional[0] + " = " + condicional[1] 

    cursor = conn.cursor()
    try:
        cursor.execute(cmd_sql)
        print(cmd_sql)
    except Exception as e:
        print(f"Falha: {e}")
    finally:
        conn.commit()
        cursor.close()


if __name__ == '__main__':
    conn = connect_database("ticketcontroller", "postgres", "localhost", "postgres", 5432)
    # create_table(conn, "teste4", [("id", "SERIAL PRIMARY KEY"), ("rg", "INTEGER")  ])

    update_element(conn, "teste4", ("id", "12"), [("rg", "100")])
    select_elements(conn, "teste4", ("id", "12"), ["rg"])
    select_all_elements(conn, "teste4", ["rg"])

    delete_element(conn, "teste4", ("id", "12"))

    disconnect_dabase(conn)
