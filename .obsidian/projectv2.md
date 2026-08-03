# 💉 SQL Injection (SQLi)

## 📖 What is SQL Injection?

SQL Injection (SQLi) is a web application vulnerability that occurs when an application inserts user input directly into an SQL query without proper validation. This allows the structure of the SQL query to be modified, causing the database to execute unintended commands.

SQL Injection mainly targets the database and can affect the confidentiality, integrity, and availability of stored data.

---

## 🎯 Main Targets

SQL Injection primarily targets the **database** behind a web application.

Common targets include:

- User Accounts
- Login Systems
- Customer Information
- Payment Records
- Administrator Accounts
- Sensitive Business Data

---

## ⚙️ How SQL Injection Works

A typical SQL Injection attack follows these steps:

1. A user submits data through a form, search box, or URL.
2. The application builds an SQL query using the provided input.
3. The database executes the generated SQL query.
4. If the input is not properly handled, the query's logic may change and perform unintended actions.

---

## 📍 Where Can SQL Injection Occur?

SQL Injection vulnerabilities are commonly found in:

- Login Forms
- Search Boxes
- URL Parameters
- Product Filters
- Contact Forms
- Cookies
- HTTP Headers
- API Requests

Any place where user input is processed by a database may become vulnerable if secure coding practices are not followed.

---

## 🧪 Types of SQL Injection

### Error-Based SQL Injection

Database error messages reveal useful information about the database structure.

### Union-Based SQL Injection

Uses the SQL `UNION` operator to combine additional query results with the original query.

### Blind SQL Injection

The application does not display database results directly. Information is inferred from the application's behavior.

### Time-Based Blind SQL Injection

Relies on differences in response time to determine whether injected conditions are true.

### Out-of-Band SQL Injection

Uses an alternative communication channel when normal responses cannot be used.

---

## ⚠️ Possible Impacts

A successful SQL Injection attack may allow an attacker to:

- Read confidential information
- Bypass authentication
- Modify existing records
- Delete important data
- Access administrator accounts
- Compromise the entire database

---

## 🛡️ Prevention

The best way to prevent SQL Injection is to separate user input from SQL code.

Recommended security measures include:

- Prepared Statements
- Parameterized Queries
- Input Validation
- Least Privilege Principle
- Secure Error Handling
- Regular Security Testing