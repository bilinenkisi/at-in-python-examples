# test_student.py
import pytest
from student import Student


@pytest.fixture
def example_student():
    """Creates an example student object for testing"""
    s = Student("Ali", "Veli")
    return s
    # Not: Bu fixture test için hazır bir öğrenci nesnesi oluşturur


def test_student_creation():
    """Tests student object creation"""
    s = Student("Ayşe", "Fatma")
    assert s.first_name == "Ayşe"
    assert s.last_name == "Fatma"
    assert s.first_name_cap == "Ayşe".capitalize()
    assert s.points == []
    # Not: Öğrenci nesnesi doğru oluşturuldu mu kontrol edildi


def test_adding_points(example_student):
    """Tests adding points to a student"""
    example_student.add_point(70)
    example_student.add_point(80)
    example_student.add_point(90)
    assert len(example_student.points) == 3
    assert 70 in example_student.points
    assert 80 in example_student.points
    assert 90 in example_student.points
    # Not: Puanlar öğrenci nesnesine doğru ekleniyor mu kontrol edildi


def test_invalid_points(example_student):
    """Tests adding invalid points"""
    with pytest.raises(ValueError):
        example_student.add_point(-10)
    with pytest.raises(ValueError):
        example_student.add_point(110)
    with pytest.raises(TypeError):
        example_student.add_point("asd")
    # Not: Geçersiz puanlar için hata fırlatılıyor mu kontrol edildi


def test_average_calculation(example_student):

    """Tests grade average calculation"""
    assert example_student.calculate_avg() == 0

    example_student.add_point(60)
    assert example_student.calculate_avg() == 60

    example_student.add_point(80)
    assert example_student.calculate_avg() == 70
    # Not: Ortalama hesaplama farklı durumlar için test edildi


@pytest.mark.parametrize("points,expected_result", [
    ([70, 80, 90], True),  # Successful
    ([40, 50, 60], False),  # Failure
    ([60, 60, 60], True),  # On Edge of Failure
    ([], False)  # N/A
])
def test_is_successful(example_student, points, expected_result):
    """Tests success status with different points"""
    for point in points:
        example_student.add_point(point)
    assert example_student.is_successful() == expected_result
    # Not: Farklı puan senaryoları için başarı durumu test edildi