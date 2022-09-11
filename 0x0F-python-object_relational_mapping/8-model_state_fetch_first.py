#!/usr/bin/python3
"""Prints the first state object from database hbtn_0e_6_usa"""

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
    try:
        f_state = session.query(State).order_by(State.id).first()
        if f_state:
            print("{}: {}".format(f_state.id, f_state.name))
        else:
            print("Nothing")
    except:
        print("Nothing")
    session.close()

