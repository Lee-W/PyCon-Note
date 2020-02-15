#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = "https://lee-w.github.io/pycon-note"
SITELOGO = "/PyCon-Note/images/avatar.jpg"
RELATIVE_URLS = False

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY = False


MENUITEMS = (
    ("About", "/pycon-note/about.html"),
    ("Archives", "/pycon-note/archives.html"),
    ("Categories", "/pycon-note/categories.html"),
    ("Tags", "/pycon-note/tags.html"),
)
