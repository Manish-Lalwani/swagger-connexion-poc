# people.py

from datetime import datetime
from flask import abort, make_response

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Chopra" : {
                "first_name" : "Rahul",
                "last_name": "Chopra",
                "timestamp": get_timestamp()
                },

    "Kapoor" : {
                "first_name" : "Kunal",
                "last_name": "Kapoor",
                "timestamp": get_timestamp()
                },

    "Agarwal" : {
                "first_name" : "Abhishek",
                "last_name": "Agarwal",
                "timestamp": get_timestamp()
                }
}

def read_all():
    return list(PEOPLE.values())


def create(person_obj):
    last_name = person_obj.get("last_name")
    first_name = person_obj.get("first_name")

    if last_name and first_name not in PEOPLE:
        PEOPLE[last_name] = {
                                "last_name" : last_name,
                                "first_name": first_name,
                                "timestamp": get_timestamp()
                            }
        return PEOPLE[last_name],201
    else:
        abort(406,f"Person with last name {last_name} already lexists")

def read_one(last_name): #this name should be same as /people/{last_name}
    if last_name in PEOPLE:
        return PEOPLE[last_name]
    else:
        abort(404,f"Person with last name {last_name} not found")



def update(last_name,person):
    if last_name in PEOPLE:
        PEOPLE[last_name]["first_name"] = person.get("first_name",PEOPLE[last_name]["first_name"])
        PEOPLE[last_name]["timestamp"] = get_timestamp()
        return PEOPLE[last_name]
    else:
        abort(404,f"Person with last name {last_name} not found")

def delete(last_name):
    if last_name in PEOPLE:
        del PEOPLE[last_name]
        return make_response(f"{last_name} successfully deleted",200)
    else:
        abort(404,f"Person with last name {last_name} not found")