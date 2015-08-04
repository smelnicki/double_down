Double down
-----------

A silly example of a python decorator.

Simply calls the decorated function twice.


Installation
------------

::

    pip install double_down


Usage
------------

.. code:: python

    # example.py
    from double_down import double_down

    @double_down
    def hello():
        print "Hello, Python"

    if __name__ == "__main__":
      hello()


Then in your terminal:

::

    > python example.py
    Hello, Python
    Hello, Python
