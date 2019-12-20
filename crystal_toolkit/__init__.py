from __future__ import print_function as _

import os as _os
import sys as _sys
import json

import dash as _dash

# noinspection PyUnresolvedReferences
from ._imports_ import *
from ._imports_ import __all__

if not hasattr(_dash, "development"):
    print(
        "Dash was not successfully imported. "
        "Make sure you don't have a file "
        'named \n"dash.py" in your current directory.',
        file=_sys.stderr,
    )
    _sys.exit(1)

_basepath = _os.path.dirname(__file__)
_filepath = _os.path.abspath(_os.path.join(_basepath, "package.json"))
with open(_filepath) as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")
__version__ = package["version"]

_current_path = _os.path.dirname(_os.path.abspath(__file__))

_this_module = _sys.modules[__name__]


_js_dist = [
    {
        "relative_package_path": "crystal_toolkit.min.js",
        "dev_package_path": "crystal_toolkit.dev.js",
        "namespace": package_name,
    }
]

_css_dist = []


for _component in __all__:
    setattr(locals()[_component], "_js_dist", _js_dist)
    setattr(locals()[_component], "_css_dist", _css_dist)

# pleasant hack to support MSONable objects in Dash callbacks natively
from monty.json import MSONable


def to_plotly_json(self):
    return self.as_dict()


MSONable.to_plotly_json = to_plotly_json

import warnings

warnings.warn(
    "Master branch is in undefined state. Please wait for first "
    "versioned release, at which point master branch will be protected."
)
