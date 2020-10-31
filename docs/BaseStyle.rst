.. currentmodule:: restext.style

Style
=====

Base Style
----------

Base class for reStructuredText markup implementations.

:class:`BaseStyle` is used for :ref:`ReSTStyle<reststyle>`

.. class:: BaseStyle

    .. attribute:: doc

        List to store all converted text.

    .. attribute:: indent_width

        Number of spaces to the left for indentation. (default: 2)

    .. attribute:: _indent

        Number that will be multiplied with `indent_width` to return the total number of indentations.

        It should not be accessed directly.

    .. attribute:: indentation

        Read-write property that returns *_indent*.

    .. method:: new_paragraph()

        Returns a new line with indentation.

    .. method:: indent()

        Sum 1 to current indent. (``_indent``)

    .. method:: dedent()

        Decrements 1 the current indent. (``_indent``)

    .. method:: spaces()

        Returns the total number of spaces for indentation. (``_indent * indent_width``)

    .. method:: bold()

        Not implemented

    .. method:: ref()

        Not implemented

    .. method:: h2()

        Not implemented

    .. method:: h3()

        Not implemented

    .. method:: underline()

        Not implemented

    .. method:: italics()

        Not implemented


ReST Style
----------

Class that actually implements the functions that transform the text into a markup language.

.. class:: ReSTStyle(BaseStyle)

