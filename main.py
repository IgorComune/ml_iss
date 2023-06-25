import psycopg2
from time import sleep
from download_data import Download

class Postgre():
    def __init__(self) -> None:
        pass

    def download_data():
        # Calls the `iss_api` method from the `Download` class to download data
        values = Download().iss_api()
        return values
    
    def db(self):
        # Establishes a connection to the PostgreSQL database
        hostname = "localhost"
        username = "postgres"
        password = "1234"
        database = "ISS"
        schema = "public"
        
        conn = psycopg2.connect(host=hostname, 
                                user=username, 
                                password=password, 
                                dbname=database, 
                                options=f'-c search_path={schema}')
        cur = conn.cursor()
        
        return cur, conn

    def close_connection(self):
        # Closes the database connection
        cur, conn = Postgre.db()
        cur.close()
        conn.close()
        print('Connection Closed!')
        
    def insert_db(self):
        # Retrieves data from the ISS API using the `download_data` method
        values = Postgre.download_data()
        print(values)
        
        # Converts values to strings
        value0 = str(values[0])
        value1 = str(values[1])
        value2 = str(values[2])
        value3 = str(values[3])
        value4 = str(values[4])
        value5 = str(values[5])
        value6 = str(values[6])
        value7 = str(values[7])
        value8 = str(values[8])
        value9 = str(values[9])
        value10 = str(values[10])
        value11 = str(values[11])
        value12 = str(values[12])
        
        # Establishes a database connection
        cur, conn = Postgre.db()
        
        # Executes an SQL INSERT statement to insert values into the 'iss_table' table
        cur.execute(f"INSERT INTO iss_table (name, id, latitude, longitude, altitude, velocity, visibility, footprint, timestamp, daynum, solar_lat, solar_lon, units) VALUES ('{value0}', '{value1}', '{value2}', '{value3}', '{value4}', '{value5}', '{value6}', '{value7}', '{value8}', '{value9}', '{value10}', '{value11}', '{value12}')")
        
        # Commits the transaction
        conn.commit()
        print('Values successfully inserted into the iss_table')
        
        # Closes the database connection
        Postgre.close_connection()
        
if __name__ == '__main__':
    # Loops indefinitely and inserts data into the database every 60 seconds
    while True:
        Postgre.insert_db()
        sleep(60)