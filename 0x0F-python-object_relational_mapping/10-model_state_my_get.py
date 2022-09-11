#!/usr/bin/python3
"""Prints the state object with name passed as argument"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    search = session.query(State).filter(State.name == argv[4]).first()
    if search:
        print(search.id)
    else:
        print("Not found")
    session.close()
