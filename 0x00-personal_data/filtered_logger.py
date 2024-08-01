#!/usr/bin/env python3
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector import connection


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    for field in fields:
        message = re.sub(
            f'{field}=.*?{separator}', f'{field}={redaction}{separator}',
            message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(
                self.fields, self.REDACTION, record.msg, self.SEPARATOR
            )
        return super(RedactingFormatter, self).format(record)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> connection.MySQLConnection:
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )


def main():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    logger = get_logger()

    for row in cursor.fetchall():
        message = (
                "name={}; email={}; phone={}; ssn={}; password={}; ip={}; "
                "last_login={}; user_agent={}".format(
                    name, email, phone, ssn, password,
                    ip, last_login, user_agent
                    )
                )

        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
