
import unittest
import json

from pprint import pprint

from subprocess import call

class TestGenomeUtilMethods(unittest.TestCase):

  def test_method(self):
    print("\n\n----------- basic test ----------")

    # write the 



    # call the script with some input
    out = call(["run_KBaseGenomeUtil.sh", 
       "test/script_test/input.json", 
       "test/script_test/output.json", 
       "test/script_test/token.txt"])

    # print error code of implementation
    print(out);

    # read and print output of the function
    with open('test/script_test/output.json') as o:    
        output = json.load(o)
    pprint(output)



if __name__ == '__main__':
    unittest.main()
