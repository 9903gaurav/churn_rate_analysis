import mysql.connector
from dotenv import load_dotenv
import os

def fetch_data_from_db(sql_query):
    load_dotenv()

    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")

    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql_query)
        result = cursor.fetchall()
        connection.commit()
        return result
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        connection.close()
