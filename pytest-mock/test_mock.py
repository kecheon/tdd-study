import time
import timeit

RES = 'Response from remote API'


def getFromRemote():
    time.sleep(3)
    return RES


def getResult():
    result = getFromRemote()
    return result


def test_getResult():
    start = timeit.default_timer()
    result = getResult()
    end = timeit.default_timer()
    duration = end - start
    print("\n실행 시간: %f" % duration)
    assert result == RES


def test_with_mock(mocker):
    with mocker.patch('test_mock.getFromRemote', return_value=RES):
        start = timeit.default_timer()
        result = getResult()
        end = timeit.default_timer()
        duration = end - start
        print("\n실행 시간: %f" % duration)
        assert result == RES
