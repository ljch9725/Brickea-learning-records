"""
Create all table that the project needs
"""
import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker
from env_init import database_flask_env_init

database_flask_env_init()

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def user_init():
    db.execute(text('drop table if exists users'))
    sql = text('''create table users(
            id serial primary key,
            username varchar not null unique,
            password varchar not null
        );''')
    db.execute(sql)
    db.commit()

def book_init():
    db.execute(text('drop table if exists books'))
    sql = text('''create table books(
            id serial primary key,
            isbn varchar not null unique,
            title varchar not null,
            author varchar not null,
            year varchar not null
        );''')
    db.execute(sql)
    db.commit()

def review_init():
    db.execute(text('drop table if exists reviews'))
    sql = text('''create table reviews(
            id serial primary key,
            username varchar references users(username) not null,
            isbn varchar references books(isbn) not null,
            comment varchar not null,
            star varchar not null
        );''')
    db.execute(sql)
    db.commit()

def main():
    review_init()
    

if __name__ == "__main__":
    main()
