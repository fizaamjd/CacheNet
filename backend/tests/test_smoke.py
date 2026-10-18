import sys


def test_python_runtime_is_supported():
    assert sys.version_info >= (3, 9)


def test_package_imports_are_available():
    import fastapi
    import pydantic

    assert fastapi is not None
    assert pydantic is not None
