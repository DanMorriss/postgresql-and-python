from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a classed based model for the "Programme" table


class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# Instead of connecting to the database directly, we will ask for a session
# Create a new instance of sessionmaker, then point to our engine (the database)
Session = sessionmaker(db)
# Open an actual session by calling the Session subclass defined above
session = Session()

# Create the database using declarative_base subclass
base.metadata.create_all(db)

# Creating records on our programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_touring = Programmer(
    first_name="Alan",
    last_name="Touring",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_burners_lee = Programmer(
    first_name="Tim",
    last_name="Burners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

dan_morriss = Programmer(
    first_name="Dan",
    last_name="Morriss",
    gender="M",
    nationality="British",
    famous_for="Language Integration"
)

# Add each instance of our programmers to the session
session.add(ada_lovelace)
session.add(alan_touring)
session.add(grace_hopper)
session.add(margaret_hamilton)
session.add(bill_gates)
session.add(tim_burners_lee)
session.add(dan_morriss)

# Commit our session to the database
session.commit()

# Updating a single record
# programmer = session.query(Programmer).filter_by(id=11).first()
# programmer.famous_for = "World President"

# Updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# Defensive programming
# if programmer is not None:
#     print("Programmer found: " + programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n)")
#     if confirmation.lower() == 'y':
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
# else:
#     print("No records found")

# delete multipple records
# programmers = session.query(Programmer)
# confirmation = input("Are you sure? This action cannot be undone (y/n)")
# if confirmation.lower() == 'y':
#     for programmer in programmers:
#         session.delete(programmer)
#         session.commit()
#     print("All records deleted")

# Query the databse to find all the programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
