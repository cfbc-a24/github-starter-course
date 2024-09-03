import copilot1

Raw_Temp=[["20081114", "Chicago", "50.1", "30.0", "35.7"],
 ["20081114", "Detroit", "45.2", "30.3", "33.4"]]

City=["foo"]
Temp=[2000]


def test_compute_mod3():
    expected_output = ['Chicago']
    assert copilot1.lowest_temperature(Raw_Temp, "20081114") == expected_output, "Test Success"


def test_computemod3bis():
    assert(type(City)==list and type(Temp)==list), "wrong types"
    
def test_computed3():
    assert(range(len(Raw_Temp[0]))==range(len(Raw_Temp[1])))
    