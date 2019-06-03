import sys

class IndentationClass:
	def __init__(self, content):
		self.version = []
		self.indent = 1
		self.tab_space = 4
		self.prev_line = []
		self.cur_line = self.get_parsed_line(content.readline().strip())
		self.content = content
		self.collaspe_state = "-"

	def header_number(self, indent):
		try:
			self.version[len(indent)-1] += 1
                        self.version = self.version[:len(indent)]
		except IndexError:
			self.version.append(1)

	def get_parsed_line(self, line):
		if line[0] not in ["*", "."]:
			parsed_line = [' ' * (self.tab_space + 2) * self.indent, line]
		bullet, text = line.split(' ', 1)
		if "*" in bullet:
			self.collaspe_state = "-"
                        if self.prev_line and len(self.prev_line) == 3:
                                self.prev_line[1] = self.collaspe_state
			self.indent = 1
			self.header_number(bullet)
			parsed_line = [".".join(map(str, self.version)), text]
		elif "." in bullet:
			self.collaspe_state = "-"
			if len(bullet) > self.indent:
				self.collaspe_state = "+"
			self.indent = len(bullet)
			if len(self.prev_line) == 3:
				self.prev_line[1] = self.collaspe_state
			parsed_line = [' ' * self.indent * self.tab_space, self.collaspe_state, text]
		return parsed_line

	def output(self):
		for line in self.content:
			if not line.strip():
				continue
			self.prev_line = self.cur_line
			self.cur_line = self.get_parsed_line(line.strip())
			print " ".join(self.prev_line)
		if len(self.cur_line) == 3:
			self.cur_line[1] = "-"
		print " ".join(self.cur_line)
	

if __name__ == "__main__":
	w = IndentationClass(sys.stdin)
	w.output()
