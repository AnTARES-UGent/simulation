# Contributing guide
## General
This repository is a team-effort, which means there are some guide-lines towards contributing to make sure everything goes smooth. When contributing, please follow the guide-lines wherever possible.

When writing Python code, always follow the PEP8 rules. Violations against those will be highlighted by most modern Python IDE's that use a linter. VSCode has an [extension](https://code.visualstudio.com/docs/python/linting), and Pycharm has that baked in. These PEP8 rules will ensure a readable and consistent codebase. 
If other languages are used, look if they have style-guides, and add one here after discussion with the team. Bash for example can use [shellcheck](https://www.shellcheck.net/).

Alongside following style-guides, also comment your code. Comments should explain the broad idea and the why of a piece of code. They serve as clarification for your future self and teammates who might need to revisit your code.


## Commit Messages
Commit messages must briefly explain what they add, while also not just stating what literally changed in the code. The message start with either 'feat: ', 'fix: ' or 'docs: ' to indicate what is changing.

Some examples:
- "docs: Updated README memberlist"
- "feat: Added error-handling for API-calls"
- "fix: Fixed Issue#12"


## Bugs
When encountering a bug that is present on the develop- or masterbranch, create an [Issue](https://github.com/AnTARES-UGent/simulation/issues) explaining the bug. This is not necessary when working on other branches, as those should be actively being worked on and tested. This way of working assures the rest of the team knows what's up.

When creating an Issue for a bug, begin its name with 'Bug: '.
In the description, you add a summary, steps to recreate and a screenshot/copy-paste of the bug happening (if applicable). 

## Branches
The main branch is for working code and working features.
It is locked from pushing anything to it directly.
Everything should first be commited/merged into a development-branch,
which then can get merged via a pull request into main.

When creating a new feature,
or fixing a bug requiring more than one commit, you should create a new branch with a fitting name.
A name would start with 'feature/' or 'bugfix/' and then the feature-name or bugfix (issue number):
- feature/new-parachute
- bugfix/#13-parachute-doesnt-deploy
- doc-update/add-workflow
 When the new feature is finished, or the bug is completely fixed and tested, you can merge into master and delete your branch. 


## Pull requests
Pull requests are the preferred way to merge two branches. They allow other people to see what you've changed, and comment on things that might need to change. When everyone is happy with the changes, the branch can be merged and the pull request closed. 

Currently, a pull request needs at least one approved review. 

When people have conflicting opinions about your feature or the way some things are done, go by the opinion of the majority. Feedback from others should never be neglected, and be taken into account before merging if the feedback directly addresses the new feature/bugfix. Before merging, make sure all feedback is addressed. The person opening the pull request is responsible for resolving all arising issues before mergin.

When merging a pull request, prefer to "Squash and merge". This will create a cleaner commit-history on the main branches so features/bugfixes can easily be reverted if necessary.


## Tests
New features and bugfixes should always be tested first inside a Docker environment. Here are the steps to do this:
- Very nice step 1
- Very nice step 2
hmmmm, needs some work
