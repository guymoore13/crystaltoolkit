.. image:: images/logo.png
  :align: center
  :alt: Crystal Toolkit Logo
  :target: https://materialsproject.org/#apps/xtaltoolkit

============
Introduction
============

Crystal Toolkit is a web app framework from the `Materials Project <https://materialsproject.org>`_
allowing Python developers to easily make an interactive web app to display materials science information.
As a showcase of the framework's capabilities, the Crystal Toolkit app allows you to import, view, analyze and
transform crystal structures and molecules.

.. warning::
  If you use Crystal Toolkit to power your own web apps,
  you are required to kindly ask your users to cite the Crystal Toolkit
  paper. Likewise, if you use a Crystal Toolkit figure or analysis in
  your own paper, please cite, thank you! Citations help us justify
  further work on new features and maintenance of the code.

Crystal Toolkit Demonstration App
---------------------------------

You can visit the current Crystal Toolkit web app `here. <https://materialsproject.org/#apps/xtaltoolkit>`_


Crystal Toolkit Web Framework
-----------------------------

Crystal Toolkit is designed as a modular, object-orientated suite of UI components
built upon the `Dash framework by Plotly <https://dash.plot.ly>`_. The main Crystal Toolkit web app is just
one example of using these components.

...

Installation
------------

You can ``pip install crystal-toolkit``.

For Jupyter integration, please see the `additional installation steps <jupyter>`_.


Running the App Locally
-----------------------

If the web app is offline or undergoing maintenance, you can also run the
web app locally using `Docker <https://www.docker.com>`_. After you've
installed Docker, run the following:

::

    docker container run -p 8000:8000 -e PMG_MAPI_KEY=YOUR_API_KEY_HERE materialsproject/crystal_toolkit

The app should then be available at `<http://localhost:8000>`_.

Make sure to set your ``PMG_MAPI_KEY`` appropriately.
If you need a Materials Project API key, please get a free account on
`Materials Project <https://materialsproject.org>`_ and access your dashboard.

Development Team
----------------

The `Crystal Toolkit Development Team <https://github.com/materialsproject/crystaltoolkit/graphs/contributors>`_ includes:

* `Matthew Horton <https://github.com/mkhorton>`_, project lead

Contributors

* `François Chabbey <https://github.com/chabb>`_ for React components
* `Jimmy Shen <https://github.com/jmmshn>`_ contributed pythreejs support, surface plotting, initial arrows/axes support, and various bug fixes
* `Joey Montoya <https://github.com/JosephMontoya-TRI>`_ contributed Pourbaix component
* `Shyam Dwaraknath <https://github.com/shyamd>`_ for planned contributions for ellipsoid support and architectural design
* `Donny Winston <https://github.com/dwinston>`_, assisted by `Tyler Huntington <https://github.com/tylerhuntington>`_, for helping embed Crystal Toolkit in a Django app
* `Matt McDermott <https://github.com/mattmcdermott>`_ contributed phase diagram, X-ray Diffraction, X-ray Absorption Spectrum components
* `Jason Munro <https://github.com/munrojm>`_ contributed band structure component
* `Stephen Weitzner <https://github.com/sweitzner>`_ contributed POV-Ray integration (in progress)
* `Richard Tran <https://github.com/richardtran415>`_ for contributing plotly-powered Wulff shapes to pymatgen, which Crystal Toolkit uses
* `Guy Moore <https://github.com/guymoore13>`_ for contributing magnetic moment visualization


New contributors are welcome, please see our `Code of Conduct. <https://github.com/materialsproject/crystaltoolkit/blob/master/code-of-conduct.md>`_
