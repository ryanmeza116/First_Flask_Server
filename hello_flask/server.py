from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/success')
def success():
    return "Success"

@app.route('/users/<username>/<id>')
def show_user_profile(username,id):
    print(username)
    print(id)
    return"username: " + username + ", id: " + id

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say_hello_to_name(name):
    return f"Hi {name.capitalize()} !"
# name.capitalize() causes the first letter to be a capital. 

@app.route('/repeat/<int:num>/<string:word>')
# int: and string: converts the data in the url to a int and string respectively to our code 
def repeat_word(num,word):
    output = ' '
    for i in range(0,num):
        output += f'<p>{word}</p>'
# Having a + = means we are added to the already existent value, which gives us the "repeating" effect desired. 
    return output








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.