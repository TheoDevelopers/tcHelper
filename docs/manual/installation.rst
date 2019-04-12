Installation
============

.. warning:: This document is out of date and needs to be updated.


tcHelper is still in its early stages of development. It is not
recommended for you to download and try to run tcHelper unless you
know what you are doing.

tcHelper will be compiled for Windows and packaged for Linux and
Mac OS X for easy installation once tcHelper v.1.0 has been
released.

If you are curious and would like to install tcHelper as it is
being developed, follow the following instructions.

Dependencies
------------

-  `pySide2`_ - pySide2 is used as the user interface framework and must
   be installed on your system for tcHelper to run. pySide2 can be
   installed by `pip install PySide2`.

pipenv
~~~~~~~

.. note:: pipenv is the preferred method for installing dependencies needed to run tcHelper.

This project uses pipenv as its virtual environment. pipenv can be used
to download all of the dependencies needed to run tcHelper and also to
download the tools used for development.

See the `pipenv documentation`_ for more information.


Windows
~~~~~~~

At the moment it requires a of effort to run tcHelper in its
current state on Windows.

Download the source files for tcHelper from the `tcHelper
website`_ and decompress the file.

In order to install tcHelper you will have to have `Python3`_
installed on your system. Once Python is installed, you must adjust your
system variables so that that you may run the ``python`` interpreter
without having to ``cd`` into the Python installed directory.
Instructions for setting system variables can be found in the `Python
documentation`_.

Once Python3 is installed, you must install the `PySide framework`_.

Once everything is installed correctly, open your terminal and ``cd``
insto the directory containing the source files you downloaded from this
repository. Run the command ``python main.py`` and tcHelper will
run.

Linux/GNU
~~~~~~~~~

Download the source files for tcHelper from the `tcHelper
website`_ and decompress the file. main.py is the main script for
tcHelper.

Make sure you have Python3 and PySide installed.

Debian
^^^^^^

``sudo apt-get install python3 && sudo apt-get install python3-pyside``
Once that is installed, run ``python3 main.py`` and tcHelper will
run.

.. _pySide2: https://wiki.qt.io/Qt_for_Python
.. _tcHelper website: https://theodevelopers.github.io/tcHelper/
.. _pipenv documentation: https://pipenv.readthedocs.io/en/latest/
.. _Python3: https://www.python.org/downloads/
.. _Python documentation: https://docs.python.org/3.4/using/windows.html
.. _PySide framework: http://qt-project.org/wiki/PySide_Binaries_Windows
