"""
# How to use a function-based generator?

(Ref: https://github.com/NVIDIA/garak/blob/17bafad90e4ed16853929a25b247d82568fd3a88/garak/generators/function.py)

Call a given function to use as a generator; specify this as either the
model name on the command line, or as the parameter to the constructor.

This generator is designed to be used programmatically, rather than
invoked from the CLI. An example usage might be:

.. code-block:: python

   import mymodule
   import garak.generators.function

   g = garak.generators.function.Single(name="mymodule#myfunction")

The target function is expected to take a string, and return a string.
Other arguments passed by garak are forwarded to the target function.

Note that one can import the intended target module into scope and then
invoke a garak run via garak's cli module, using something like:

.. code-block:: python

   import garak
   import garak.cli
   import mymodule

   garak.cli.main("--target_type function --target_name mymodule#function_name --probes encoding.InjectBase32".split())

"""

from garak import cli

import chain

cli.main("--config config/garak.yaml".split())
