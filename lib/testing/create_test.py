#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect(":memory:")
cursor = connection.cursor()


with open("lib/create.sql") as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

class TestCreate:
    '''Tests for the bears table schema'''

    def test_creates_bears_with_name_column(self):
        '''creates a table "bears" with a column "name".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert("name" in columns)

    def test_creates_bears_with_age_column(self):
        '''creates a table "bears" with a column "age".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert("age" in columns)

    def test_creates_bears_with_sex_column(self):
        '''creates a table "bears" with a column "sex".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert("sex" in columns)

    def test_creates_bears_with_color_column(self):
        '''creates a table "bears" with a column "color".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert("color" in columns)

    def test_creates_bears_with_temperament_column(self):
        '''creates a table "bears" with a column "temperament".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert("temperament" in columns)

    def test_creates_bears_with_alive_column(self):
        '''creates a table "bears" with a column "alive".'''
        columns = [column[1] for column in cursor.execute("PRAGMA table_info(bears);")]
        assert("alive" in columns)

    def test_creates_bears_with_id_pk(self):
        '''creates a table "bears" with a primary key "id".'''
        columns = [column for column in cursor.execute("PRAGMA table_info(bears);")]
        assert(columns[0][1] == "id" and columns[0][5] == 1)  # Check if 'id' is primary key