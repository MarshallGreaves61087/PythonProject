'''
Created on 14 Feb 2019

@author: Marshal61087
'''
import unittest
from example.LabManager import Lab_Manager


class Test(unittest.TestCase):
    
    def setUp(self): #executed for each unit before the test
        print("Initializing Test Environment")
        self.labmanager = Lab_Manager({"name":"Ben",
                                      "location":"Leeds",
                                      "test":"Neck exam",
                                      "result":"All clear"})
        pass

    def tearDown(self):
        print("Releasing Test Environment")
        del self.labmanager
        pass

    def test_lab_manager_create(self):
        print("Lab Manager Creation Test")
        self.assertEqual("Ben",self.labmanager.name, "Name not initialized")
        self.assertEqual("Leeds",self.labmanager.location, "Location not initialized")
        self.assertEqual("Neck exam",self.labmanager.test, "Test not initialized")
        self.assertEqual("All clear",self.labmanager.result, "Result not initialized")
        print("Lab Manager Creation test complete.")
        pass
    
    def test_lab_manager_delete(self):
        pass

    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()