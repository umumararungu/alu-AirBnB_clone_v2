#!/usr/bin/python3

import unittest
import MySQLdb

class TestDatabaseFunctionality(unittest.TestCase):
    def setUp(self):
        """Connect to the test database"""
        self.conn = MySQLdb.connect(
            user='hbnb_test',
            password='hbnb_test_pwd',
            host='localhost',
            database='hbnb_test_db'
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
       """Close the database connection"""
        self.cursor.close()
        self.conn.close()

    def test_create_state(self):
        """ Get the initial number of records in the states table """
        self.cursor.execute("SELECT COUNT(*) FROM states")
        initial_count = self.cursor.fetchone()[0]
        
        create_state_function()  # Replace with the actual function call

        self.cursor.execute("SELECT COUNT(*) FROM states")
        final_count = self.cursor.fetchone()[0]
        
        self.assertEqual(final_count, initial_count + 1, "New state was not created")

if __name__ == '__main__':
    unittest.main()

