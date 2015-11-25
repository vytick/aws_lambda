import  psycopg2
import psycopg2.extras
import json


class PostgreSQL():
	def __init__(self, sett):
		self.conn_string = sett['string']
		self.conn = psycopg2.connect(self.conn_string)
		self.cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	def __del__(self):
		self.conn.close()


db = PostgreSQL({
	'string' : "host='path_to_database' dbname='transaccounts' user='username' password='password'"
	})


def getComments(transaction_id):
	db.cursor.execute("SELECT * FROM comments WHERE id = ", (str(transaction_id)) 
	return db.cursor.fetchall()


def add_comment_handler(event, context):
	response = dict()
	response["result"] = "FAILED"

	if (isinstance(event, dict)):
		if ("transaction_id" in event.keys()):
			comments = getComments(event["transaction_id"])
			response = json.dumps(comments)
		else:
			response["reason"] = "WRONG KEYS RECEIVED: %s", ''.join(str(e) for e in event.keys())
	else:
		response["reason"] = "NO DICT"


	return json.dumps(response)

	

