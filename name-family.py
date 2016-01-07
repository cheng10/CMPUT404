class Student:
	courseMarks={}
	name=""
	def _int_(self, name, family):
		self.name=name
		self.family=family
	def addCourseMark(self, course, mark):
		self.courseMark[course]=mark
	def average(self):
		return sum(self.courseMark.values())

jack=Student("Jack", "Chen")
jack.addCourseMark(Math101,100)
jack.addCourseMark(Math102,80)
print jack.average(self)
