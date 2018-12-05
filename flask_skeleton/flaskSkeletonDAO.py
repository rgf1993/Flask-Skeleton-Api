from flask_skeleton import db, app
import psycopg2
import psycopg2.extras
import json
from sqlalchemy import exc 
#import logging

def get_user():
    conn = psycopg2.connect(app.config["SQLALCHEMY_DATABASE_URI"])
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    stmt = """select * from users"""
    cur.execute(stmt)
    result = cur.fetchall()
    dict_result = []
    for row in result:
        dict_result.append(dict(row))

    cur.close()
    conn.close()
    return dict_result
