# Postman Testing API Report

**Project:** Multi-Tenant POS System (Spring Boot backend)
**Tested with:** Postman
**Base URL:** `http://localhost:5000`
**Collection:** POS System (14 folders, 64 requests)

> This report documents the API test plan built from the Postman collection. The Result column is left empty so the actual outcome of each run can be recorded after testing. Expected status codes are assumptions from the endpoint documents.

## Part 1: Setup and modules 1 to 7

### 1. Purpose and scope

The purpose of this testing is to check that the REST API of the POS backend accepts valid requests, rejects invalid ones, and enforces role-based access with JWT tokens. The collection covers authentication, store setup, product catalogue, orders, staff, inventory, customers, refunds, shifts and analytics.

### 2. Test environment

| Item | Value |
| --- | --- |
| Backend | Spring Boot (REST API) |
| Database | MySQL |
| API tool | Postman |
| Base URL | `http://localhost:5000` |
| Authentication | Bearer JWT token returned by `/auth/login` |
| Content type | `application/json` |

**Postman variables (one token per role)**

| Variable | Used for |
| --- | --- |
| `store_admin_jwt` | Store admin requests (store, branch, category, product, inventory, customer, employee) |
| `store_manager_jwt` | Store manager requests |
| `branch_manager_jwt` | Branch manager requests (branch orders, branch employees) |
| `cashier_jwt` | Cashier requests (orders, refunds, shifts) |
| `jwt2` | A token used for the user list request |

Create each token by logging in with a user of that role, then paste it into the matching Postman variable.

### 3. How the tests are run

1. Start MySQL and the Spring Boot backend on port 5000.
2. Import the collection `POS System` into Postman.
3. Create the role tokens (section 2) from the login request.
4. Run the folders in the order below, either by hand or with the Collection Runner.
5. For each request, note the status code and response, then mark Pass or Fail.
6. Save screenshots of each folder's result in `reports/06-testing/screenshots/`.

**Recommended order:** Auth, Store, Branch, Category, Product, Employee, Inventory, Customer, Shift (start), Orders, Refund, Analytics, Shift (end). Later requests depend on records created by earlier ones.

### 4. Module 1: Auth and user service

Purpose: register users, log in, and read the profile.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.1 | Sign up | POST | `/auth/signup` | None | fullName, email, password, username, role `ROLE_STORE_ADMIN` | 200 or 201, JWT returned | ☐ Pass ☐ Fail |
| 1.2 | Sign in | POST | `/auth/login` | None | email, password | 200, JWT returned | ☐ Pass ☐ Fail |
| 1.3 | Profile | GET | `/api/users/profile` | Store admin | Bearer token | 200, profile with role | ☐ Pass ☐ Fail |
| 1.4 | Get all users | GET | `/users/list` | Admin token | Bearer token | 200, list of users | ☐ Pass ☐ Fail |

Not part of this backend (leftovers from another project, to be removed from the collection): a login OTP request on port 5454, a Keycloak profile request, and an access token from refresh token request.

### 5. Module 2: Store

Purpose: create and manage the store owned by a store admin.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 | Create store | POST | `/api/stores` | Store admin | brand, storeType, contact (address, email, phone), description | 200 or 201, store with status pending | ☐ Pass ☐ Fail |
| 2.2 | Get store by employee | GET | `/api/stores/employee` | Store manager | Bearer token | 200, store | ☐ Pass ☐ Fail |
| 2.3 | Get admin store | GET | `/api/stores/admin` | Store admin | Bearer token | 200, store | ☐ Pass ☐ Fail |
| 2.4 | Update store | PUT | `/api/stores/1` | Store admin | brand, description, storeType, contact | 200, updated store | ☐ Pass ☐ Fail |
| 2.5 | Branch list of store | GET | `/api/branches/store/1` | Store admin | storeId in path | 200, branch list | ☐ Pass ☐ Fail |

Request 2.5 is the same call as 3.3, so it is counted once in the coverage summary.

### 6. Module 3: Branch

