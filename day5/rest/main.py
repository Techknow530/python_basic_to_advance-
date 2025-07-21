from flask import  Flask , jsonify , request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling"},
    {"id": 2, "title": "Atomic Habits", "author": "James Clear"}
]

#home route 
@app.route("/")
def home():
    return "welcome to  the book api"

#get all boook 

@app.route("/books",methods =['GET'])
def get_books():
    return jsonify(books)

#get book by id 
@app.route("/book/<int:book_id>",methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return jsonify(book)
    return jsonify({"error":"book not found "}) ,404

#post(create) a new book 

@app.route("/books",methods=["POST"])
def add_book():
    data=request.get_json()
    new_book = {
        "id": len(books) +1,
        "title":data["title"],
        "author":data["author"]
    }
    books.append(new_book)
    return jsonify(new_book),201



#put (update) book by id 
@app.route("/book/<int:book_id>",methods=["PUT"])
def update_book(book_id):
    data= request.get_json()
    for book in books:
        if book["id"] == book_id:
            book["title"] = data.get("title",book["title"])
            book["author"]=data.get("author",book["author"])
            return jsonify(book)
    return jsonify({"error":"Book not found"}),404

#delete book by id 

@app.route("/book/<int:book_id>",methods=["DELETE"])
def delete_book(book_id):
    data = request.get_json()
    for index,book in enumerate(books):
        if book["id"] == book_id:
            delete_book = books.pop(index)
            return jsonify(delete_book)
    return jsonify({"error":"Book not FOund "}),404





if __name__ == "__main__":
    app.run(debug=True)
