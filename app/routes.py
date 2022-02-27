from flask import current_app as app

@app.route("/test")
def test():
    return {"successful":True}