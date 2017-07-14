===============================================
How to sprint on open source projects in Python
===============================================


Outline
=======

  #. What you need?
  #. What you need to get comfortable with?
  #. What you can contribute?
  #. How to create development environments?
  #. How to contribute code?
  #. How to find my sprint and get setup?
  #. Where to get more help?


What you need?
==============

  * A python aware code editor. There are many free options: Pycharm, Canopy,
    Spyder, emacs, vi(m), ...
  * An account on `github.com`
  * The `git` tool. OSX: Install Xcode command line tools.
    Windows: https://git-scm.com/download/. Linux: use your package manager
    (`yum`, `apt-get`).
  * A tool to quickly create and manager light development environments
  * [OPTIONAL] A C/C++ compiler (depending on the project you want to
    contribute to), or a Fortran compiler.
  * [OPTIONAL] Several Virtual Machines running different Operating Systems to
     test you changes on multiple platforms.


What you need to get comfortable with?
======================================

  * Working at the command line
  * `git`
  * Good coding practices (testing frameworks, styling tools, restructured text
    and documentation generators).
  * Debuggers and grep-type tools to find your way through new source code.


What you can contribute?
========================

List of ideas, requiring more and more technical knowledge of the package in
question:

  * Documentation improvements
  * Tutorial review
  * Example review
  * Example creation
  * Existing ticket review
  * Add unit tests
  * Bug fix tickets
  * Tutorial creation
  * New features tickets
  * Other PR review
  * Triage of issues

Two advice:

  * Your own needs are the best driver for open source contributions
  * If you don't know where to start, look for issues tagged `easy`
  * Ask current maintainers what would be the most helpful.


How to create development environments?
=======================================

Two most reliable (free) tools to provision development environments I know:

  * Enthought's ``EDM``
  * Continuum Analytics' ``miniconda``

+========================+===============================================+===================================+
|                        |                     EDM                       |         Miniconda                 |
+========================+===============================================+===================================+
| 1. Download            | enthought.com/products/edm                    | conda.io/miniconda                |
+------------------------+-----------------------------------------------+-----------------------------------+
| 2. Create a new env    | edm environments create --version 3.6 devenv  | conda create -n devenv python=3.6 |
+------------------------+-----------------------------------------------+-----------------------------------+
| 3. Activate new envir. | edm shell -e devenv                           | source activate devenv            |
+------------------------+-----------------------------------------------+-----------------------------------+
| 4. Add dependencies    | edm install "numpy==1.11.3-2" scipy           | conda install numpy=1.11 scipy    |
+------------------------+-----------------------------------------------+-----------------------------------+
| 5. dev env location    | ~/.edm/envs/devenv                            | ~/miniconda/envs/devenv           |
+========================+===============================================+===================================+

More help? ``edm -h`` or ``conda -h`` commands.


How to contribute code?
=======================


How to find my sprint and get setup?
====================================




Where to get more help?
=======================

  * Sprint help on slack: `sprints` channel at http://scipy2017.slack.com
