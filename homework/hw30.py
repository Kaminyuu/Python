import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    # tel2 = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }
    return person


def gen_tel():
    tel = ''
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(tel) != 10:
        tel += choice(nums)
    return tel


def write_json(person_dict):
    try:
        data = json.load(open('test.json'))
    except FileNotFoundError:
        data = dict()

    data[gen_tel()] = person_dict
    with open('test.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())

