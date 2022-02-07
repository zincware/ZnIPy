import os
from distutils import dir_util

import pytest

from znipy import NotebookLoader


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
def loader(datadir):
    return NotebookLoader(file=datadir.join("./example_nb.ipynb"))


def test_HelloWorld(loader):
    module = loader.load_module()
    assert module.HelloWorld().get_name() == "HelloWorld"


def test_AbstractClass(loader):
    module = loader.load_module()
    with pytest.raises(TypeError):
        _ = module.AbstractClass()


def test_MyMethod(loader):
    module = loader.load_module()
    assert module.MyMethod().abstract_method() == "Lorem Ipsum"


def test_return_str(loader):
    module = loader.load_module()
    assert module.return_str("Lorem Ipsum") == "Lorem Ipsum"


def test_func_with_decorator(loader):
    module = loader.load_module()
    assert module.func_with_decorator() == 42
