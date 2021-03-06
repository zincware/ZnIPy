import os
from distutils import dir_util

import pytest

import znipy


@pytest.fixture
def datadir(tmpdir, request):
    """
    Fixture responsible for searching a folder with the same name of test
    module and, if available, moving all contents to a temporary directory so
    tests can use them freely.

    References
    ----------
    https://stackoverflow.com/a/29631801/10504481
    """
    filename = request.module.__file__
    test_dir, _ = os.path.splitext(filename)

    if os.path.isdir(test_dir):
        dir_util.copy_tree(test_dir, str(tmpdir))

    return tmpdir


@pytest.fixture()
def module(datadir):
    os.chdir(datadir)
    znipy.register()
    import example_nb

    return example_nb


def test_HelloWorld(datadir):
    os.chdir(datadir)
    znipy.register()
    import example_nb

    assert example_nb.HelloWorld().get_name() == "HelloWorld"

    from example_nb import HelloWorld

    assert HelloWorld().get_name() == "HelloWorld"

    assert example_nb.HelloWorld is HelloWorld


def test_AbstractClass(module):
    with pytest.raises(TypeError):
        _ = module.AbstractClass()


def test_MyMethod(module):
    assert module.MyMethod().abstract_method() == "Lorem Ipsum"


def test_return_str(module):
    assert module.return_str("Lorem Ipsum") == "Lorem Ipsum"


def test_func_with_decorator(module):
    assert module.func_with_decorator() == 42
