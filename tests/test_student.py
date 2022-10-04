import pytest
from school_schedule.student import Student


def test_new_student():
    EXPECTED_NAME = "Yael"
    EXPECTED_GRADE = "Freshman"
    EXPECTED_CLASSES = ["Algebra II", "Art", "Music"]

    actual_student = Student(EXPECTED_NAME, EXPECTED_GRADE, EXPECTED_CLASSES)

    assert actual_student.name == EXPECTED_NAME
    assert actual_student.grade == EXPECTED_GRADE
    assert actual_student.classes == EXPECTED_CLASSES

def test_add_new_classes():
    EXPECTED_NAME = "Yael"
    EXPECTED_GRADE = "Freshman"
    EXPECTED_CLASSES = ["Algebra II", "Art", "Music"]

    actual_student = Student(EXPECTED_NAME, EXPECTED_GRADE, EXPECTED_CLASSES)
    new_class = "Science"

    actual_student.add_class(new_class)

    assert new_class in actual_student.classes
    assert "Algebra II" in actual_student.classes
    assert "Art" in actual_student.classes
    assert "Music" in actual_student.classes
    assert len(actual_student.classes) == 4