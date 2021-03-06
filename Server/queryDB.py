import sqlite3

class pacrom_db:
	def __init__(self, db_name):
		self.c = None
		self.db_name = db_name
		self.conn = None


	def Connect(self):
		try:
			self.conn = sqlite3.connect(self.db_name)
			self.c = self.conn.cursor()
			self.conn.isolation_level = None
			return 1
		except:
			return 0

	def Close(self):
		try:
			self.c.close()
			return 1
		except:
			return 0

	def AddMemberToLocalChat(self, userName, address):
		"""Once a user logged in to the local server, add them to the connected users"""
		query = """INSERT INTO localUser (uname, ipAddress) values ("%s", "%s")""" % (userName, address)
		if userName == "":
			return 0
		try: 
			self.c.execute(query)
			print "Added to local chat [" + userName + "]\n"
			return 1
		except sqlite3.IntegrityError as error:
			if error.message.split()[0] == "UNIQUE":
				return 0 
			else:
				raise

	def removeMemberFromLocalChat(self, userName,address) :
		"""Remove user from localchat once DC or logout"""
		query = """DELETE FROM localUser where uname = ("%s") and ipAddress = ("%s") """ % (userName, address)
		try:
			self.c.execute(query)
			print "DC from local chat [" +userName+"]\n"
			return 1
		except:
			return 0

	def GetLocalChatUsers(self,address):
		"""Will be used to show all the connected users in the local server"""
		query = """ SELECT uname FROM localUser where ipAddress = ("%s") """ % address

		try:
			self.c.execute(query)
			return self.c.fetchall()
		except:
			return 0

def runLocalChat():
	conn = sqlite3.connect("pacromDB.db")
	c = conn.cursor()
	c.execute("""DROP TABLE localUser""")
	c.execute("""CREATE TABLE localUser (uname TEXT UNIQUE NOT NULL) """)

# test = pacrom_db("pacromDB.db")
# test.Connect()
