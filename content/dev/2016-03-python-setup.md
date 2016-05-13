Title: Python Environment setup under 10 minutes on Mac
Date: 2016-03-01 21:40
Modified: 2016-03-01 21:40
Category: Development
Tags: Python, Virtualenv, Virtualenvwrapper, Homebrew
Slug: python-setup-under-5-minutes-on-mac
Authors: Vividh Viswanatha
Summary: Short version for index and feeds
Status: draft

If you are new to Python development or if you got a shiny new Macbook like me, you might be wanting to setup Python. We all know it is not a good idea to use default Python packaged with your Mac. If you were not aware, it is a bad practice due to the following reasons.

Default system python might be used by other OS packages or applications, which might have hard dependence on the python version. Hence you will not be able to easily upgrade or downgrade python depending on your project needs. You will also have to compile and install python and if things go wrong you might end up with a corrupt Python. Alternatively, you could also download Python installer from python.org site.However handling different versions of Python or Python packages will not be possible.

When you have to deal with such problems
http://33.media.tumblr.com/ec225e66f479de8146c28993f12f20a6/tumblr_inline_o1hodwTFOf1raprkq_500.gif

Ok now that you have been informed better lets move on to setting up new Python. There are two ways you could do this one the hard way and the other easy way. Hard way is where you will compile source and create new Python binary location. I will not be going through this method in this post. Easy way, as it implies is not more then three easy steps to have everything setup and ready.

Check where is the default Python binary at
```shell
$ which python
```
This should return /usr/bin/python

Install Homebrew
```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
Update Homebrew
```shell
$ brew update
```
Install Python 2.x
    brew install python
This will install latest Python under Python 2.x version.

Install Python 3.x
    brew install python3
This will install latest Python under Python 3.x version.

Check where is the new Python binary now for both Python2.x and Python3.x
    which python
This should return /usr/local/bin/python
    which python3
This should return /usr/local/bin/python3

Now you have both new Python2 and Python3 installed. However, we still have one issue.We cannot switch between different Python versions when ever required depending on the project and will not be able to install and maintain different versions of python packages. Imagine you have an application that needs version 1 of LibFoo, but another application requires version 2. How can you use both these applications? (Taken from https://virtualenv.readthedocs.org/en/latest/, no better way to explain this)

Virtualenv to the rescue. Virtualenv is a tool to create isolated Python environments.

Install Virtualenv
    pip install virtualenv
This should install virtualenv package to help install new virtual Python binary environments.

Now to create new virtual Python environment, Lets run the following commands

Create an directory to install virtual Python Binaries
mkdir -p ~/.virtualenv
cd .virtualenv

Create virtualenv
    virtualenv my_python

Switch to my_python
    source ~/.virtualenv/bin/activate

Check where is the new Python binary now for both Python2.x and Python3.x
    which python
This is should show ~/.virtualenvs/my_python/bin/python

This should suffice most of our needs, however we could further ease our efforts to create Python virtualenvs and switching back and forth between different virtualenvs.

Virtualenvwrapper to the rescue. virtualenvwrapper is a set of extensions to virtualenv. This extension help creating, deleting and managing your virtualenvs.

Install virtualenvwrapper
    pip install virtualenvwrapper
