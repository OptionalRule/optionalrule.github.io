# Overview

This is the source for a Jekyll based website for Optional Rule Games.

## Assets Used
Noting various assets I'm using for attribution and reference.
* Bootstrap 5 with JQuery for the base styles and scripts.
* [Jekyll](https://jekyllrb.com/) static site generator.
* [Parallax.js](https://pixelcog.github.io/parallax.js/)
* Favicons and header code generated from [realfavicongenerator.net]

## Other Setup Notes

Keeping a few notes as to the process as I found these split up between various resources or unclear.

### Development and Running locally.

For ease and portability, this is enabled to run in a docker container using BretFisher's docker 
setup.  To run the site locally just:
```
> docker-compose up -d
```
The site is configured to run at localhost:4000

To run the development site with drafts published run the following command.
```
> docker-compose exec jekyll bundle exec jekyll serve --drafts
```

### Website Build Folder

Github pages only offers me options for / (/'root') or /doc directories for the site source.  Jekyll defaults to _site for the subdir.  Either always build to /doc or use /_site normally for dev (and properly ignore it) and build to /doc to publish.

#### Build Command (local)
```
> jekyll build --incremental --destination docs/
```
#### Build Command (docker)

```
> docker run -v $(pwd):/site bretfisher/jekyll jekyll build --incremental --destination docs/ .
```
On windows PowerShell
```
> docker run -v ${PWD}:/site bretfisher/jekyll jekyll build --incremental --destination docs/ .
```
Via docker-compose
```
> docker-compose exec jekyll bundle exec jekyll build --incremental --destination docs/ .
```

#### Note on building from docker container

Attach to the docker container by finding the container ID and using
```
> docker exec -it <container id> bash
```

I've had some problems with the latest version of the Jekyll docker image and had to build from an attached terminal inside the running containers.  If this is the case I just attach to the terminal and run.
```
> bundle exec jekyll build --incremental --destination docs/
```

### Custom Domain

GitHub pages for the custom domain should be setup using both A Records and CNAME.  This is needed for GitHub Pages to create the cert to use for HTTPS.  Otherwise I'll get an error that the domain is configured correctly.  Note you can alternatively just setup a domain alias.

* In Github Pages enter the full domain name (with 'www') which will create a CNAME file in the website root.
* In the DNS config site create a CNAME entry for the www version of the site name. (i.e. www.optionalrule.com)
* In the DNS config site create A Records for the apex domain.