"""
9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""

exam_st_date = (11, 12, 2014)

print("The examination will start from : " + exam_st_date[0].__str__() + " / " + exam_st_date[1].__str__() + " / " + exam_st_date[2].__str__())
