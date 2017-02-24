class MinmlDB(object):
	"""
	Main database class
	"""

	def __init__(self, *args, **kwargs):
		"""
		Create a new instance of MinmlDB
		
		:param storage: The class of the type of storage to be user
						Default storage class is JSONStorage
		"""

		pass
		
	def collection(self, name=DEFUALT_COLLECTION, **options):
		"""
		Access a specific table
		
		:param name: Name of the table (string)
		:param cache_size: Number of query results to cache
		"""

		pass

	def collections(self):
		"""
		Get the names of all the tables in the database
		"""

		pass

	def purge_collection(self, name):
		"""
		Purge a specific collection from the database
		
		:para name: Name of the collection to be purged 
		"""

		pass

	def purge_collection(self):
		"""
		Purge all the collections in the database
		"""

		pass

	def close(self):
		"""
		Close the database
		"""

		pass

	def __enter__(self):
		""" Executed when the class is entered - instance is created.
		To be along with the with statement"""

		#TODO: Read more about context managers
		return self

	def __exit__(self, *args):
		""" Executed when the class is exited - instance goes out of scope 

		:param args: Exception arguments
		"""
		# Check of the db is closed 

