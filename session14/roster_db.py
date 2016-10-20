import dbm
import random

def create_db():
    '''
    return a new dabase containing names and 0s
    '''
    ROSTER = ("Beshansky",
                "Collins",
                "Fischer",
                "Giovanucci",
                "Jain",
                "Kim",
                "Lauture",
                "Lee",
                "Maddox",
                "Martinez",
                "Mendez",
                "Oh",
                "Petrone",
                "Posada",
                "Rule",
                "Schilb",
                "Tariq",
                "Wang",
                "Wolf")
    visits = ['0']
    db = dbm.open('db_student', 'c')
    for student in ROSTER:
        db[student] = random.choice(visits)
    db.close()
    return db


def call(db_name):
    '''
    Among the names that are called least times,
    return one name randomly.

    update database after each call.
    '''
    db = dbm.open(db_name, 'c')
    

def display_all(db_name):
    '''
    display all names and values
    '''
    db = dbm.open(db_name, 'r')
    for student in db:
        print(student, db[student])
    db.close()

# new_db = create_db()
display_all('db_student')
call('db_student')
