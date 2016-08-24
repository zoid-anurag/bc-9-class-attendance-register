from datetime import datetime

from database_connections import database_insert_reason
from database_connections import database_return_reasons
from database_connections import database_insert_ongoing
from database_connections import database_return_ongoing
from database_connections import database_delete_ongoing
from database_connections import database_insert_inclass
from database_connections import database_return_inclass
from database_connections import database_delete_inclass
from database_connections import database_return_classes
from database_connections import database_return_students

"""This is the attendance register and it contains functions or methods
to initiate and stop classes as well as checking students in and out of 
classes. It also passes relevant data to database_connection module
"""
class AttendanceRegister(object):

	def __init__():
		pass

	 
	@staticmethod
	def log_start(class_id):
	#method to log in a class if not logged in
		time = datetime.now()
		if class_id in database_return_ongoing():
			return "Class already logged in"
		for dataset in database_return_classes():
			if class_id in dataset:
				print(class_id)
				database_insert_ongoing(class_id, time)
				return "Class of id: {}, logged in".format(class_id)
		return "Class not created yet"
		
	@staticmethod
	def log_end(class_id):
	#method to log out a class if it is logged in 
		if class_id in database_return_ongoing():
			database_delete_ongoing(class_id)
			return "Class has been logged out"
		return "Class is not on going"


	@staticmethod
	def check_in(student_id, class_id):
	#method to check student into a particular class
		if student_id in database_return_inclass():
			return "Student already attending class"
		for dataset in database_return_students():
			if student_id in dataset:
				print(student_id)
				database_insert_inclass(student_id, class_id)
				return "Student ID: {} checked into class ID: {}".format(student_id, class_id)
		return "Student not created yet"

 
	@staticmethod
	#method to check out student from a class
	def check_out(student_id, class_id, reason):
		day = datetime.now()
		s_id = student_id
		c_id = class_id
		rea = reason
		for student in database_return_inclass():
			if student_id == int(student):
				database_delete_inclass(s_id, c_id)
				database_insert_reason(s_id, c_id, day, rea)
				return "Student ID: {} has been checked out".format(student_id)
		return "Student not attending a class"

	@staticmethod
	def show_reasons():
		print(database_return_reasons())


#print(AttendanceRegister.check_out(2, 1, "sick"))