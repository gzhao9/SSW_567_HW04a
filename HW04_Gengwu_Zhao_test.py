import unittest
from HW04_Gengwu_Zhao import *
class TestHW04(unittest.TestCase):
    def test_repo(self):
        User1=gituser("gzhao9")

        self.assertTrue('SSW_555_B'in User1.get_repo_list())
        self.assertTrue('SSW_567'in User1.get_repo_list())
        self.assertTrue('Student-Repository'in User1.get_repo_list())
        self.assertTrue('Triangle_Gengwu_Zhao_567'in User1.get_repo_list())
    
        self.assertGreaterEqual(User1.get_commits('SSW_555_B'),2)
        self.assertGreaterEqual(User1.get_commits('SSW_567'),2)
        self.assertGreaterEqual(User1.get_commits('Student-Repository'),2)
        self.assertGreaterEqual(User1.get_commits('Triangle_Gengwu_Zhao_567'),6)
        self.assertGreaterEqual(User1.get_commits('Nothing'),-1)

if __name__ == '__main__':
    unittest.main()
