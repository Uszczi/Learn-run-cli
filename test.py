import sys
from io import StringIO


def test_imports():
    stream = StringIO()
    sys.stdout = stream

    try:
        from lrc.main import main
    except Exception as e:
        raise(e)
    else:
        main()

    try:
        from lrc2.main import main
    except Exception as e:
        raise(e)
    else:
        main()


if __name__ == "__main__":
    test_imports()
