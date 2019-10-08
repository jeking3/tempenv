Developer Overview
==================

1. If you are a first-time contributor:

   * Go to `https://github.com/jeking3/tempenv
     <https://github.com/jeking3/tempenv>`_ and click the
     "fork" button to create your own copy of the project.

   * Clone the project to your local computer::

      git clone git@github.com:your-username/tempenv.git

   * Add the upstream repository::

      git remote add upstream git@github.com:jeking3/tempenv.git

   * Now, you have remote repositories named:

      - ``upstream``, which refers to the ``jeking3`` repository
      - ``origin``, which refers to your personal fork

2. Install development prerequisites:

   * The required local packages for development are listed in the
     file ``requirements/dev.txt``.  This command will install them
     locally::

      make prerequisites

3. Develop your contribution:

   * Pull the latest changes from upstream::

      git checkout master
      git pull upstream master

   * Create a branch for the feature you want to work on. Since the
     branch name will appear in the merge message, use a sensible name
     such as 'issue-123'::

      git checkout -b issue-123

   * Commit locally as you progress (``git add`` and ``git commit``)

4. To submit your contribution:

   * Push your changes back to your fork on GitHub::

      git push origin issue-123

   * Go to GitHub. The new branch will show up with a green Pull Request
     button---click it.

   * If this pull request fixes an issue, also add to the end of pull request
     description, "This fixes #100" where 100 is the issue number.

5. Review process:

    * Reviewers (the other developers and interested community members) will
      write inline and/or general comments on your Pull Request (PR) to help
      you improve its implementation, documentation, and style.  Every single
      developer working on the project has their code reviewed, and we've come
      to see it as friendly conversation from which we all learn and the
      overall code quality benefits.  Therefore, please don't let the review
      discourage you from contributing: its only aim is to improve the quality
      of project, not to criticize (we are, after all, very grateful for the
      time you're donating!).

    * To update your pull request, make your changes on your local repository
      and commit. As soon as those changes are pushed up (to the same branch as
      before) the pull request will update automatically.

    * `Travis-CI <https://travis-ci.org/>`_, a continuous integration service,
      is triggered after each Pull Request update to build the code and run unit
      tests of your branch. The Travis tests must pass before your PR can be merged.
      If Travis fails, you can find out why by clicking on the "failed" icon (red
      cross) and inspecting the build and test log.

    * `AppVeyor <http://ci.appveyor.com>`_, is another continuous integration
      service, which we use.  You will also need to make sure that the AppVeyor
      tests pass.


Divergence between ``upstream master`` and your feature branch
--------------------------------------------------------------

Never merge the main branch into yours. If GitHub indicates that the
branch of your Pull Request can no longer be merged automatically, rebase
onto master::

   git checkout master
   git pull upstream master
   git checkout bugfix-for-issue-123
   git rebase master

If any conflicts occur, fix the according files and continue::

   git add conflict-file1 conflict-file2
   git rebase --continue

However, you should only rebase your own branches and must generally not
rebase any branch which you collaborate on with someone else.

Finally, you must push your rebased branch::

   git push --force origin bugfix-for-issue-123

(If you are curious, here's a further discussion on the
`dangers of rebasing <http://tinyurl.com/lll385>`_.
Also see this `LWN article <http://tinyurl.com/nqcbkj>`_.)

Guidelines
----------

* All code must have tests.
* All code must be documented.
* All changes are reviewed.

Stylistic Guidelines
--------------------

testenv uses the ``black`` auto-formatting project to maintain strict
code style.  This is enforced when you try to commit locally.

Bugs
----

Please `report bugs on GitHub <https://github.com/jeking3/tempenv/issues>`_.

