import pytest

@pytest.fixture
def temporary_file():
    print("Creating file" )
    yield "temp_file.txt"
    print("Deleting file")


def test_temporary_file(temporary_file):
    assert temporary_file == "wrong.txt"
