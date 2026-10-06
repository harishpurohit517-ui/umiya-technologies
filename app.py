
from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# =========================================================
# PRODUCTS
# =========================================================

products = [
    {
        "name": "1.8 GB RAM",
        "price": "₹3,000",
        "category": "RAM",
        "description": "1.8 GB laptop RAM",
        "image": "ram.jfif"
    },
    {
        "name": "Dell Keyboard + Mouse Combo",
        "price": "₹1,000",
        "category": "Keyboard & Mouse",
        "description": "Dell keyboard and mouse combo",
        "image": "dell_combo.jfif"
    },
    {
        "name": "HS04 Battery",
        "price": "₹700",
        "category": "Battery",
        "description": "HS04 laptop battery",
        "image": "hs04_battery.jfif"
    },
    {
        "name": "256 GB SSD",
        "price": "₹2,000",
        "category": "SSD",
        "description": "256 GB laptop SSD",
        "image": "ssd_256gb.jfif"
    },
    {
        "name": "Laptop Screen",
        "price": "₹5,000",
        "category": "Screen",
        "description": "Laptop replacement screen",
        "image": "laptop_screen.jfif"
    },
    {
        "name": "Laptop Panel",
        "price": "₹700",
        "category": "Panel",
        "description": "Laptop replacement panel",
        "image": "laptop_panel.jfif"
    },
    {
        "name": "Laptop Touchpad",
        "price": "₹700",
        "category": "Touchpad",
        "description": "Laptop replacement touchpad",
        "image": "laptop_touchpad.jfif"
    }
]


# =========================================================
# WEBSITE HTML
# =========================================================

