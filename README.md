# yoavram/pyandoc README

This a fork of the original [pyandoc](https://github.com/kennethreitz/pyandoc) project by [kennethreitz](https://github.com/kennethreitz).

The original project statement is: *Pyandoc: a simple Pandoc wrapper for Python*.

## Citations in Markdown

I wanted to use *Pandoc* for parsing *Markdown* files with *citations*.
Pandoc supports that by giving a `--bibliography=FILE` command-line argument with a bibliography file (like `.bib`).
See the [Pandoc documentation](http://johnmacfarlane.net/pandoc/README.html#citations) for more details on that.

But *pyandoc* did not support that. So I changed it.

  - Added and *add_argument* method to the *Document* class where you can give any argument listed in the *Pandoc* documentation.
  For example, want a Table of Contents? Do *add_argument("toc")*. 
  - Added an *bib(bibfile)* method. This method will check that the file given exists and will pass it to the arguments with the *bibliography=* prefix.
  - Same for *csl(cslfile)* for specifing an *CSL* file.

## PDF and EPUB output

I wanted to output PDF files with Pandoc, but *pyandoc* outputs to the stdout, 
and PDFs are generated in Pandoc using LaTeX and therefore must be output to file.
So I wrote a new method in *pyandoc.Document* called *to_file*. 
The method accepts an output filename (with an extention that Pandoc knows, such as *pdf* or *epub*).
I tested it with PDF and EPUB but it should work for other formats as well. The method works with the
*bib* and all the other stuff mentioned above.

## Pandoc executable path

The original project had the path to the *pandoc* executable hardcoded, and you were supposed to change it after import.
But that didn't work for me (got an error - see [issue](https://github.com/kennethreitz/pyandoc/issues/5)).
So I changed the hardcoded path, it is in the file *core.py* at the top. 
It is now simply *pandoc* so you can either change it via *pyandoc.PANDOC_PATH* or just
put *pandoc* in your path. This solution should work for both Windows and Linux users.


## Other details

I tested this on Windows 7 64-bit with *Pandoc* 1.9.4.2 (running *citeproc-hs* 0.3.4).

I'm using *pyandoc* as an alternative HTML renderer for [Flask-FlatPages](http://packages.python.org/Flask-FlatPages/#flask_flatpages) 
to render blog posts written in *Markdown* and containing academic citations - see the project [here](https://github.com/yoavram/yoavram.github.com/tree/source) and the module that uses *pyandoc* to render HTML [here](https://github.com/yoavram/yoavram.github.com/blob/source/renderers.py).

For installation and usage please see the [original project](https://github.com/kennethreitz/pyandoc),
the only differences are the extra methods the *Document* class has.
