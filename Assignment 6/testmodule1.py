import module1

list_1 = [10, 20, 30]
list_2 = [10, 30, 30]

def test_compute_matching():
    expected_output = [True, False, True]
    
    assert module1.compute_matching(list_1, list_2) == expected_output, "Test Success"

def test_compute2():
    assert(len(list_1) == len(list_2)), "they should be of the same length"
    
    
def test_compute3():
    assert(list_1!=[] and list_2 !=[]), "empty"
    

