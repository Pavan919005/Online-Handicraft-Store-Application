import sqlite3
import json
from flask import Flask,jsonify,request,make_response,Response,abort,Response
app = Flask(__name__)

@app.route('/products',methods=['POST'])
def postproduct():
      if not request.json:
           return make_response(jsonify("please provide data in json format"),400)
      data = request.json


      try:
          if(data["productid"]):
               print("productid has been given")
      except:
          return make_response(jsonify("productid has not been given"),400)

      try:
          if(data["name"]):
               print("Name has been given")
      except:
          return make_response(jsonify("name"),400)

      try:
          if(data["description"]):
               print("Description has been given")
      except:
          return make_response(jsonify("description"),400)

      try:
          if(data["price"]):
               print("price has been given")
      except:
          return make_response(jsonify("price has not been given"),400)

      conn = sqlite3.connect("Handicrafts.db")
      c = conn.cursor()
      c.execute("Select * from products")
      for row in c.fetchall():
          if(int(data["productid"])==row[0]):
                return make_response(jsonify("productid"),400)
      conn.commit()
      c.close()
      conn.close()

      conn = sqlite3.connect("Handicrafts.db")
      c = conn.cursor()
      c.execute("INSERT INTO products (productid,name,description,price) VALUES (?,?,?,?)",(data["productid"],data["name"],data["description"],data["price"],))
      conn.commit()
      c.close()
      conn.close()
      return jsonify({}),201


@app.route('/products',methods=['GET'])
def getproducts():
      conn = sqlite3.connect("Handicrafts.db")
      c = conn.cursor()
      c.execute("Select * from products")
      products=list()
      for row in c.fetchall():
            product={
             "productid":row[0],
             "name":row[1],
             "description":row[2],
             "price":row[3]
            }
            products.append(product)
      conn.commit()
      c.close()
      conn.close()
      return  Response(json.dumps(products), mimetype='application/json')

@app.route('/products/<int:productid>',methods=['DELETE'])
def deleteproduct(productid):
   conn1 = sqlite3.connect("Handicrafts.db")
   c1 = conn1.cursor()
   c1.execute("Select * from products")
   for row in c1.fetchall():
        if (row[0]==productid):
            conn = sqlite3.connect("Handicrafts.db")
            c = conn.cursor()
            c.execute("Delete  from products where productid=(?)",(productid,))
            conn.commit()
            c.close()
            conn.close()
            return make_response(jsonify(), 200)

   conn1.commit()
   c1.close()
   conn1.close()
   return make_response(jsonify("productid"),400)
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='5000')
