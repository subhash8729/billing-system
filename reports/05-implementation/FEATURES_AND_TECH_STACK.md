# Features, Modules and Tech Stack

## Features
POS terminal, product search, cart management, customer management, discounts, order history, bill download, cashier shift summary, refund management, inventory management, sales and report charts, branch dashboard, store dashboard, product management, super admin panel, subscription plans and store onboarding, login and forgot password, dark/light theme, landing page.

## Backend Modules
| Module | Purpose |
| --- | --- |
| Auth and User | Signup, login with JWT, password reset |
| Store and Branch | Store onboarding, approval, branches, employees |
| Product and Category | Product catalogue per store |
| Inventory | Stock per branch |
| Order and Customer | POS sales and customer records |
| Refund | Refunds linked to orders and shifts |
| Shift Report | Cashier shift totals and summaries |
| Analytics | Branch, store and super admin dashboards |
| Subscription and Payment | Plans, subscriptions, Razorpay and Stripe |
| Email | Verification and receipt emails |

## Tech Stack
| Area | Technology |
| --- | --- |
| Backend | Spring Boot, Spring MVC |
| Security | Spring Security, JWT, BCrypt |
| Database | MySQL with JPA / Hibernate |
| Payments | Razorpay, Stripe |
| Build | Maven |
| Frontend | React |
| Testing | Postman, JUnit |

## Code Structure
Package `com.zosh` with layers: controller, service (and impl), repository, modal, payload (DTOs), mapper, domain (enums), event, exception and util.
