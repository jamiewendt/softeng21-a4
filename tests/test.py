import pytest
from pmgr.project import Project, TaskException

#test = Project('clean')

test2 = Project('bake')

#test.add_task('vacuum')

#def test1():
#     test1 = Project('clean')
#     test1.add_task('vacuum')
#     yield test1
#     test1.remove_task('vacuum')

def test_get_tasks(test1):
    assert test1.get_tasks() == ['vacuum']
    assert test2.get_tasks() == []
