import unittest
import Backend.dbconnection
class Test_Database(unittest.TestCase):
    def setUp(self):
        self.ob=Backend.dbconnection.Database()

    def test_fetchcourse(self):
        query="select * from new_table"
        row=self.ob.fetch_all(query)
        y=bool(row)
        self.assertEqual(True,y)

    def test_addcourse(self):
        q1="Insert into new_table(course_name,duration,course_credit,charges,course_head,description) values('Python',15,10,12000,'Ishwor','No')"
        a=bool(self.ob.add(q1))
        self.assertEqual(False,a)

    def test_update(self):
        q2="update new_table set course_name='Java',duration =25, course_credit=10, charges=15000, course_head='Sujan', description='Noneed'where id=39"
        a=bool(self.ob.update(q2))
        print(a)


    def test_delete(self):
        q3="delete from new_table where id=29"
        self.ob.delete(q3)

    def test_search(self):
        q4="select name , select_gender from student where roll=29"
        rows=bool(self.ob.fetch_all(q4))
        self.assertIsNot(True,rows)




if __name__=="__main__":
    obj=Test_Database()





