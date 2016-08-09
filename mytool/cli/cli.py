# -*- coding: utf-8 -*-

"""The ``cli`` module for the package."""

from os import environ

# The ``click`` package is for building command line tools.
# See http://click.pocoo.org/6/
import click

# Import the tool.
from mytool.jobs.foo import tool


@click.group()
def main():
    pass


@main.command()
def tool():
    output = tool()
    click.echo(output)


@main.command()
@click.argument("message")
@click.option(
    "--repeat",
    is_flag=True,
    help="Repeat the message?")
def echo(message, repeat):
    click.echo(message)
    if repeat:
        click.echo(message)

