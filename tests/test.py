import pytest
from pmgr.project import Project, TaskException 

@pytest.fixture(scope="function")
def testproj():
    testproj = Project('clean')
    yield testproj
    testproj.delete()
    

def test_add_task(testproj):
    testproj.add_task("dust")
    assert "dust" in testproj.get_tasks()

def test_duplicate_add_task(testproj):
    testproj.add_task("vacuum")
    with pytest.raises(TaskException):
        testproj.add_task("vacuum")

def test_remove_task(testproj):
    testproj.add_task("mop")
    testproj.remove_task("mop")
    assert [] == testproj.get_tasks()

def test_no_remove_task(testproj):
    with pytest.raises(TaskException):
        testproj.remove_task("laundry")

def test_get_tasks(testproj):
    assert [] == testproj.get_tasks()
    testproj.add_task("sweep")
    assert "sweep" in testproj.get_tasks()