Purpose: manage the branches of a store.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3.1 | Create branch | POST | `/api/branches` | Store admin | name, address, workingDays | 200 or 201, branch | ☐ Pass ☐ Fail |
| 3.2 | Get branch employees | GET | `/api/branches/1/employee/list` | Branch manager | branchId in path | 200, employee list | ☐ Pass ☐ Fail |
| 3.3 | Get all branches of a store | GET | `/api/branches/store/1` | Store admin | storeId in path | 200, branch list | ☐ Pass ☐ Fail |
| 3.4 | Get branch by id | GET | `/api/branches/1` | Store admin | id in path | 200, branch | ☐ Pass ☐ Fail |
| 3.5 | Update branch | PUT | `/api/branches/1` | Store admin | name, address, workingDays, openTime, closeTime | 200, updated branch | ☐ Pass ☐ Fail |

### 7. Module 4: Category

Purpose: group the products of a store.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 4.1 | Create category | POST | `/api/categories` | Store admin | storeId, name | 200 or 201, category | ☐ Pass ☐ Fail |
| 4.2 | Get categories by store | GET | `/api/categories/store/1` | Store admin | storeId in path | 200, category list | ☐ Pass ☐ Fail |
| 4.3 | Update category | PUT | `/api/categories/1` | Store admin | name | 200, updated category | ☐ Pass ☐ Fail |

### 8. Module 5: Product

Purpose: create and maintain the product catalogue.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 5.1 | Create product | POST | `/api/products` | Store admin | name, sku, mrp, sellingPrice, brand, categoryId, storeId, image | 200 or 201, product | ☐ Pass ☐ Fail |
| 5.2 | Get products by store | GET | `/api/products/store/1` | Store admin | storeId in path | 200, product list | ☐ Pass ☐ Fail |
| 5.3 | Update product | PATCH | `/api/products/1` | Store admin | name, sku, mrp, sellingPrice, categoryId | 200, updated product | ☐ Pass ☐ Fail |

### 9. Module 6: Orders

Purpose: create POS orders and read them by branch, cashier and date.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 6.1 | Create order | POST | `/api/orders` | Cashier | customer, items (productId, quantity), paymentType `UPI` | 200 or 201, order with total | ☐ Pass ☐ Fail |
| 6.2 | Branch orders | GET | `/api/orders/branch/1` | Branch manager | branchId in path | 200, order list | ☐ Pass ☐ Fail |
| 6.3 | Cashier orders | GET | `/api/orders/cashier/102` | Cashier | cashierId in path | 200, order list | ☐ Pass ☐ Fail |
| 6.4 | Get orders by branch | GET | `/api/orders/branch/1` | Cashier | filters optional | 200, order list | ☐ Pass ☐ Fail |
| 6.5 | Get today's orders | GET | `/api/orders/today/branch/1` | Cashier | branchId in path | 200, today's orders | ☐ Pass ☐ Fail |
| 6.6 | Get recent orders | GET | `/api/orders/recent/1` | Cashier in the collection | branchId in path | 200 for branch manager or admin | ☐ Pass ☐ Fail |

Note: the endpoint document allows request 6.6 only for branch manager and branch admin, but the collection uses a cashier token. Test it with a branch manager token, and check that a cashier gets 403.

### 10. Module 7: Employee

Purpose: add and list staff for a store or branch.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 7.1 | Get store employees | GET | `/api/employees/store/1` | Store admin | storeId in path | 200, employee list | ☐ Pass ☐ Fail |
| 7.2 | Branch employee list | GET | `/api/employees/branch/1` | Store admin | branchId in path | 200, employee list | ☐ Pass ☐ Fail |
| 7.3 | Add store employee | POST | `/api/employees/store/1` | Store admin | email, password, fullName, role `ROLE_BRANCH_MANAGER`, storeId, branchId | 200 or 201, employee | ☐ Pass ☐ Fail |
| 7.4 | Add cashier | POST | `/api/employees/branch/1` | Store admin | email, password, fullName, role `ROLE_BRANCH_CASHIER` | 200 or 201, cashier | ☐ Pass ☐ Fail |

*Part 1 ends here. Modules 8 to 13, the findings and the conclusion follow in Part 2.*
