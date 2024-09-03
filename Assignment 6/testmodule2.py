import module2

list_1 = [10, 20, 30]
list_2 = [10, 30, 30]

def test_compute_matching_mod2():
    expected_output = [0, 2]
    
    assert module2.compute_matching_indices(list_1, list_2) == expected_output, "Test Success"

def test_compute2_mod2():
    assert(type(list_1) == type(list_2)), "they should be of the same length"
    
    
def test_compute3_mod2():
    assert(list_1!=[] and list_2 !=[]), "empty lists"
    

