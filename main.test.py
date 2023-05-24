import unittest


cnx = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    port=int(os.environ.get("DB_PORT")),
    user=os.environ.get("DB_USER")

)

corsa = cnx.cursor()

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here




if __name__ == '__main__':
    unittest.main()
