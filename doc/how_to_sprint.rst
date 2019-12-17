===============================================
How to sprint on open source projects in Python
===============================================

This tutorial was given at the SciPy conference in 2016-2018 to teach people
how to contribute to open source projects using the ``git`` command line tool
and Github.

Outline
=======

  #. What you need to get comfortable with
  #. What you need
  #. What you can contribute
  #. How to create development environments
  #. How to contribute code
  #. How to find my sprint and get setup
  #. What if I need more help?


Contributing: what you need to get comfortable with
====================================================

  * Working at the command line.
  * Issue workflow on Github.
  * Making changes and recording them using `git`.
  * *Good coding practices (testing frameworks, styling tools, restructured
    text and documentation generators).
  * *Debuggers and grep-type tools to find your way through new source code.

Do you need to be here? No if you are already comfortable with the first 3
items!


What you can contribute
=======================

List of ideas, requiring more and more technical knowledge of the package in
question:

  * Documentation improvements
  * Tutorial review/improvements
  * Example review
  * Example creation
  * Add unit tests (driven by test coverage analysis)
  * Fix a bug
  * Tutorial creation
  * Implement new features
  * Review other people's PR
  * Close old issues not relevant anymore
  * Triage issues

Three pieces of advice:

  * Your own needs are the best driver for open source contributions.
  * If you don't know what to do, look for issues tagged `easy`.
  * If you don't know what to do, ask maintainers what would be the 
    most helpful.

Next, see your sprint lead for suggestions.

Contributing: what tools you need
=================================

  * A python aware code editor. There are many free options: Pycharm,
    Canopy, Spyder, emacs, vi(m), ....
  * An account on `github.com`.
  * The `git` tool. OSX: Install Xcode command line tools.
    Windows: https://git-scm.com/download/. Linux: use your package manager
    (`yum`, `apt-get`, ...).
  * A tool to quickly create and manage light development environments.
  * [OPTIONAL] A C/C++ compiler (depending on the project you want to
    contribute to), or a Fortran compiler.
  * [OPTIONAL] Several Virtual Machines running different Operating Systems to
    test your changes on multiple platforms.

How to create development environments?
=======================================

Two most reliable (free) tools to provision development environments I know:

  * Anaconda's ``miniconda``
  * Enthought's ``EDM``

+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
|                        |                                      EDM                               |                   Miniconda                                        |
+========================+========================================================================+====================================================================+
| 1. Download            | `enthought.com/products/edm <http://www.enthought.com/products/edm/>`_ | `docs.conda.io <https://docs.conda.io/en/latest/miniconda.html>`_  |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
| 2. Create a new env    | edm environments create --version 3.6 devenv                           | conda create -n devenv python=3.6                                  |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
|                        | edm env import NEW_ENV -f bundled_env.json (1)                         |                                                                    |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
| 3. Activate new envir. | edm shell -e devenv                                                    | source activate devenv                                             |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
| 4. Add dependencies    | edm install "numpy==1.11.3-2" scipy                                    | conda install numpy=1.11 scipy                                     |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
|                        |                                                                        | conda install --file requirements.txt                              |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+
| 5. Install package     | pip install -e .                                                       | pip install -e .                                                   |
+------------------------+------------------------------------------------------------------------+--------------------------------------------------------------------+

(1) This command creates a new environment ``NEW_ENV`` from a full environment
description contained in the json file (bundle). The json file can be created
from an existing environment replacing ``import`` by ``export``.

More help? ``edm -h`` or ``conda -h`` commands.

The project contains C extensions?
----------------------------------
Some projects require a C/C++ compiler because contain C/C++ code or Cython
code which needs to get compiled to be tested/distributed.

  * On OSX and linux, you can typically use the native compiled (gcc). Use
    ``yum``/``apt-get`` or OSX command line tools to install it if needed.
  * On Windows, ... it is a mess. For Python2.7, you need to use VS2008. For
    Python 3.4, you need to use VS 2010. For Python 3.5 and 3.6, you need to
    use VS 2015. See https://pandas.pydata.org/pandas-docs/stable/contributing.html
    for links to free installers.


How to contribute code?
=======================

