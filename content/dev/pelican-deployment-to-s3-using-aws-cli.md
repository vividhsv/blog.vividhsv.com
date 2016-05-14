Title: Pelican Deployment to S3 using AWS-CLI
Date: 2016-05-14 13:30
Modified: 2016-05-14 13:30
Category: Development
Tags: Pelican,AWS,S3
Slug: pelican-deployment-to-s3-using-aws-cli
Authors: Vividh Viswanatha

This blog is built using [Pelican](http://blog.getpelican.com/) an amazing static site generator written in Python. I host this blog site on AWS S3 which makes it quite cheap to host a static site. Pelican  also makes it easy to push to AWS S3 with the help of [s3cmd](http://s3tools.org/s3cmd). However, s3cmd doesn't support Python 3.x.

Here was the problem, I had Pelican running on Python 3.5 and s3cmd doesn't support Python 3.x.  I could have fallen back to python 2.x to solve the problem but there was AWS CLI which supports Python 3.5 to the rescue.

All it requires is to install AWS CLI and make sure aws access keys are made available to it, for more information please check out [AWS CLI documentation](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html).
```shell
pip install awscli
```
Next, edit Makefile to change s3_upload task to use AWS CLI. Around line 114 in Makefile comment out line 115 under 's3_upload: publish' and add the following line
```shell
aws s3 sync $(OUTPUTDIR)/ s3://$(S3_BUCKET) --acl public-read --delete
```

Thats it!. Now you can keep Pelican with Python 3.x and still upload to s3 using AWS CLI. Run the below Make task to upload to s3.
```shell
make s3_upload
```
