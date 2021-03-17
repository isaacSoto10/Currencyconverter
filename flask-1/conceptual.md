### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
- **One of the most important differencesthat i notice is that so far one is used to back-end development and the other one to front-end development.**

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  ****:

- What is a unit test?
- **Automated test run by developers to ensure that a certain section of an application meeths its design and requierements.**

- What is an integration test?**A test to test the whole program, and not just a section or fragment**

- What is the role of web application framework, like Flask?
- **Third-party frameworks to develop web applications**

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
- **The seconf option fits better to specify the items/models/requirements of the direction/serach**

- How do you collect data from a URL placeholder parameter using Flask?
**using routes**
- How do you collect data from the query string using Flask?
- **Using the method request.args.get; user = request.args.get('user')** 

- How do you collect data from the body of the request using Flask?
- **using request.form**

- What is a cookie and what kinds of things are they commonly used for?
**It is a storage and theyre used to collect information so you dont have to put it again every time you get in to the web app**
- What is the session object in Flask?
- 
- **is data stored on the server**

- What does Flask's `jsonify()` do? **jsonify serializes data to JavaScript Object Notation (JSON) format, wraps it in a Response object with the application/json mimetype. Note that jsonify is sometimes imported directly from the flask module instead of from flask.** 
