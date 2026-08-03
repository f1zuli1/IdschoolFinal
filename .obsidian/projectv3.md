# 🌐 Cross-Site Scripting (XSS)

## 📖 What is Cross-Site Scripting (XSS)?

Cross-Site Scripting (XSS) is one of the most common client-side web application vulnerabilities. It occurs when an application allows untrusted user input to be interpreted as JavaScript by a user's browser.

Unlike SQL Injection, which targets the database, XSS targets the **browser** and the users interacting with the vulnerable website.

---

## 🎯 Main Targets

Cross-Site Scripting primarily targets the **client-side** of a web application.

Common targets include:

- User Sessions
- Cookies
- Web Browsers
- User Accounts
- Sensitive User Information
- Client-side JavaScript

---

## ⚙️ How Cross-Site Scripting Works

A typical XSS attack follows these steps:

1. An attacker submits malicious content to a web application.
2. The application stores or reflects the content without proper validation.
3. Another user visits the vulnerable page.
4. The browser executes the malicious JavaScript as if it were trusted.

Flow:

Attacker → Web Application → Victim Browser → JavaScript Executes

---

## 📍 Where Can XSS Occur?

Cross-Site Scripting vulnerabilities are commonly found in:

- Search Boxes
- Comment Sections
- User Profiles
- Contact Forms
- Chat Applications
- URL Parameters
- Review Systems
- Message Boards

Any feature that displays user input without proper protection may become vulnerable.

---

## 🧪 Types of Cross-Site Scripting

### Stored XSS

The malicious script is permanently stored on the server, such as in comments or user profiles. Every user who visits the affected page executes the script.

### Reflected XSS

The malicious script is reflected immediately in the server's response. It usually requires the victim to click a specially crafted link.

### DOM-Based XSS

The vulnerability exists entirely within client-side JavaScript. The browser modifies the Document Object Model (DOM) using untrusted data, allowing malicious code to execute.

---

## ⚠️ Possible Impacts

A successful XSS attack may allow an attacker to:

- Steal Session Cookies
- Hijack User Sessions
- Impersonate Users
- Redirect Users to Fake Websites
- Display Fake Login Pages
- Modify Website Content
- Execute Actions on Behalf of the User

---

## 🛡️ Prevention

The best way to prevent Cross-Site Scripting is to ensure that user input is never executed as JavaScript.

Recommended security measures include:

- Output Encoding
- Input Validation
- HTML Sanitization
- Content Security Policy (CSP)
- HttpOnly Cookies
- Secure Coding Practices
- Regular Security Testing