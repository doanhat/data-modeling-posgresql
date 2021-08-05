import psycopg2
from sql_queries import create_table_queries, drop_table_queries

t_host = "localhost" # either a domain name, an IP address, or "localhost"
t_port = "5432" # This is the default postgres port
t_dbname = "postgres"
t_user = "admin"
t_pw = "secret"


def create_database():
    """
    - Creates and connects to the sparkifydb
    @return: cursor and connection to sparkifydb
    """

    # connect to default database
    conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=admin password=secret")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    @param cur:
    @param conn:
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list.
    @param cur:
    @param conn:
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database.

    - Establishes connection with the sparkify database and gets
    cursor to it.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.
    """
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()