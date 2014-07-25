site2ikiwiki
============

A general simple html or wiki converter to markdown and so to ikiwiki (http://ikiwiki.info/).

Initially, designed to migrate/import PmWiki and pure HTML websites into ikiwiki.


Usage
=====

## Configuration

* Create a configuration file:

```
cd /path/to/site2ikiwiki
cp default.json yoursite.json

```

Example of config file (json format)

```
{
 "sitename": "yoursite",
 "source_dir": "/path/to/your-old-site",
 "source_address": "http://localhost/your-old-site",
 "source_type": "pmwiki",
 "ikiwiki_source": "/path/to/mdwn-files-of-new-site",
 "ikiwiki_dest": "/path/to/your-new-site",
 "ikiwiki_address": "http://localhost/your-new-site",
 "ikiwiki": "True",
 "ikiwiki_version_control": "git"
}
```

- **sitename**: put your site name (no spaces)
- **source_dir**: put here the source files of your page/wiki
- **source_address**: put here the web address (http) of your page/wiki
- **source_type**: pmwiki|html|...
- **ikiwiki_source**: directory to generate the markdown of your new ikiwiki site
- **ikiwiki_dest**: directory for ikiwiki parse html
- **ikiwiki_address**: web directory of your new ikiwiki site
- **ikiwiki**: True|False   -> default is true, but if you only want to generate markdown, fill it with "False"
- **ikiwiki_version_control**: default is GIT, could be others (check it at http://ikiwiki.info/ikiwiki-makerepo/) 

IMPORTANT: because of Json format, every values must me put "inside commas". Otherwise, the config load will fail.


## Running the import

* On a terminal, run:
```
$ python convert.py yoursite.json
```