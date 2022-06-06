# Calcylator

A CLI calculator implemented with python.

Allow to make the follow operations:

* Addition: **+**
* Subtraction: **-**
* Multiplication: **\***
* Divition: **/**
* Power: **\*\***
* Percent: **%**
* Absolute output: with the specified **~a** option, allow to get absolute values

Have the option to auto-copy to the paperclip with the command **~cp**.

## Installation

Download the current repository in any dir of your computer and remember the path to it.

Install calcylator with pip:

* To just install in path and use it as a command:

    ```bash
    pip install /path/to/calcylator/folder
    ```

* To add the option to edit the script without need to install each time:

    ```bash
    pip install -e /path/to/calcylator/folder
    ```

When installed, run:

```bash
calcylator
```

## Usage/Examples

* For help:

    ```bash
    calcylator ~h
    ```

* Monomials operations:

    ```bash
    calcylator 2+2
    ```

    ```bash
    calcylator 2-2
    ```

    ```bash
    calcylator 2/2
    ```

    ```bash
    calcylator 2*2
    ```

    ```bash
    calcylator 2**2
    ```

    ```bash
    calcylator 2%
    ```

* Polinomials operations:

    ```bash
    calcylator 2+2*2-2/2**2*2%
    ```

* To get the output as an absolute value:

    ```bash
    calcylator ~a -5
    ```

* To auto-copy to paperclip:

    ```bash
    calcylator ~cp 2+2
    ```

**_Notes:_**

* You need to have installed python in your computer.
* Calcylator doesn't resolve algebraic operations.
* The absolute option "**~a**" just it's aplicated for the output, doesn't mean you can write as input somethin like:

    ```bash
    calcylator |-5|
    ```

    This will remove "**|**" and just return **-5**.

## Posible problems

* **~cp** command:

    If you have any problem with the **~cp** option, it's because a problem with the [**_pyperclip_**](https://pyperclip.readthedocs.io/en/latest/) librarie, try to run any of this commands (NOT ALL OF THEM):

    * To install the xsel utility:

        ```bash
        sudo apt-get install xsel
        ```

    * To install the xclip utility:

        ```bash
        sudo apt-get install xclip
        ```

    * To install the gtk Python module:

        ```bash
        pip install gtk
        ```

    * To install the PyQt4 Python module:

        ```bash
        pip install PyQt4
        ```

    For more information, go to the pyperclip website documentation.

## Authors

* [@Cromega08](https://www.github.com/cromega08)

## License

* [GNU AGPL v3.0](https://choosealicense.com/licenses/agpl-3.0/)

## You done your homework?

If you have any feedback, please feel free to fork this repository and update.