HTML = """

<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>UMIYA TECHNOLOGIES</title>


<style>

/* =====================================================
   BASIC
   ===================================================== */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: Arial, sans-serif;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #f5f7fa;
    color: #222;
}


/* =====================================================
   HEADER
   ===================================================== */

header {

    background: #111827;

    color: white;

    padding: 20px 7%;

    display: flex;

    justify-content: space-between;

    align-items: center;

    position: sticky;

    top: 0;

    z-index: 1000;
}

.logo {

    font-size: 25px;

    font-weight: bold;

    letter-spacing: 1px;
}

nav a {

    color: white;

    text-decoration: none;

    margin-left: 25px;

    font-size: 16px;

    transition: 0.3s;
}

nav a:hover {

    color: #60a5fa;
}


/* =====================================================
   HERO
   ===================================================== */

.hero {

    background:
        linear-gradient(
            135deg,
            #111827,
            #2563eb
        );

    color: white;

    text-align: center;

    padding: 90px 20px;
}

.hero h1 {

    font-size: 48px;

    margin-bottom: 15px;
}

.hero p {

    font-size: 20px;

    margin-bottom: 30px;
}

.search-box {

    width: 90%;

    max-width: 600px;

    padding: 17px 22px;

    border: none;

    border-radius: 30px;

    font-size: 16px;

    outline: none;
}


/* =====================================================
   GENERAL SECTIONS
   ===================================================== */

.section {

    padding: 60px 7%;
}

.section-title {

    text-align: center;

    font-size: 32px;

    margin-bottom: 35px;
}


/* =====================================================
   CATEGORIES
   ===================================================== */

.categories {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(160px, 1fr)
        );

    gap: 20px;
}

.category {

    background: white;

    padding: 25px;

    border-radius: 15px;

    text-align: center;

    box-shadow:
        0 5px 20px
        rgba(0,0,0,0.08);

    font-size: 18px;

    font-weight: bold;

    transition: 0.3s;
}

.category:hover {

    transform: translateY(-5px);
}


/* =====================================================
   PRODUCTS
   ===================================================== */

.products {

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(250px, 1fr)
        );

    gap: 25px;
}

.product {

    background: white;

    border-radius: 18px;

    overflow: hidden;

    box-shadow:
        0 5px 20px
        rgba(0,0,0,0.10);

    transition: 0.3s;
}

.product:hover {

    transform: translateY(-7px);

    box-shadow:
        0 10px 30px
        rgba(0,0,0,0.15);
}


/* =====================================================
   PRODUCT IMAGE
   ===================================================== */

.product-image {

    width: 100%;

    height: 230px;

    background: #eeeeee;

    display: flex;

    justify-content: center;

    align-items: center;

    overflow: hidden;
}

.product-image img {

    width: 100%;

    height: 100%;

    object-fit: contain;
}


/* =====================================================
   PRODUCT INFORMATION
   ===================================================== */

.product-info {

    padding: 20px;
}

.product-info h3 {

    font-size: 21px;

    margin-bottom: 10px;
}

.category-name {

    color: #2563eb;

    font-size: 14px;

    font-weight: bold;

    margin-bottom: 8px;
}

.description {

    color: #666;

    margin-bottom: 15px;
}

.price {

    font-size: 23px;

    font-weight: bold;

    color: #111827;
}


/* =====================================================
   CONTACT
   ===================================================== */

.contact {

    background: #111827;

    color: white;

    text-align: center;

    padding: 70px 20px;
}

.contact h2 {

    font-size: 34px;

    margin-bottom: 20px;
}

.contact p {

    font-size: 18px;

    margin: 10px;
}

.phone {

    display: inline-block;

    margin-top: 10px;

    padding: 13px 25px;

    background: #2563eb;

    color: white;

    text-decoration: none;

    border-radius: 30px;

    font-size: 20px;

    font-weight: bold;

    transition: 0.3s;
}

.phone:hover {

    background: #60a5fa;

    color: #111827;
}


/* =====================================================
   FOOTER
   ===================================================== */

footer {

    background: #080c14;

    color: #aaa;

    text-align: center;

    padding: 22px;
}


/* =====================================================
   MOBILE
   ===================================================== */

@media (max-width: 700px) {

    header {

        flex-direction: column;

        gap: 15px;
    }

    nav a {

        margin: 0 8px;
    }

    .hero h1 {

        font-size: 35px;
    }

    .hero {

        padding: 65px 15px;
    }

    .section {

        padding: 45px 5%;
    }

}

</style>

</head>


<body>


<!-- =====================================================
     HEADER
     ===================================================== -->

<header>

    <div class="logo">

        UMIYA TECHNOLOGIES

    </div>


    <nav>

        <a href="#home">
            Home
        </a>

        <a href="#products">
            Products
        </a>

        <a href="#contact">
            Contact
        </a>

    </nav>

</header>



<!-- =====================================================
     HERO
     ===================================================== -->

<section
    class="hero"
    id="home"
>

    <h1>
        UMIYA TECHNOLOGIES
    </h1>

    <p>
        Laptop Parts & Accessories
    </p>


    <input

        type="text"

        id="search"

        class="search-box"

        placeholder="Search for a product..."

        onkeyup="searchProducts()"

    >

</section>



<!-- =====================================================
     CATEGORIES
     ===================================================== -->

<section class="section">

    <h2 class="section-title">
        Categories
    </h2>


    <div class="categories">

        <div class="category">
            💾 RAM
        </div>

        <div class="category">
            💽 SSD
        </div>

        <div class="category">
            🔋 Batteries
        </div>

        <div class="category">
            ⌨️ Keyboard & Mouse
        </div>

        <div class="category">
            🖥️ Screens
        </div>

        <div class="category">
            🖱️ Touchpads
        </div>

        <div class="category">
            🧩 Panels
        </div>

    </div>

</section>



<!-- =====================================================
     PRODUCTS
     ===================================================== -->

<section
    class="section"
    id="products"
>

    <h2 class="section-title">
        Our Products
    </h2>


    <div
        class="products"
        id="productList"
    >


        {% for product in products %}

        <div

            class="product"

            data-name="{{ product.name }}"

            data-category="{{ product.category }}"

        >


            <div class="product-image">

                <img

                    src="{{ url_for(
                        'product_image',
                        filename=product.image
                    ) }}"

                    alt="{{ product.name }}"

                >

            </div>


            <div class="product-info">

                <h3>
                    {{ product.name }}
                </h3>


                <div class="category-name">

                    {{ product.category }}

                </div>


                <div class="description">

                    {{ product.description }}

                </div>


                <div class="price">

                    {{ product.price }}

                </div>

            </div>


        </div>

        {% endfor %}


    </div>

</section>



<!-- =====================================================
     CONTACT
     ===================================================== -->

<section
    class="contact"
    id="contact"
>

    <h2>
        Contact Us
    </h2>


    <p>
        UMIYA TECHNOLOGIES
    </p>


    <p>
        Laptop Parts & Accessories
    </p>


    <p>
        Call us for product availability and enquiries
    </p>


    <a
        class="phone"
        href="tel:9916648774"
    >
        📞 9916648774
    </a>

</section>



<!-- =====================================================
     FOOTER
     ===================================================== -->

<footer>

    © 2026 UMIYA TECHNOLOGIES

    <br>

    Laptop Parts & Accessories

</footer>



<!-- =====================================================
     SEARCH JAVASCRIPT
     ===================================================== -->

<script>

function searchProducts() {

    let input =
        document
        .getElementById("search")
        .value
        .toLowerCase();


    let products =
        document
        .querySelectorAll(".product");


    products.forEach(
        function(product) {

            let name =
                product
                .getAttribute("data-name")
                .toLowerCase();


            let category =
                product
                .getAttribute("data-category")
                .toLowerCase();


            if (
                name.includes(input)
                ||
                category.includes(input)
            ) {

                product.style.display =
                    "block";

            }

            else {

                product.style.display =
                    "none";

            }

        }
    );

}

</script>


</body>

</html>

"""


# =========================================================
# PRODUCT IMAGE ROUTE
# =========================================================

@app.route("/product-image/<filename>")

def product_image(filename):

    folder = os.path.dirname(
        os.path.abspath(__file__)
    )

    return send_from_directory(
        folder,
        filename
    )


# =========================================================
# HOME PAGE
# =========================================================

@app.route("/")

def home():

    return render_template_string(
        HTML,
        products=products
    )


# =========================================================
# START SERVER
# =========================================================

if __name__ == "__main__":

    print()
    print("==========================================")
    print("       UMIYA TECHNOLOGIES")
    print("==========================================")
    print()
    print("Website:")
    print("http://127.0.0.1:5000")
    print()
    print("Contact: 9916648774")
    print()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )

