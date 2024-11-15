import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def group():
    pass

@group.command()
@click.option(
    "-n",
    "--number",
    default=0,
    help = "Number is the amount of values between 0 and 2 π to calculate the sine with."
)
def sin(number):
    """Caculate the sine of x, an integer between 0 and 2 π, for n times.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@group.command()
@click.option(
    "-n",
    "--number",
    default = 0,
    help = "Number is the amount of values between 0 and 2 π to calculate the tangent with."
)
def tan(number):
    """Caculate the tangent of x, an integer between 0 and 2 π, for n times.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    group()