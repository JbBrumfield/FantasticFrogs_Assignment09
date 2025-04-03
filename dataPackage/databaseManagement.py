# File Name : databaseManagement.py
# Student Name: Jacob Brumfield, Nikki Carfora, Ray Happel
# email:  brumfijb@mail.uc.edu, happelrc@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date:  4/3/2025
# Course #/Section:  IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Connect to the professors SQL database to produce interesting results

# Brief Description of what this module does: This module connects to our SQL database GroceryStoreSimulator and querys the database for different information.
# Citations: In Class work, https://stackoverflow.com/questions/28981770/store-sql-result-in-a-variable-in-python, 

# Anything else that's relevant:

import pyodbc

class databaseManagement:
    def connect_to_database(self):
        """
        Connect to our SQL server instance.
        @return: the connection object.
        """
        try:
            conn = pyodbc.connect(
                'Driver={SQL Server};'
                'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                'Database=GroceryStoreSimulator;'
                'uid=IS4010Login;'
                'pwd=P@ssword2;'
            )
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None
        return conn

    def submit_sql_to_server(self, sql_statements, conn):
        """
        Submits a SQL statement to our SQL Server.
        @param conn: connection object.
        @param sql_statements: SQL query string to execute.
        @return: cursor object containing the query results.
        """
        try:
            cursor = conn.cursor()
            cursor.execute(sql_statements)
            return cursor.fetchall() 
        except Exception as e:
            print(f"Error executing query: {e}")
            return None

    def fetch_manufacturer_name(self, manufacturer_id, brand_id, conn):
        """
        Fetches the manufacturer's name by ManufacturerID.
        @param manufacturer_id: The ManufacturerID to look up.
        @param conn: The connection object.
        @return: Manufacturer name or None if not found.
        """
        sql = f"SELECT Manufacturer, Brand FROM tManufacturer, tBrand WHERE ManufacturerID, BrandID = {manufacturer_id, brand_id}"
        results = self.submit_sql_to_server(sql, conn)
        if results and len(results) > 0:
            return results[0][0]  # Manufacturer name is in the second coloumn. 
        else:
            return None
    
    # Me and Jacob agreed to comment this out for, we can delete it later on/in the morning
    # def fetch_brand_name(self, brand_id, conn):
        """
        Fetches the brand's name by BrandID.
        @param brand_id: The BrandID to lookup.
        @param conn: The connection objec
        @return: Manufacturer name or None if not found
        """
        """ 
        sql = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}"
        results = self.submit_sql_to_server(sql, conn)
        if results and len(results) > 0:
            return results[0][0]  # Since we repeated steps 3 and 4, Brand name is in the Second coloumn. 
        else:
            return None # Return None if Brand name is invalid
        """


        
