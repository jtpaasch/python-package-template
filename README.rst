MyTool
======

Short description of what it does.


Installation
------------

Clone the repo into a folder somewhere on your computer, e.g., ~/mytool::

    git clone https://.../mytool.git ~/mytool

Then make a virtual environment and install ``tox``::

    cd ~/mytool
    pyvenv venv
    . bin/venv/activate
    pip install --upgrade pip
    pip install tox

Now use pip to install  the tool globally on your system::

    pip install -e ~/mytool

Or better, install it in a virtual environment::

    mkdir -p ~/venvs/mytool
    cd ~/venvs/mytool
    pyvenv venv
    . venv/bin/activate
    pip install -e ~/mytool


Usage
-----

Run the tool from the command line::

    mytool --help


Tests
-----

To run the tests, install tox, then execute the tox command
from the root of this repo::

    cd ~/mytool
    tox
