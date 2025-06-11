from lib.tyres_class_system import *

def test_we_can_create_a_tyre_position():
    ford = Car()
    assert ford.RF.data == []
    assert ford.LF.data == []
    assert ford.RR.data == []
    assert ford.LR.data == []

def test_add_single_entry_to_RF():
    ford = Car()
    ford.RF.record_data("1","1","11/06/25")
    assert ford.RF.data == [{"11/06/25": ["1", "1"]}]

def test_add_entry_and_retrieve_single_tyre_history():
    ford = Car()
    ford.RF.record_data("1","1","11/06/25")
    ford.RF.record_data("2","2","10/06/25")
    assert ford.retrieve_single_tyre_data("RF") == [{"11/06/25": ["1","1"]},{"10/06/25": ["2","2"]}]

def test_attempting_to_retrieve_empty_tyre_data():
    ford = Car()
    assert ford.retrieve_single_tyre_data("LF") == "No data recorded"

def test_retrieve_latest_entry_from_each_tyre():
    ford = Car()
    ford.RF.record_data("1","1","11/06/25")
    ford.RF.record_data("2","2","10/06/25")
    ford.LF.record_data("1","1","11/06/25")
    assert ford.retrieve_overview_data() == "RF: Pressure 2, Depth 2, recorded on 10/06/25, LF: Pressure 1, Depth 1, recorded on 11/06/25"
    
    #[{"11/06/25": ["1","1"]},{"10/11/25": ["2","2"]},"No data recorded","No data recorded"]