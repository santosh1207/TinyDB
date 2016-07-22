from tinydb import TinyDB, Query
import cProfile

def insert_test(db_file='db.json'):
    db = TinyDB(db_file)
    db.insert({
        'name': 'Aman Verma',
        'items': 1,
        'contact': 7890701597
    })

	
def main():
     cProfile.run("insert_test()")
    
if __name__ == '__main__':
    main()