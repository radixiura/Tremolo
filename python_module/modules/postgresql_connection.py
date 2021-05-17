def connect_postgresql():
    import psycopg2
    from psycopg2 import OperationalError

    def create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print('Connection to PostgreSQL DB sucessful')
        except OperationalError as e:
            print(f"The error '{e}' occured")
        return connection

    connection = create_connection("postgres", "postgres", "serv313", "127.0.0.1", "5432")

    def create_database(connection, query):
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed successfully")
        except OperationalError as e:
            print(f"The error '{e}' occurred")

    create_database_query = "CREATE DATABASE sm_app"
    create_database(connection, create_database_query)

    connection = create_connection(
        "sm_app", "postgres", "abc123", "127.0.0.1", "5432"
    )

    def execute_query(connection, query):
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            print("Query executed sucessfully")
        except OperationalError as e:
            print(f"The error '{e}' has occured")

    create_users_table = """
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        login TEXT NOT NULL,
        password TEXT NOT NULL,
        age INTEGER,
        info TEXT
    )
    """

    execute_query(connection, create_users_table)
