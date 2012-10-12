import subprocess
from os.path import exists

PANDOC_PATH = r'C:\Program Files (x86)\Pandoc\bin\pandoc.exe'

class Document(object):
	"""A formatted document."""
	
	INPUT_FORMATS = (
		'native', 'markdown', 'markdown+lhs', 'rst', 
		'rst+lhs', 'html', 'latex', 'latex+lhs'
	)
	
	OUTPUT_FORMATS = (
		'native', 'html', 'html+lhs', 's5', 'slidy', 
		'docbook', 'opendocument', 'odt', 'epub', 
		'latex', 'latex+lhs', 'context', 'texinfo', 
		'man', 'markdown', 'markdown+lhs', 'plain', 
		'rst', 'rst+lhs', 'mediawiki', 'rtf'
	)

	# TODO: Add odt, epub formats (requires file access, not stdout)
	
	def __init__(self):
		self._content = None
		self._format = None
		self._register_formats()

        def bib(self, bibfile):
                if not exists(bibfile):
                        raise IOError("Bib file not found: "+bibfile)
                self.bibfile = bibfile

        def csl(self, cslfile):
                if not exists(cslfile):
                        raise IOError("Bib file not found: "+cslfile)
		self.cslfile = cslfile
		
	@classmethod
	def _register_formats(cls):
		"""Adds format properties."""
		for fmt in cls.OUTPUT_FORMATS:
			clean_fmt = fmt.replace('+', '_')
			setattr(cls, clean_fmt, property(
				(lambda x, fmt=fmt: cls._output(x, fmt)), # fget
				(lambda x, y, fmt=fmt: cls._input(x, y, fmt)))) # fset
	
	def _input(self, value, format=None):
		# format = format.replace('_', '+')
		self._content = value
		self._format = format
	
	def _output(self, format):
                subprocess_arguments = [PANDOC_PATH, '--from=%s' % self._format, '--to=%s' % format]
                
                if hasattr(self, "bibfile"):                       
                        subprocess_arguments.append('--bibliography=%s' % self.bibfile)
                if hasattr(self, "cslfile"):
                        subprocess_arguments.append('--csl=%s' % self.cslfile)
                
                p = subprocess.Popen(
                        subprocess_arguments,
                        stdin=subprocess.PIPE, 
                        stdout=subprocess.PIPE
                )

		return p.communicate(self._content)[0]
