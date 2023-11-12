# Colorful Grid Module

A simple Python module for creating and manipulating a grid with colored symbols.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python module provides a `Grid` class that allows you to create a grid and set colored symbols at specific coordinates. The module uses ANSI escape codes for terminal color formatting.

## Installation

1. Install the [colorama](https://pypi.org/project/colorama/) library:

    ```bash
    pip install colorama
    ```

2. Download the `colorful_grid.py` file from this repository.

## Usage

1. Import the `Grid` class from `colorful_grid.py`:

    ```python
    from colorful_grid import Grid
    ```

2. Create a `Grid` object with the desired width and height:

    ```python
    my_grid = Grid(5, 5)
    ```

3. Use the `create_symbol` method to set a colored symbol at specific coordinates:

    ```python
    my_grid.create_symbol('R', 0, 0, 255, 0, 0)
    ```

4. Use the `delete_symbol` method to remove a symbol at specific coordinates:

    ```python
    my_grid.delete_symbol(2, 2)
    ```

5. Draw the grid using the `draw_grid` method:

    ```python
    my_grid.draw_grid()
    ```

## Example

Here's a simple example demonstrating the usage:

```python
from colorful_grid import Grid

my_grid = Grid(5, 5)

my_grid.create_symbol('R', 0, 0, 255, 0, 0)
my_grid.create_symbol('G', 2, 2, 0, 255, 0)
my_grid.create_symbol('B', 4, 4, 0, 0, 255)

my_grid.draw_grid()

my_grid.delete_symbol(2, 2)

my_grid.draw_grid()
```

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Please follow the [Contributing Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
