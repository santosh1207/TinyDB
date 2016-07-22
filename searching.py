import cProfile
from tinydb import TinyDB, Query


def search_test(db_file='db.json'):
    db = TinyDB(db_file)
    customer = Query()
    print(db.search(customer.contact == 9998875835))
    #print(db.search(customer.contact == 9195755989))
    #print(db.search(customer.items == 45))
    #print(db.search(customer.contact == 9353812690))

def main():
    cProfile.run("search_test()")
	
if __name__=='__main__':
    main()