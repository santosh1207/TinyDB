import random

from tinydb import TinyDB

phone_number = set()


def generate_phone_num():
    global phone_number
    while True:
        ph = random.randint(9000000000L, 9999999999L)
        if ph not in phone_number:
            phone_number.add(ph)
            return ph


def generate_names(first_names, last_names, last_name_first=False):
    for fn in first_names:
        for ln in last_names:
            if last_name_first:
                yield "{}, {}".format(ln, fn)
            else:
                yield "{} {}".format(fn, ln)


def generate_customer_records(seed_first_names, seed_last_names, count=320, file_name='db.json', min_items=1,
                              max_items=50):
    db = TinyDB(file_name)

    names = [name for name in generate_names(seed_first_names, seed_last_names)]  # Generate the names
    random.shuffle(names)  # Shuffle to make them look "more" random

    for i in xrange(count):
        db.insert({
            'name': names[random.randint(0, len(names) - 1)],
            'items': random.randint(min_items, max_items),
            'contact': generate_phone_num()
        })


def main():
    first_names = ["Charles", "Marie", "Sarah", "Anurag"]
    last_names = ["Charmichael", "Gautam", "Walker", "Deamon"]
    generate_customer_records(first_names, last_names)

#main()
print("Successfully automated the requested number of records of customers and stored in the db.json file! And also finding the time taken to execute the test cases")
import cProfile

if __name__ == '__main__':
    cProfile.run("main()")