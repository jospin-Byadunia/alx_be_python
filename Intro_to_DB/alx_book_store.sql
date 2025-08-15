CREATE TABLE Books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(130) NOT NULL,
    author_id INT REFERENCES Authors(author_id),
    price DOUBLE NOT NULL,
    publication_date DATE
);

CREATE TABLE Authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(215) NOT NULL,
);

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) UNIQUE NOT NULL
);

CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES Customers(customer_id),
    order_date DATE NOT NULL,
);
CREATE TABLE Order_Details(
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES Orders(order_id),
    book_id INT REFERENCES Books(book_id),
    quantity DOUBLE,
);