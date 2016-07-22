from tinydb import TinyDB, Query
import cProfile

def update_test(db_file='db.json'):
    db = TinyDB(db_file)
    customer = Query()
    db.update({'items': 990}, customer.contact == 9734286136)
	
def main():
    cProfile.run("update_test()")
	
if __name__ == '__main__':
    main()