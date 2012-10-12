# yoavram/pyandoc README

This a fork of the original [pyandoc](https://github.com/kennethreitz/pyandoc) project by [kennethreitz](https://github.com/kennethreitz).

The original project statement is: *Pyandoc: a simple Pandoc wrapper for Python*.

## Changes

### Big

I wanted to use *Pandoc* for parsing *Markdown* files with *citations*.
Pandoc supports that by giving a *--bibliography=FILE* command-line argument with a bibliography file (like *.bib*).
See the [Pandoc documentation](http://johnmacfarlane.net/pandoc/README.html#citations) for more details on that.

Byt *pyandoc* did not support that. So I changed it.

  - Added and *add_argument* method to the *Document* class where you can give any argument listed in the *Pandoc* documentation.
  For example, want a Table of Contents? Do *add_argument("toc")*. 
  - Added an *bib(bibfile)* method. This method will check that the file given exists and will pass it to the arguments with the *bibliography=* prefix.
  - Same for *csl(cslfile)* for specifing an *CSL* file.

### Small

The original project had the path to the *pandoc* executable hardcoded, and you were supposed to change it after import.
But that didn't work for me (got an error - see [issue](https://github.com/kennethreitz/pyandoc/issues/5)).
So I changed the hardcoded path, it is in the file *core.py* at the top.


## Other details

I tested this on Windows 7 64-bit with *Pandoc* 1.9.4.2 (running *citeproc-hs* 0.3.4).

I'm using it as an alternative HTML renderer for [Flask-FlatPages](http://packages.python.org/Flask-FlatPages/#flask_flatpages) 
to render blog posts written in *Markdown* and containing academic citations - see the project [here](https://bitbucket.org/yoavram/msb).

For installation and usage please see the [original project](https://github.com/kennethreitz/pyandoc),
the only differences are the extra methods the *Document* class has.
