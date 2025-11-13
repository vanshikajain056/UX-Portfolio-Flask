from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the root route ("/") to serve the main portfolio page
@app.route("/")
def portfolio():
    # Renders the HTML file found in the 'templates' folder
    return render_template("index.html")

# Define a simple function to run the application
if __name__ == "__main__":
    # debug=True allows the server to automatically restart when you save changes
    app.run(debug=True)