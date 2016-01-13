class Student:
	courseMarks={}
	name=""
	family=""
	def __init__(self, name, family):
		self.name=name
		self.family=family
	def addCourseMark(self, course, mark):
		self.courseMarks[course]=mark
	def average(self):
		return sum(self.courseMarks.values())/len(self.courseMarks)
	
if __name__ == "__main__": 
	jack=Student("Jack", "Chen")
	jack.addCourseMark("Math101",100)
	jack.addCourseMark("Math102",80)
	print "Name:" + jack.name
	print "Family:" + jack.family
	print "Average:" +str(jack.average())
