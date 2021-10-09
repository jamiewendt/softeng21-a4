import pytest
from pmgr.project import Project 

@pytest.fixture(scope="function")
def testproj():
    testproj = Project('clean')
    yield testproj
    #testproj.delete()
    

def test_add_task(testproj):
    #testproj.add_task("dust")
    assert "dust" in testproj.get_tasks()






#def test_add_task(self, task_name):
 #  assert add_task(test, sweep) == 'sweep'

#def test_get_tasks(object_):
 #   assert object_.get_tasks() == ['vaccuum']

    #assert test2.get_tasks() == []

