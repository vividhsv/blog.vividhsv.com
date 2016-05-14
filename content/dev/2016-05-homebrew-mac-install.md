Title: Installing Homebrew on Mac
Date: 2016-05-12 20:30
Modified: 2016-05-12 20:30
Category: Development
Tags: Homebrew
Slug: installing-homebrew-on-mac
Authors: Vividh Viswanatha

We all love the ease package managers like 'apt-get' in Ubuntu and 'yum' in centOS provide. Wouldn't it be great to have a similar package manager for MacOS too? Homebrew solves that problem for us. Homebrew, "The missing package manager for OS X" as they rightly advertise on their website.

### Installing prerequisites

Before we begin installing Homebrew, we will have to install the prerequisites, Command Line Tools for Xcode. Run the below command to install Command Line Tools for Xcode. If you have already installed Xcode you can skip this step.

To check if you have Command Line tools for Xcode installed. Open up Terminal app and run the below command.
```shell
$ xcode-select -p
```
If you see;
```shell
/Library/Developer/CommandLineTools
```
you already have Command Line Tools installed.

If not, install Command Line Tools for Xcode by running the following command
```shell
$ xcode-select --install
```
This should pop open an alert window requesting to confirm installing Command Line Tools. Click on "Install". Now wait for it to be downloaded and installed. Once done, you can verify Command Line Tools are installed by running the above verification  command.

### Installing Homebrew

Install Homebrew
```shell
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
As of today, when this is article was written command to install Homebrew was as above. Please verify or even better get the latest install script or command from [Homebrew](http://brew.sh/) site.

### Using Homebrew

To update Homebrew
```shell
$ brew update
```

To install a package, like "tree"
```shell
$ brew install tree
```

To Troubleshoot any issues with Homebrew
```shell
$ brew doctor
```

Get more information from man pages for Homebrew by running
```shell
$ man brew
```
or
```shell
$ brew --help
```

Isn't this great? I use brew to install Python, golang, nodejs, etc. Homebrew is a breeze in uninstalling packages as well and helps me keep my Macbook clean.
