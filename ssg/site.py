from pathlib import Path

class Site:
	def _init_(self, source, dest):
		self.source = Path(source)
		self.dest = Path(dest)

	def create_dir(self, path):
		directory = self.dest + "/" + path.relative_to(self.source)
		directory.mkdir(parents = true, exist_ok = true)

	def build(self):
		self.dest.mkdir(parents = true, exist_ok = true)
		for path in self.source.rglob("*"):
			if(path.is_dir()):
				self.create_dir(path)
