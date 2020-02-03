def Articles():
    data = [
        {'id': 1,
        'title':'Article Python Data',
        'body':'we saw how to begin building a basic RESTful web server with Flask, limited to GET requests. This allowed retrieval of a dataset and some of its subsets. For most visualizations, the constraint that data be passively consumed, not altered, is acceptable,1 but even allowing for this, a lot of fairly basic stuff was missing (e.g., the ability to paginate retrieved data, allowing you to control the size of responses from the server). In this chapter, we’ll see two Flask RESTful plugins that add this functionality and a whole lot more for the price of a few lines of Python. I think you’ll be impressed by how much web API can be rolled with so little.',  
        'author':'Gary',
        'create_date':'06-24-2019'},
        {'id': 2,
        'title':'Flask is',
        'body':'Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.',  
        'author':'James',
        'create_date':'02-03-2020'},
        {'id': 3,
        'title':'Application Setup',
        'body':'A Flask application is an instance of the Flask class. Everything about the application, such as configuration and URLs, will be registered with this class.',  
        'author':'Park',
        'create_date':'02-03-2020'}
    ]
    return data