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

### Website Build Folder

Github pages only offers me options for / (/'root') or /doc directories for the site source.  Jekyll defaults to _site for the subdir.  Either always build to /doc or use /_site normally for dev (and properly ignore it) and build to /doc to publish.

### Custom Domain

GitHub pages for the custom domain should be setup using both A Records and CNAME.  This is needed for GitHub Pages to create the cert to use for HTTPS.  Otherwise I'll get an error that the domain is configured correctly.  Note you can alternatively just setup a domain alias.

* In Github Pages enter the full domain name (with 'www') which will create a CNAME file in the website root.
* In the DNS config site create a CNAME entry for the www version of the site name. (i.e. www.optionalrule.com)
* In the DNS config site create A Records for the apex domain.