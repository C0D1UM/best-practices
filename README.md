# CODIUM Best Practices

The recommendations in this document come from the collective experience of the team, and will evolve and grow over time with that experience.  None of them are set in stone.  However, if you decide to depart from them in a pull request, you will need to explain a good reason.

## Development Process

### Project

A project repo will be the place where all code, documentation and issue tracking will live.  Configuration (server addresses, database urls etc) and secrets (keys and passwords) should remain outside the repo.

- We aim to use the [cactus model](https://barro.github.io/2016/02/a-succesful-git-branching-model-considered-harmful/) of branching in git.  Production builds should be tagged with a version, to be able to easily deploy and rollback to a specific version in the event of a problem.

- There should be no commits made directly to the project repo.  Developers should work on their own fork and submit pull requests to the project repo to be vetted and merged by another team member.

- Whenever there is more than one developer on a project, developers should not merge their own pull requests.

- Pull requests should encapsulate a single fix or feature, and should contain only changes relevant to that fix/feature.

- Pull requests should not contain merge commits.

- Pull requests should not contain generated code.

- Commits should encapsulate an atomic change, a single step in the process of creating the fix or feature in the pull request.

- Code changes should be documented within the code[0].

- Bugfixes and new features should include tests[1].

#### Migrations

- Pull Requests should not contain migrations.  If schema changes are required, it should be indicated in the name of the PR or with a label.  Then, when the PR is reviewed and ready to merge, migrations should be added in a separate commit and merged immediately.

- Migrations files should not be deleted or changed once they are in the master branch. 

### Development Environment

- Use an IDE where possible.  Webstorm and PyCharm are excellent.

- If you must use a text editor, at least install a linter plugin for the language you are using.  Ensure the editor's settings for indentation match up with the code style guidelines below, or install an editorConfig plugin to do it automatically.

- You should be able to work on and preview the project without an internet connection.  This encourages an adequate level of decoupling between components, with the added bonus of being able to work without an internet connection.

### Teamwork

- We practice agile development and start each day with a short SCRUM meeting where we talk about our successes and problems from the previous day, and our tasks for the day ahead.

- At the beginning of each week, we will review our goals and assign our tasks for the week's sprint.

#### Code Review

- Code review is an key part of the development process at CODIUM.  It gives a chance for developers to view each other's code and share knowledge from all parts of the project and even other projects.  All pull requests should be reviewed by a peer before being merged.

- Requests for review should be answered promptly, usually within an hour and within a day at the most.  If you are asked to review a pull request and won't be able to review it in time you should assign it to someone else for review.

- Ensure that the pull request meets the standards of the existing code in the repo and follows the best practices listed here.  Ask for clarification on any changes that you don't understand, maybe the code could be simpler or maybe you could learn something new in the process.  Once you are satisfied that the code is up to standard, you can merge the pull request.

#### Concentration

- Developers are encouraged to ask and answer questions.  Sometimes however you need to concentrate on a difficult problem and would like to not be disturbed.  If a developer is wearing headphones or has gone to another room to work, try not to interrupt them, send them a slack message that they can answer in their own time when they have finished their task.

### Testing

- Every function, class and method you write should have unit tests.

- When submitting a bugfix pull request, add a test that fails before the patch is applied.  Use `git cherry-pick` if necessary to rearrange your commits so the test comes first.

- The project should have some basic end-to-end tests as a failsafe to ensure sanity.  E.g. a rest API should have a test that hits every endpoint with basic GET and POST requests.  An angular SPA should have a test that at least bootstraps the app in PhantomJS.

## Code Style

Having a style guide will help keep code clear and readable even when it is written and amended by many people over time.  By following these best practices, we agree to think of the long term maintainability of the software we write.

Some of the items covered by this guide, for example indentation, are purely a matter of convention/opinion.  In these cases it is best to just pick one way and stick with it, because a team can't have two conventions at once.  Kind of like driving on the left side of the road.

- All files should use unix line endings (\n, not \r\n)

- All files should end in a newline

- Javascript, HTML (and Jade, HAML etc), Css (and Sass, Scss, Stylus etc) should be indented with two spaces

- Python should be indented with four spaces.

- All python code should be PEP8 compliant (https://www.python.org/dev/peps/pep-0008/)

- All angular code should follow John Papa's style guide (https://github.com/johnpapa/angular-styleguide)

### Documentation

- Use standard docstrings in Python and Javascript for all classes and functions.

- Be unapologetically simple, and apologetically clever: try to find a solution to the problem that is so straightforward it doesn't require any explanation.  When you do need to use a clever solution to a problem, make sure to thoroughly explain it in a comment.

- Regexes are practically obfuscated by design, therefore all regexes must be accompanied by a comment explaining what they do.

### Logging

- In python, use the logging module.  No `print` statements should ever make it into project repo code.

- Similarly in angular, use the $log service rather than console.log. ** TODO Find out best practice for logging in node.

- If you annotate your logging calls so that it's clear where they come from and what they are reporting, leave them in the code.  If you found them useful once, they will probably be useful again one day.

## Deployment

There are many ways to deploy a project, and to enable innovation we don't proscribe any particular one to every project.  We share ansible playbooks between projects for common django and angular SPA deployments, you are free to use them, build on them or experiment with other solutions.  However, all deployment setups should share the following features:

- Complete a deploy with one click, or at the command line in 3 words or less.

###### Good:
```bash
grunt deploy
```

```bash
./deploy.sh
```

###### Not good:
```
...
Step 22: Type in username and password for host server.
Step 23: go to app folder and copy assets directory to ftpzilla.
...
```

- Deploy scripts should be idempotent: running it twice should have no effect the second time.

- As far as is possible, the deploy script should be fast.  Avoid running unnecessary slow tasks such as transferring large files over the internet if the files are unchanged.

- There should be clear documentation for deployment in the README at the base of the repo.  It should be clear enough that a new developer can set up a development environment and be able to deploy to a staging server without assistance within a couple of hours.

- Major and minor releases, new features, and any significant patches should only be deployed to production on a Monday.  Hotfixes can be deployed Tuesday-Thursday but only emergency fixes should be deployed on a Friday.

## Interview Problems
[link](interview.md)
