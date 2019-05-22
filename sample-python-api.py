import json
import falcon
import psycopg2


class Youngest:
	def on_get(self, req, resp):
		try:
			conn = psycopg2.connect('dbname=gigacover')
			cur = conn.cursor()
			cur.execute("""SELECT name FROM CUSTOMERS WHERE dob = (SELECT MAX(dob) FROM CUSTOMERS);""")
			results = cur.fetchall()
			cur.close()
		except (Exception, psycopg2.DatabaseError) as error:
			print(error)
		finally:
			if conn is not None:
				conn.close()
				resp.body = json.dumps(results, default=str)
				resp.status = falcon.HTTP_200


class Customers:
	"""GET call"""
	def on_get(self, req, resp):
		try:
			conn = psycopg2.connect('dbname=gigacover')
			cur = conn.cursor()
			cur.execute("""SELECT * FROM CUSTOMERS""")
			results = cur.fetchall()
			cur.close()

		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

		finally:
			if conn is not None:
				conn.close()
				resp.body = json.dumps(results, default=str)
				resp.status = falcon.HTTP_200

	"""POST Call"""
	def on_post(self, req, resp):
		data = json.loads(req.stream.read())
		name = data['name']
		dob = data['dob']
		updated_at = data['updated_at']
		sql = """ INSERT INTO CUSTOMERS (name, dob, updated_at) VALUES(%s, %s, %s)"""

		try:
			conn = psycopg2.connect('dbname=gigacover')
			cur = conn.cursor()
			cur.execute(sql, (name, dob, updated_at))
			conn.commit()
			cur.close()

		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

		finally:
			if conn is not None:
				conn.close()
		successmessage = 'Successfully added ' + name
		obj = {}
		obj['message'] = successmessage
		resp.body = json.dumps(obj)
		resp.status = falcon.HTTP_200

	"""PUT CALL"""
	def on_put(self, req, resp):
		data = json.loads(req.stream.read())
		name = data['name']
		dob = data['dob']
		updated_at = data['updated_at']
		sql = """ UPDATE customers SET dob = %s, updated_at = %s WHERE name = %s"""

		try:
			conn = psycopg2.connect('dbname=gigacover')
			cur = conn.cursor()
			cur.execute(sql, (dob, updated_at, name))
			conn.commit()
			cur.close()

		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

		finally:
			if conn is not None:
				conn.close()
			successmessage = 'Successfully updated ' + name
			obj = {}
			obj['message'] = successmessage
			resp.body = json.dumps(obj)
			resp.status = falcon.HTTP_200

	"""DELETE CALL"""
	def on_delete(self, req, resp):
		data = json.loads(req.stream.read())
		name = data['name']
		sql = """ DELETE FROM CUSTOMERS WHERE name = %s"""

		try:
			conn = psycopg2.connect('dbname=gigacover')
			cur = conn.cursor()
			cur.execute(sql, (name,))
			conn.commit()
			cur.close()

		except (Exception, psycopg2.DatabaseError) as error:
			print(error)

		finally:
			if conn is not None:
				conn.close()
			deletemessage = 'Successfully deleted ' + name
			obj = {}
			obj['message'] = deletemessage
			resp.body = json.dumps(obj)
			resp.status = falcon.HTTP_200


api = falcon.API()
api.add_route('/test', Customers())
api.add_route('/youngest', Youngest())