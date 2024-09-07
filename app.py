from flask import Flask, render_template, request, redirect, url_for,Response
import os

app = Flask(__name__)

TEMPLATES = [
    'index', 'services', 'gallery', 'portfolio', 'login', 'signup', 'contact',
    'faq', 'testimonial', 'pricing', 'blog', 'about', 'team', 'terms', 'privacy'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    template_name = request.form.get('template_name')
    if template_name in TEMPLATES:
        create_html_file(template_name)
        return Response("<h1>Template Generated And Saved!</h1>")
    return "Template not found!", 404

def create_html_file(template_name):
    html_content = {
        'index': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index Page</title>
    <!-- Bootstrap CSS CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <!-- Custom CSS (Optional) -->
    <style>
        body {
            padding-top: 20px;
            text-align: center;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="display-4">Welcome to the Index Page</h1>
        <p class="lead">This is a simple page styled with Bootstrap.</p>
        <button id="fetchButton" class="btn btn-primary">Fetch Data</button>
        <div id="result" class="mt-3"></div>
    </div>

    <!-- jQuery CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <!-- Bootstrap Bundle with Popper CDN -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
    <!-- AJAX Example Script -->
    <script>
        $(document).ready(function() {
            $('#fetchButton').click(function() {
                $.ajax({
                    url: 'https://api.example.com/data', // Replace with your API endpoint
                    method: 'GET',
                    success: function(response) {
                        $('#result').html('<pre>' + JSON.stringify(response, null, 2) + '</pre>');
                    },
                    error: function() {
                        $('#result').html('<div class="alert alert-danger">An error occurred while fetching data.</div>');
                    }
                });
            });
        });
    </script>
</body>
</html>
''',
        'services': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Services</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.8.3/font/bootstrap-icons.min.css">
    <style>
        .service-item {
            margin-bottom: 30px;
        }
        .icon {
            font-size: 50px;
            color: #007bff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Our Services</h1>
        <div class="row">
            <div class="col-md-4 service-item text-center">
                <div class="icon">
                    <i class="bi bi-house"></i>
                </div>
                <h3>Service 1</h3>
                <p>Providing high-quality service for your needs.</p>
            </div>
            <div class="col-md-4 service-item text-center">
                <div class="icon">
                    <i class="bi bi-cpu"></i>
                </div>
                <h3>Service 2</h3>
                <p>Advanced solutions for your technology problems.</p>
            </div>
            <div class="col-md-4 service-item text-center">
                <div class="icon">
                    <i class="bi bi-people"></i>
                </div>
                <h3>Service 3</h3>
                <p>Expert consultation for business growth.</p>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'gallery': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .gallery-item {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Gallery</h1>
        <div class="row">
            <div class="col-md-4 gallery-item">
                <img src="https://via.placeholder.com/400x300" class="img-fluid" alt="Gallery Image 1">
            </div>
            <div class="col-md-4 gallery-item">
                <img src="https://via.placeholder.com/400x300" class="img-fluid" alt="Gallery Image 2">
            </div>
            <div class="col-md-4 gallery-item">
                <img src="https://via.placeholder.com/400x300" class="img-fluid" alt="Gallery Image 3">
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'portfolio': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .portfolio-item {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Portfolio</h1>
        <div class="row">
            <div class="col-md-4 portfolio-item">
                <div class="card">
                    <img src="https://via.placeholder.com/400x300" class="card-img-top" alt="Project 1">
                    <div class="card-body">
                        <h5 class="card-title">Project 1</h5>
                        <p class="card-text">Description of Project 1.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 portfolio-item">
                <div class="card">
                    <img src="https://via.placeholder.com/400x300" class="card-img-top" alt="Project 2">
                    <div class="card-body">
                        <h5 class="card-title">Project 2</h5>
                        <p class="card-text">Description of Project 2.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4 portfolio-item">
                <div class="card">
                    <img src="https://via.placeholder.com/400x300" class="card-img-top" alt="Project 3">
                    <div class="card-body">
                        <h5 class="card-title">Project 3</h5>
                        <p class="card-text">Description of Project 3.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'login': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .login-form {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="login-form">
        <h1>Login</h1>
        <form>
            <div class="mb-3">
                <label for="username" class="form-label">Username</label>
                <input type="text" class="form-control" id="username" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" required>
            </div>
            <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'signup': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .signup-form {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="signup-form">
        <h1>Sign Up</h1>
        <form>
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input type="email" class="form-control" id="email" required>
            </div>
            <div class="mb-3">
                <label for="password" class="form-label">Password</label>
                <input type="password" class="form-control" id="password" required>
            </div>
            <button type="submit" class="btn btn-primary">Sign Up</button>
        </form>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'contact': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h1>Contact Us</h1>
        <form>
            <div class="mb-3">
                <label for="name" class="form-label">Name</label>
                <input type="text" class="form-control" id="name" required>
            </div>
            <div class="mb-3">
                <label for="email" class="form-label">Email address</label>
                <input type="email" class="form-control" id="email" required>
            </div>
            <div class="mb-3">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" id="message" rows="4" required></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Send</button>
        </form>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'faq': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .faq-item {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Frequently Asked Questions</h1>
        <div class="accordion" id="faqAccordion">
            <div class="accordion-item faq-item">
                <h2 class="accordion-header" id="headingOne">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                        What is your return policy?
                    </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#faqAccordion">
                    <div class="accordion-body">
                        Our return policy is 30 days from the date of purchase. Please keep your receipt.
                    </div>
                </div>
            </div>
            <div class="accordion-item faq-item">
                <h2 class="accordion-header" id="headingTwo">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                        Do you offer international shipping?
                    </button>
                </h2>
                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#faqAccordion">
                    <div class="accordion-body">
                        Yes, we offer international shipping to most countries.
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'testimonial': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testimonials</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .testimonial-item {
            margin-bottom: 30px;
        }
        .testimonial-item img {
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">What Our Clients Say</h1>
        <div class="row">
            <div class="col-md-4 testimonial-item text-center">
                <img src="https://via.placeholder.com/100" alt="Client 1">
                <h3>Client 1</h3>
                <p>"The service was fantastic! I would definitely recommend them to others."</p>
            </div>
            <div class="col-md-4 testimonial-item text-center">
                <img src="https://via.placeholder.com/100" alt="Client 2">
                <h3>Client 2</h3>
                <p>"A top-notch experience. The team was professional and helpful."</p>
            </div>
            <div class="col-md-4 testimonial-item text-center">
                <img src="https://via.placeholder.com/100" alt="Client 3">
                <h3>Client 3</h3>
                <p>"I am extremely satisfied with the results. Great job!"</p>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'pricing': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pricing</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .pricing-table {
            margin-top: 20px;
        }
        .pricing-card {
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Pricing Plans</h1>
        <div class="row pricing-table">
            <div class="col-md-4">
                <div class="pricing-card">
                    <h3>Basic</h3>
                    <p class="price">$10/month</p>
                    <ul class="list-unstyled">
                        <li>Feature 1</li>
                        <li>Feature 2</li>
                        <li>Feature 3</li>
                    </ul>
                    <a href="#" class="btn btn-primary">Sign Up</a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="pricing-card">
                    <h3>Standard</h3>
                    <p class="price">$25/month</p>
                    <ul class="list-unstyled">
                        <li>Feature 1</li>
                        <li>Feature 2</li>
                        <li>Feature 3</li>
                        <li>Feature 4</li>
                    </ul>
                    <a href="#" class="btn btn-primary">Sign Up</a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="pricing-card">
                    <h3>Premium</h3>
                    <p class="price">$50/month</p>
                    <ul class="list-unstyled">
                        <li>Feature 1</li>
                        <li>Feature 2</li>
                        <li>Feature 3</li>
                        <li>Feature 4</li>
                        <li>Feature 5</li>
                    </ul>
                    <a href="#" class="btn btn-primary">Sign Up</a>
                </div>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'blog': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .blog-post {
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Blog</h1>
        <div class="row">
            <div class="col-md-6 blog-post">
                <h2>Blog Post 1</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ac vestibulum arcu.</p>
                <a href="#" class="btn btn-primary">Read More</a>
            </div>
            <div class="col-md-6 blog-post">
                <h2>Blog Post 2</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam ac vestibulum arcu.</p>
                <a href="#" class="btn btn-primary">Read More</a>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'about': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .about-content {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">About Us</h1>
        <div class="about-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.</p>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'team': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Team</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .team-member {
            margin-bottom: 30px;
        }
        .team-member img {
            border-radius: 50%;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Meet Our Team</h1>
        <div class="row">
            <div class="col-md-4 team-member text-center">
                <img src="https://via.placeholder.com/150" alt="Team Member 1">
                <h3>Team Member 1</h3>
                <p>Role and a brief description of the team member.</p>
            </div>
            <div class="col-md-4 team-member text-center">
                <img src="https://via.placeholder.com/150" alt="Team Member 2">
                <h3>Team Member 2</h3>
                <p>Role and a brief description of the team member.</p>
            </div>
            <div class="col-md-4 team-member text-center">
                <img src="https://via.placeholder.com/150" alt="Team Member 3">
                <h3>Team Member 3</h3>
                <p>Role and a brief description of the team member.</p>
            </div>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'terms': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terms of Service</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .terms-content {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Terms of Service</h1>
        <div class="terms-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.</p>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        'privacy': '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy Policy</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/css/bootstrap.min.css">
    <style>
        .privacy-content {
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="my-4">Privacy Policy</h1>
        <div class="privacy-content">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum.</p>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>
''',
        # Add more templates as needed
    }
    
    if template_name in html_content:
        file_name = f"{template_name}.html"
        with open(file_name, 'w') as file:
            file.write(html_content[template_name])
        print(f"{file_name} created successfully.")
    else:
        print(f"No template named '{template_name}' found.")

def main():
    print("Options: index, services, gallery, portfolio, login, signup, contact, faq, testimonial, pricing, blog, about, team, terms, privacy")  # List all available options
    user_input = input("SwiftStack: Enter an option or a template name: ").strip()
    
    if user_input == "options":
        print("SwiftStack: Available templates:")
        print("index, services, gallery, portfolio, login, signup, contact, faq, testimonial, pricing, blog, about, team, terms, privacy")  # List all available options
    else:
        create_html_file(user_input)

if __name__ == "__main__":
    app.run(debug=True)