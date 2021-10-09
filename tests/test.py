import pytest
from pmgr.project import Project, TaskException 

@pytest.fixture (scope="function")
def object_():
    test1 = Project('clean')
    


#def test_add_task(self, task_name):
 #  assert add_task(test, sweep) == 'sweep'

def test_get_tasks(object_):
    assert object_.get_tasks() == ['vaccuum']

    #assert test2.get_tasks() == []

