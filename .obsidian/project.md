# 🌐 Web Attacks

## SQL Injection (SQLi)

### 📖 What is SQL Injection?

SQL Injection (SQLi) is a web security vulnerability that allows an attacker to manipulate SQL queries by injecting malicious input into an application's database query.

It occurs when an application inserts user input directly into SQL statements without proper validation or parameterized queries.

---

### 🎯 Target

- Database
- Authentication System
- Sensitive Information

---

### ⚙️ How Does SQL Injection Work?

1. User submits input.
2. The application sends the input to the database.
3. The database executes the SQL query.
4. If input is not handled securely, the query's behavior can change.

---

### 💻 Conceptual Example

#### Vulnerable Query

```sql
SELECT * FROM users
WHERE username = 'USER_INPUT'
AND password = 'USER_INPUT';
```

Instead of treating user input as data, the application inserts it directly into the SQL query.

---

### ⚠️ Possible Impacts

- Authentication Bypass
- Data Disclosure
- Data Modification
- Data Deletion
- Unauthorized Access

---

### 🛡️ Prevention

- Prepared Statements (Parameterized Queries)
- Input Validation
- Least Privilege Principle
- Error Handling
- Regular Security Testing

---

# Cross-Site Scripting (XSS)

## 📖 What is XSS?

Cross-Site Scripting (XSS) is a web security vulnerability that allows malicious JavaScript to execute inside another user's browser.

Unlike SQL Injection, XSS targets the user's browser instead of the database.

---

## 🎯 Target

- Browser
- User Session
- Cookies
- Client-side JavaScript

---

## ⚙️ How Does XSS Work?

1. Attacker submits malicious content.
2. The web application fails to sanitize or encode it.
3. Another user opens the vulnerable page.
4. The browser executes the malicious JavaScript.

---

## 📚 Types of XSS

### 1️⃣ Stored XSS

- Stored permanently on the server.
- Executes whenever users visit the affected page.

Examples:
- Comments
- Forum Posts
- User Profiles

---

### 2️⃣ Reflected XSS

- Returned immediately in the HTTP response.
- Usually delivered through a crafted URL.

Examples:
- Search Parameters
- Error Messages

---

### 3️⃣ DOM-Based XSS

- Exists entirely in client-side JavaScript.
- The vulnerability occurs inside the browser.

---

### ⚠️ Possible Impacts

- Session Hijacking
- Cookie Theft
- Phishing
- User Impersonation
- Website Defacement

---

### 🛡️ Prevention

- Output Encoding
- Input Validation
- HTML Sanitization
- Content Security Policy (CSP)
- HttpOnly Cookies
- Secure Coding Practices

---

# SQL Injection vs XSS

| SQL Injection | XSS |
|---------------|-----|
| Targets Database | Targets Browser |
| Uses SQL | Uses JavaScript |
| Server-side | Client-side |
| Database Compromise | User Compromise |
| Prevented with Prepared Statements | Prevented with Output Encoding & Sanitization |

---

# ✅ Conclusion

Both SQL Injection and XSS are among the most common web application vulnerabilities.

- SQL Injection attacks the **database**.
- XSS attacks the **user's browser**.

Following secure coding practices, validating user input, and implementing modern security mechanisms significantly reduce the risk of these attacks.