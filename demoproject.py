import sys

class IndentationClass:
	def __init__(self, content):
		self.version = []
		self.indent = 0
		self.tab_space = 4
		self.prev_line = []
		self.cur_line = []
		self.content = content
		self.collaspe_state = "-"

	def header_number(self, indent):
		try:
			self.version[len(indent)-1] += 1
                        self.version = self.version[:len(indent)]
		except IndexError:
			self.version.append(1)

	def output(self):
		for line in self.content:
                        if not line.strip():
                                continue

			bullet, text = line.split(' ', 1)
			if "*" in bullet:
				self.collaspe_state = "-"
				if self.prev_line:
					self.indent = 1
				self.header_number(bullet)
				if len(self.prev_line) == 3:
					self.prev_line[1] = self.collaspe_state
				self.cur_line = [".".join(map(str, self.version)), text]
			elif "." in bullet:
				self.collaspe_state = "-"
				if len(bullet) > self.indent:
					self.collaspe_state = "+"
				self.indent = len(bullet)
				self.cur_line = [' ' * self.indent * self.tab_space, self.collaspe_state, text]
				if len(self.prev_line) == 3:
					self.prev_line[1] = self.collaspe_state
			else:
				self.prev_line[-1] += " ".join([' ' * (self.tab_space + 2) * self.indent, line])
				continue

			if self.prev_line:
				sys.stdout.write(" ".join(self.prev_line))
			self.prev_line = self.cur_line

		if len(self.prev_line) == 3:
			self.prev_line[1] = "-"
		sys.stdout.write(" ".join(self.prev_line))


if __name__ == "__main__":
	w = IndentationClass(sys.stdin)
	w.output()
