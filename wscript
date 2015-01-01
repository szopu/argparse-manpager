#! /usr/bin/env python

# The next two lines enable the use of the manpyger waftool before installing it. When you
# use the tool in your own projects and argparse-mapager is installed, you do not need them.
from sys import path
path.append("waftools")

def options(ctx):
    ctx.load('manpyger')

def configure(ctx):
    ctx.load('manpyger')
    ctx.check_python_version()

def build(ctx):
    ctx(features="py", source=ctx.path.find_dir("manpager").ant_glob("**/*.py"))
    ctx(features="entrypynt", modules="manpager", target="manpager.sh")
