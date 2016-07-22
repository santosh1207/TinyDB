from tinydb import TinyDB, Query
import cProfile

def remove_test(db_file='db.json'):
    db = TinyDB(db_file)
    customer = Query()
    db.remove(customer.items < 40)
	
def main():
     cProfile.run("remove_test()")
    
if __name__ == '__main__':
    main()