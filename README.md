[![Coverage Status](https://coveralls.io/repos/github/zincware/ZnIPy/badge.svg?branch=main)](https://coveralls.io/github/zincware/ZnIPy?branch=main)

# ZnIPy - Easy imports from Jupyter Notebooks

See [Importing Jupyter Notebooks as Modules](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Importing%20Notebooks.html) for more information.

```python
from znipy import NotebookLoader

module = NotebookLoader().load_module("JupyterNotebook.ipnyb")

hello_world = module.HelloWorld()
```
or with direct imports
```python
import znipy
znipy.register()

from JupyterNotebook import HelloWorld

hello_world = HelloWorld()
```
