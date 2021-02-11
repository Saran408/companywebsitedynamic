# Dynamic Website Design for a Manufacturing Company
## AIM:
To design a dynamic website for a chip manufacturing company.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Updating the sample content.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 7:
Create a database model and migrate the database.
### Step 8:
Retrieve data from database and display it in a dynamic webpage.
### Step 9:
Publish the website in the given URL.

## PROGRAM:

### base.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Silicon Private Limited</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
    <link rel = "icon" href ="{% static 'img/titleicon.png' %}" type = "image/x-icon"> 
              
</head>

<body>
    <div class="container">
    <div class="banner">
       <h1>Silicon Private Limited</h1>
    </div>
    <div class="menu">
        <div class="menuitem"><a href="/home">Home</a></div> 
        <div class="menuitem"><a href="/products">Products</a></div> 
        <div class="menuitem"><a href="/people">People</a></div>
        <div class="menuitem"><a href="/contactus">Contact Us</a></div> 
    </div><div class="content">
    {% block content %}    
    {% endblock  %}
    </div>
    <div class="footer">
        Copyright © 2020 Silicon Private Limited, Developed by SARAN.
    </div>
    </div>
</body>

</html>
```
### home.html
```
{% extends "companyapp/base.html" %}

{% block content %}
    <div class="homecontent">    
    <h1>About Us</h1>
    <img src="/static/img/arch.jpg" alt="Building">
    <div class="contenttext">
    Silicon Pvt Ltd, provides a broad range of semiconductor and infrastructure software applications that serve the data center, networking, software, broadband, wireless, and storage and industrial markets. Common applications for its products include: data center networking, home connectivity, broadband access, telecommunications equipment, smartphones, base stations, data center servers and storage, factory automation, power generation and alternative energy systems, displays, and mainframe operations and management, and application software development. Some of Silicon's core technologies and products include:
    <ul>
        <li>Memory Chips</li>
        <li>SATA HDD</li>
        <li>SATA SSD </li>
        <li>Broadband Modems</li>
        <li>Wifi Devices</li>
        <li>Switching Devices</li>
        <li>Optical Sensors</li>
    </ul>
    </div>
    </div>
{% endblock  %}
```
### people.html
```
{% extends "companyapp/base.html" %}
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>PEOPLE LIST</title>
    <link rel="stylesheet" href="{% static 'css/layout.css' %}">
</head>

<body>
    {% block content %}
    <div class="content">
        <h1>OUR PEOPLES</h1>
        <div class="productcontent">
            <div class="productitems">
                {% for people in peoples %}
                <div class="productitem">
                    <div class="itemimage">
                        <img src="{{ people.photo.url }}" alt="people image">
                    </div>
                    <div class="peoplephoto">{{ photo }}</div>
                    <div class="itemname">{{ people.name }}</div>
                    <div class="itemprice">{{ people.designation }}</div>
                </div>
                {% endfor %}
            </div>
       </div>
    </div>
    {% endblock %}
</body>

</html>
```
### products.html
```
{% extends "companyapp/base.html" %}
{% load static %}
<!DOCTYPE html>
<html>

<head>
    <title>PRODUCTS LIST</title>
    <link rel="stylesheet" href="{% static 'css/people.css' %}">
</head>

<body>
    {% block content %}
    <div class="content">
        <h1>OUR PREMIUM PRODUCTS</h1>
        <div class="productcontent">
            <div class="productitems">
                {% for product in products %}
                <div class="productitem">
                    <div class="itemimage">
                        <img src="{{ product.photo.url }}" alt="product image">
                    </div>
                    <div class="peoplephoto">{{ photo }}</div>
                    <div class="itemname">{{ product.name }}</div>
                    <div class="itemprice">{{ product.price }}</div>
                </div>
                {% endfor %}
            </div>
        </div>
    </div>
    {% endblock %}
</body>

</html>
```
### contactus
```
{% extends "companyapp/base.html" %}

{% block content %}
    <div class="productcontent">    
    <h1>Contact Us</h1> 
    <div class="productitems">
        <div class="productitem"> 
            <div class="contactname"><h1>E-MAIL : silicon@gmail.com</h1></div>
            <div class="contactprice"><h1> Contact No : 9384419249 </h1></div>
        </div>
        <div class="productitem"></div>
        <div class="productitem"> 
            <div class="contactimage">
            <img src="/static/img/indian.jpg"  alt="product image">
            </div>
        </div>
    </div>
    </div> 
{% endblock  %}
```
## OUTPUT:
![output](./static/img/homeput.png)

![output](./static/img/productput.png)

![output](./static/img/peopleput.png)

![output](./static/img/contactusput.png)

##  CODE VALIDATION REPORT
![output](./static/img/homeputvali.png)

![output](./static/img/productputvali.png)

## RESULT:
Thus a website is designed for the chip manufacturing company and is hosted in the URL http://saran.student.saveetha.in:8000/. HTML code is validated.