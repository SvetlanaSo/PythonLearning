import sys
sys.path.insert(1, "/Users/Svetlana/PythonLearning/NumberGuesser/application")
from number_guesser import is_valid

tests = [
[111,False],
[99,True],
[1,True],
[50,True],
["a",False],
["1",True],
[-1,False],
['-1',False],
['0',False],
[1.5,False],
['1.5',False],
["%",False],
["сто",False],
["два",False],
[0x36,False],
['',False],
[' ',False],
[' 7',False]
]
test_num = 0
for test in tests:
    test_num+=1
    out_value = is_valid(test[0], 100)
    if out_value==test[1]:
        result = "success"
    else:
        result = "failure" 
    print('{:2d} {:10s} {:7s}    {:4s}{:6s}  {:8s}{:6s}'.format( test_num, str(test[0]), str(result), "got:",str(out_value), "expected:", str(test[1])))