from lib.tyres_class_system import *
import datetime as dt

def test_init_create_blank_dictionary():
    RF = Tyre()
    assert RF.data == []
    
def test_record_data_create_one_record():
    RF = Tyre()
    RF.record_data('1', '1', '11/6/25') 
    assert RF.data == [{'11/6/25': ['1', '1']}]
    
def test_record_two_entries_create_one_record():
    RF = Tyre()
    RF.record_data('1', '1', '11/6/25')
    RF.record_data('2', '2', '11/6/25')
    assert RF.data[1] == {'11/6/25': ['2', '2']}