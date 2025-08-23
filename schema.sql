---TEMPORARY TABLE TO STORE SALES DATA
CREATE TABLE temp_orders (
    ID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    Product TEXT,
    QuantityOrdered INTEGER,
    PriceEach REAL,
    OrderDate TEXT,
    PurchaseAddress TEXT,
    Month INTEGER,
    Sales REAL,
    City TEXT,
    Hour INTEGER
);
-----------------------------------------------------

---DIVIDING THE TEMP TABLE DATA INTO SUB TABLES
CREATE TABLE orders (
    OrderID INTEGER PRIMARY KEY,
    OrderDate TEXT,
    Month INTEGER,
    Hour INTEGER
);

CREATE TABLE products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT UNIQUE,
    PriceEach REAL
);

CREATE TABLE customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    PurchaseAddress TEXT,
    City TEXT
);

CREATE TABLE order_items (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    ProductID INTEGER,
    QuantityOrdered INTEGER,
    Sales REAL,
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES products(ProductID)
);

CREATE TABLE order_customers (
    OrderID INTEGER,
    CustomerID INTEGER,
    PRIMARY KEY (OrderID, CustomerID),
    FOREIGN KEY (OrderID) REFERENCES orders(OrderID),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID)
);
--------------------------------------------------------------

-- Inserting DATA into the new tables
INSERT INTO orders (OrderID, OrderDate, Month, Hour)
SELECT DISTINCT OrderID, OrderDate, Month, Hour
FROM temp_orders;

INSERT OR IGNORE INTO products (ProductName, PriceEach)
SELECT DISTINCT Product, PriceEach
FROM temp_orders;

INSERT OR IGNORE INTO customers (PurchaseAddress, City)
SELECT DISTINCT PurchaseAddress, City
FROM temp_orders;

INSERT INTO order_items (OrderID, ProductID, QuantityOrdered, Sales)
SELECT
    t.OrderID,
    p.ProductID,
    t.QuantityOrdered,
    t.Sales
FROM temp_orders t
JOIN products p ON t.Product = p.ProductName;

INSERT INTO order_customers (OrderID, CustomerID)
SELECT DISTINCT
    t.OrderID,
    c.CustomerID
FROM temp_orders t
JOIN customers c
  ON t.PurchaseAddress = c.PurchaseAddress
 AND t.City = c.City;
--- i used 'IGNORE INTO' to prevent sqlite3 from not storing duplicate values as i wanted to view them my self
------------------------------------------------

--- DROPPING THE temp_orders table as its work as a place holder for data is finished
DROP TABLE temp_orders;
-------------------------------------------------------------------------------------

--- now i noticed that the purchase table 'customers' column purchase address contains
-- zip code and state so i decided to move them to seperate table

ALTER TABLE customers ADD COLUMN State TEXT;
ALTER TABLE customers ADD COLUMN ZIP INTEGER;

UPDATE customers SET ZIP = SUBSTR(PurchaseAddress, -5);
UPDATE customers SET State = SUBSTR(PurchaseAddress, LENGTH(PurchaseAddress) - 7, 2);

UPDATE customers
SET PurchaseAddress =  TRIM(REPLACE(PurchaseAddress, ', ' || TRIM(City) || ', ' || TRIM(State) || ' ' || TRIM(ZIP), '') );
-------------------------------------------------------------------------------------

--- then i noticed that the orders table column, orderdate contains time and data in one so i decided to put them into different table
ALTER TABLE orders ADD COLUMN time INTEGER;

UPDATE orders SET time = SUBSTR(OrderDate, -8);
UPDATE orders SET OrderDate = SUBSTR(OrderDate, 1, 10);

---DROPPING TABLE OF month because it serve's no purpose as the data is of january
ALTER TABLE orders DROP COLUMN month;
-------------------------------------------------------------------------------------

---CREATING VIEWS TO better represent data
-- VIEW 1: Full Order Details
CREATE VIEW order_details AS
SELECT
    o.OrderID,
    o.OrderDate,
    o.time AS OrderTime,
    c.PurchaseAddress,
    c.City,
    c.State,
    c.ZIP,
    p.ProductName,
    p.PriceEach,
    oi.QuantityOrdered,
    oi.Sales
FROM order_items oi
JOIN orders o ON oi.OrderID = o.OrderID
JOIN products p ON oi.ProductID = p.ProductID
JOIN order_customers oc ON o.OrderID = oc.OrderID
JOIN customers c ON oc.CustomerID = c.CustomerID;

-- VIEW 2: Sales by City
CREATE VIEW sales_by_city AS
SELECT
    c.City,
    SUM(oi.Sales) AS TotalSales,
    COUNT(DISTINCT o.OrderID) AS TotalOrders
FROM order_items oi
JOIN orders o ON oi.OrderID = o.OrderID
JOIN order_customers oc ON o.OrderID = oc.OrderID
JOIN customers c ON oc.CustomerID = c.CustomerID
GROUP BY c.City
ORDER BY TotalSales DESC;

-- VIEW 3: Sales by Product
CREATE VIEW sales_by_product AS
SELECT
    p.ProductName,
    SUM(oi.QuantityOrdered) AS TotalQuantity,
    SUM(oi.Sales) AS TotalSales
FROM order_items oi
JOIN products p ON oi.ProductID = p.ProductID
GROUP BY p.ProductName
ORDER BY TotalSales DESC;

-- VIEW 4: Sales by Hour of Day
CREATE VIEW sales_by_hour AS
SELECT
    o.time AS OrderTime,
    o.OrderDate AS OrderDate,
    SUM(oi.Sales) AS TotalSales,
    COUNT(DISTINCT o.OrderID) AS TotalOrders
FROM order_items oi
JOIN orders o ON oi.OrderID = o.OrderID
GROUP BY o.OrderDate, o.time
ORDER BY o.OrderDate, o.time;

-- VIEW 5: Sales by State
CREATE VIEW sales_by_state AS
SELECT
    c.State,
    SUM(oi.Sales) AS TotalSales,
    COUNT(DISTINCT oi.OrderID) AS TotalOrders
FROM order_items oi
JOIN order_customers oc ON oi.OrderID = oc.OrderID
JOIN customers c ON oc.CustomerID = c.CustomerID
GROUP BY c.State
ORDER BY TotalSales DESC;

-- VIEW 6: Daily Sales Summary
CREATE VIEW sales_by_day AS
SELECT
    o.OrderDate,
    ROUND(SUM(oi.Sales),2) AS TotalSales,
    COUNT(DISTINCT o.OrderID) AS TotalOrders
FROM order_items oi
JOIN orders o ON oi.OrderID = o.OrderID
GROUP BY o.OrderDate
ORDER BY o.OrderDate ASC;


