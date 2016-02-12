class binary_search():

	def _init__(self):
		list_values = [1,2,3,4,5,5,5,5,6,7,7,7,8]
		high = len(list_values)
		low = 0
		x = 5
		result = 0

	def occurence(self,low,high,x):

		while low <= high:
			mid = int((low+high)/2)

			if list_values[mid] ==  x:
				print  (list_values[mid])
				result +=1

			elif x < list_values[mid]:
				high = mid-1
			else: 
				low = mid+1


a = binary_search()

