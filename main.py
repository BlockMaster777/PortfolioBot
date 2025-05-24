# coding=utf-8
""""
"""
import db_manager
from config import *


if __name__ == '__main__':
    manager = db_manager.DBManager(db_path)
    manager.create_tables()
