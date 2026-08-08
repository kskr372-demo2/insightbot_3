from app.tools.date_tool import get_current_date
from app.tools.time_tool import get_current_time
from app.tools.random_tool import get_random_number


def test_date_tool():
    result = get_current_date()

    assert result is not None
    assert isinstance(result, str)


def test_time_tool():
    result = get_current_time()

    assert result is not None
    assert isinstance(result, str)


def test_random_tool():
    result = get_random_number()

    assert result is not None
    assert isinstance(result, int)