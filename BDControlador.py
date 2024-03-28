import psycopg2

def connect_database(databe_name, user_name, host_name, pass_, port_name):
    conn = psycopg2.connect(database = databe_name,
             	            user = user_name,
                             host = host_name,
                             password = pass_,
                             port = port_name)
    return conn