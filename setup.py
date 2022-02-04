# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe

setup(
    name="lecturas",
    version="1.0",
    description="mini sistema para henerar pruebas de lecturas",
    author="LaloDev",
    author_email="juancontreras10noeggertah@gmail.com",
    url="s/n",
    license="s/n",
    scripts=["lecturaView.py"],
    console=["lecturaView.py"],
    options={"py2exe": {"bundle_files": 1}},
    zipfile=None,
)