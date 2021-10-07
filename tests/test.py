import pytest
<<<<<<< HEAD
from pmgr.project import Project, TaskException

test = Project('clean')

def test_get_tasks():
    assert test.get_tasks() == []
