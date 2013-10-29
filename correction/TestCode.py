# -*- coding: utf-8 -*-
'''
Created on 9 déc. 2012

@author: Vincent Bruneau, Johann Verbroucht
'''
import unittest
import sys
from Code import Code
from Student import Student
from Mark import Mark

class Test(unittest.TestCase):


    def test_get_list_size(self):
        list1 = [1, 4, 3, 2, 3, 4]
        list2 = [1, 4, 3]
        list3 = list()
        code = Code()
        assert 6 == code.get_list_size(list1)
        assert 3 == code.get_list_size(list2)
        assert 0 == code.get_list_size(list3)
        
    def test_factoriel(self):
        code = Code()
        assert 40320 == code.factoriel(8)
        assert 1 == code.factoriel(0)
        assert 6 == code.factoriel(3)
        
    def test_get_max_in_list(self):
        list1 = [1, 24, 3, 12, 3, 4, 23]
        list2 = [1, 4, 3]
        list3 = list()
        code = Code();
        assert 24 == code.get_max_in_list(list1)
        assert 4 == code.get_max_in_list(list2)
        assert 0 == code.get_max_in_list(list3)

    def test_sort_list(self):
        list1 = [1, 24, 3, 12, 3, 4, 23]
        list2 = [1, 4, 3, 2]
        list3 = [1, -4, 3, 12]
        sorted_list1 = [1, 3, 3, 4, 12, 23, 24]
        sorted_list2 = [1, 2, 3, 4]
        sorted_list3 = [-4, 1, 3, 12]
        code = Code()
        assert sorted_list1 == code.sort_list(list1);
        assert sorted_list2 == code.sort_list(list2);
        assert sorted_list3 == code.sort_list(list3);
        
    def test_delete_uneven(self):
        list1 = [1, 24, 3, 12, 3, 4, 23]
        list2 = [1, -4, 3, 2]
        list3 = [1, 3, 3, 17]
        result1 = [24, 12, 4]
        result2 = [-4, 2]
        result3 = []
        code = Code()
        assert result1 == code.delete_uneven(list1);
        assert result2 == code.delete_uneven(list2);
        assert result3 == code.delete_uneven(list3);

    def test_get_occurrence(self):
        string1 = "abababababab"
        string2 = "oublié aba trada"
        string3 = "I love chocolat"
        code = Code()
        assert 6 == code.get_occurrence("a", string1)
        assert 1 == code.get_occurrence("oublié", string2)
        assert 0 == code.get_occurrence("latlat", string3)
        assert 2 == code.get_occurrence("foo", "foobar foo")
        assert 3 == code.get_occurrence("foo", "foofoo foobar")
            
    def test_create_student(self):
        code = Code()
        studentid = 3
        studentlastname = "StudentLastname"
        studentfirstname = "StudentFirstname"
        teacherid = 15
        teacherlastname = "TeacherLastname"
        teacherfirstname = "TeacherFirstname"
        
        student = code.create_student(studentid, studentlastname, studentfirstname, teacherid, teacherlastname, teacherfirstname)
        assert studentid == student.peopleid
        assert studentlastname == student.lastname
        assert studentfirstname == student.firstname
        assert teacherid == student.teacher.peopleid
        assert teacherlastname == student.teacher.lastname
        assert teacherfirstname == student.teacher.firstname
        
    def test_get_average(self):
        code = Code()
        marklist1 = [Mark(mark=18), Mark(mark=12), Mark(mark=14), Mark(mark=16)]
        student1 = Student()
        student1.marklist = marklist1

        marklist2 = [Mark(mark=18), Mark(mark=12), Mark(mark=0)]
        student2 = Student()
        student2.marklist = marklist2

        assert 15 == code.get_average(student1)
        assert 10 == code.get_average(student2)
        
    def test_get_best_mark(self):
        code = Code()
        mark1 = Mark(mark=18)
        marklist1 = [mark1, Mark(mark=12), Mark(mark=14), Mark(mark=16)]
        student1 = Student()
        student1.marklist = marklist1

        mark2 = Mark(mark=12)
        marklist2 = [Mark(mark=8), mark2, Mark(mark=0)]
        student2 = Student()
        student2.marklist = marklist2

        assert mark1 == code.get_best_mark(student1)
        assert mark2 == code.get_best_mark(student2)
        
    def test_sort_mark_list(self):
        code = Code()
        mark1 = Mark(mark=18)
        mark2 = Mark(mark=12)
        mark3 = Mark(mark=14)
        mark4 = Mark(mark=16)
        marklist1 = [mark1, mark2, mark3, mark4]
        student1 = Student()
        student1.marklist = marklist1

        mark21 = Mark(mark=8)
        mark22 = Mark(mark=12)
        mark23 = Mark(mark=0)
        marklist2 = [mark21, mark22, mark23]
        student2 = Student()
        student2.marklist = marklist2
        
        sorted_marklist1 = [mark2, mark3, mark4, mark1]
        sorted_marklist2 = [mark23, mark21, mark22]

        assert sorted_marklist1 == code.sort_mark_list(student1)
        assert sorted_marklist2 == code.sort_mark_list(student2)
        
    def test_is_a_kaprekar_number(self):
        code = Code()
        assert code.is_a_kaprekar_number(1)
        assert code.is_a_kaprekar_number(4879)
        assert code.is_a_kaprekar_number(7777)
        assert code.is_a_kaprekar_number(187110)
        assert code.is_a_kaprekar_number(500500)
        assert not(code.is_a_kaprekar_number(0))
        assert not(code.is_a_kaprekar_number(sys.maxint))
        assert not(code.is_a_kaprekar_number(12))
        assert not(code.is_a_kaprekar_number(4444))
        assert not(code.is_a_kaprekar_number(4444))

    def test_is_a_palindrome(self):
        code = Code()
        assert code.is_a_palindrome("Kayak")
        assert code.is_a_palindrome("Esope reste ici et se repose")
        assert code.is_a_palindrome("Eh ! ça va la vache.")
        assert not(code.is_a_palindrome("Lapin"))
        assert not(code.is_a_palindrome("Kaya"))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()