The typical workflows
---------------------

  #. Identify a work item you want to contribute. **Think small**.

  #. Create a ticket for your work item **if it doesn't already exist**.

  #. Assign the ticket you are working on to yourself so others know it is
     work in progress.

  #. Go to the package's Github repository. Fork it into your account where you
     have push rights. If you are contributing to a package you have push
     rights for, you might skip this step. Discuss with your project
     lead/repository owner.

  #. Clone your fork locally (or the package's repository directly if you have
     push rights and are allowed to push branches to it directly)::

        git clone https://github.com/<USER NAME>/sprint_tutorial

     Whichever repository you clone will represent a "remote" and be called
     "origin". A remote is a repository you can pull from. Git allows multiple
     remotes to be defined on your local checked out code, in case you want to
     pull and push to/from different locations.

  #. Create a new development environment (if not already done). Build the
     project into your dev environment. Run the test suite.

  #. Branch off to a new branch for your work item::

        git branch fix/bug_name
        git checkout fix/bug_name

     or in a single step::

        git checkout -b fix/bug_name

  #. Make sure you are in the expected branch::

        git branch

  #. Do work. **STAY FOCUSED** and only address the work item you selected.
     Otherwise review will be hard(er), therefore delayed, and your PR is
     likely to be rejected.

  #. Review what has been done with::

        git status
        git diff file1.py

  #. When a set of changes represents a valuable step toward your goal,
     commit::

        git commit -m "TEST: add unit test to show the bug" file1.py file2.py ...

     Or make a more complete commit message using an editor::

        git commit file1.py file2.py ...

     and write the commit message in the editor ``git`` uses.

  #. Don't forget to include or update unit tests to make sure your work
     doesn't break in the future. Remember, your most important contribution
     might be your tests! If some code isn't unit-tested, it is either already
     broken, and it will be (and no one will know about it)! And run the entire
     test suite to make sure your contribution didn't break anything.

  #. Once you have done everything you want, push your branch to Github::

        git push --set-upstream origin fix/bug_name

     or simply::

        git push

  #. Go to Github to make a `Pull Request` (PR) with your work. You should see
     your branch available for a PR in both your repo and in the upstream
     repository that you forked. Select the branch you would like to pull your
     branch into, and add a complete description.

  #. Check for the result of Continuous Integration (CI).

  #. Discuss your work with your reviewer. Implement fixes and improvements,
     and push again to your branch. Your PR will update automatically.

  #. If the original package's master branch gets updated between your cloning
     and the time your PR is merged, you may be asked to merge master changes
     into your branch or rebase your branch onto the new one, and resolve any
     conflict. To that effect, you need to define another remote you want to
     pull changes from, assuming you have forked the repo. In that case, the
     common approach is to define the official package repo as a new remote
     called "upstream"::

        git remote add upstream git@github.com:jonathanrocher/sprint_tutorial

     If the project you are contributing to is ok with merges of master, it is
     easier to do the following::

        git checkout master
        git pull upstream master
        git checkout fix/bug_name
        git merge master
        git push

     If your project requires to rebase::

        git fetch upstream
        git rebase upstream/master

     Note that the commit hash of your current state will be changed, so if you
     have pushed before the rebase, your state will need to be "force-pushed"::

        git push --force

  #. Once the PR has been approved, it will be merged in the upstream project
     by someone who has push rights.

  #. After merge, there are 3 typical cleaning steps: delete the branch on the
     remote repositories (in Github), update master locally from upstream,
     update master in your own fork and delete the work branch locally.::

        git checkout master
        git pull upstream master
        git push origin master
        git branch -d fix/bug_name

  #. GOTO 1.


Check-list before making a PR and requesting review.
----------------------------------------------------

That check-list depends on each project, but typically, you should think of the
following:

  * Tests pass on your machine (try as many OSs as possible).
  * Code conforms to pylint/flake8/pep8/styling.
  * All new functions and classes have docstrings.
  * Your branch is sync-ed with current master.
  * CI tests are all green.
  * Documentation is updated (if needed).
  * Changelog is updated (if needed).


When things go wrong with git
-----------------------------
Git is an incredibly powerful tool to manage code, but it is pretty easy to
mess up. It is ok, everyone messes up with ``git``. The good news is, you can
(almost) always recover from a mess up. If you have an issue, pause, think,
google, find a git guru!

Here are a few tricks to get out of common situations:

  * You have made a mess and want to erase all un-committed code (ALL FILES)::

        git reset --hard HEAD

  * You have made a mess in only 1 file::

        git checkout HEAD -- filename

  * You have committed too quickly, and want to include more files, or redo your
    commit message::

        git reset --soft HEAD^

  * You don't like where you are going and decide you want to go back in time,
    to a precise commit, look for the commit hash with::

        git log

    and then reset to that point::

        git reset --hard <HASH>

    You can also go back in time without loosing your work since then, just to
    check things out::

        git checkout <HASH>

  * You have pulled master or a collaborator's work and now have a conflict?
    Open the conflicted file in an editor, and merge lines manually. Then::

        git add filename

    to mark it as resolved. Your branch is back to being ready to be committed.

  * You would like to pause your work in progress without committing to do
    something else or switch to another branch that has conflicts::

        git stash

    When you are done, and want your changes back::

        git stash pop

    Note that you can stash multiple times. States are stored on a stack
    (FILO).


What's next?
============

Look for your sprint in http://bit.ly/sprints2018 . Get yourself setup as much
as possible using information there. Then, head down and connect with your
sprint lead.


Where to get more help?
=======================

  * Your sprint leader
  * The project's contributing guidelines (see column H of http://bit.ly/sprints2018 )
  * The project's `travis.yml` file.
  * Sprint help on slack: `sprints` channel at http://scipy2018.slack.com
  * Contribution workflow: https://pandas.pydata.org/pandas-docs/stable/contributing.html
  * Numpy testing guidelines: https://github.com/numpy/numpy/blob/master/doc/TESTS.rst.txt
  * Numpy docstring guidelines: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
  * Restructured text primer: http://docutils.sourceforge.net/docs/user/rst/quickref.html
