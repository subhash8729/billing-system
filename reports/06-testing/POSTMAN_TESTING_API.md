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

## Part 2: Modules 8 to 13, findings and conclusion

### 11. Module 8: Inventory

Purpose: track stock of each product in each branch.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8.1 | Create inventory | POST | `/api/inventories` | Store admin | productId, branchId, quantity | 200 or 201, inventory | ☐ Pass ☐ Fail |
| 8.2 | Get by branch and product | GET | `/api/inventories/branch/1/product/1` | Store admin | ids in path | 200, stock record | ☐ Pass ☐ Fail |
| 8.3 | Get all by branch | GET | `/api/inventories/branch/1` | Store admin | branchId in path | 200, inventory list | ☐ Pass ☐ Fail |
| 8.4 | Update inventory | PUT | `/api/inventories/1` | Store admin | quantity | 200, updated quantity | ☐ Pass ☐ Fail |

### 12. Module 9: Customer

Purpose: store customer details used at checkout.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 9.1 | Create customer | POST | `/api/customers` | Store admin | fullName, phone, email | 200 or 201, customer | ☐ Pass ☐ Fail |
| 9.2 | Get all customers | GET | `/api/customers` | Store admin | none | 200, customer list | ☐ Pass ☐ Fail |
| 9.3 | Search customer | GET | `/api/customers/search?q=` | Store admin | q (search text) | 200, matching customers | ☐ Pass ☐ Fail |
| 9.4 | Delete customer | DELETE | `/api/customers/1` | Store admin | id in path | 200 or 204 | ☐ Pass ☐ Fail |

### 13. Module 10: Refund

Purpose: refund an order and read refunds by cashier, branch and date.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 10.1 | Create refund | POST | `/api/refunds` | Cashier | orderId, reason, amount | 200 or 201, refund | ☐ Pass ☐ Fail |
| 10.2 | Get refunds by cashier | GET | `/api/refunds/cashier/102` | Cashier | cashierId in path | 200, refund list | ☐ Pass ☐ Fail |
| 10.3 | Get refunds by branch | GET | `/api/refunds/branch/1` | Cashier | branchId in path | 200, refund list | ☐ Pass ☐ Fail |
| 10.4 | Get refund by id | GET | `/api/refunds/1` | Cashier | id in path | 200, refund | ☐ Pass ☐ Fail |
| 10.5 | Get all refunds | GET | `/api/refunds` | Cashier | none | 200, refund list | ☐ Pass ☐ Fail |
| 10.6 | Get by cashier and date range | GET | `/api/refunds/cashier/102/range` | Cashier | startDate, endDate | 200, refunds in range | ☐ Pass ☐ Fail |

### 14. Module 11: Shift report

Purpose: track a cashier's working period with sales and refund totals.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 11.1 | Start shift | POST | `/api/shift-reports/start` | Cashier | branch details (branchId) | 200 or 201, shift started | ☐ Pass ☐ Fail |
| 11.2 | Get current shift | GET | `/api/shift-reports/current` | Cashier | none | 200, live shift totals | ☐ Pass ☐ Fail |
| 11.3 | End shift | PATCH | `/api/shift-reports/end` | Cashier | none | 200, final report | ☐ Pass ☐ Fail |
| 11.4 | Find by cashier | GET | `/api/shift-reports/cashier/102` | Cashier | cashierId in path | 200, shift list | ☐ Pass ☐ Fail |
| 11.5 | Find by branch | GET | `/api/shift-reports/branch/1` | Cashier | branchId in path | 200, shift list | ☐ Pass ☐ Fail |
| 11.6 | Find by date | GET | `/api/shift-reports/cashier/102/by-date` | Cashier | date | 200, shift report | ☐ Pass ☐ Fail |

### 15. Module 12: Admin dashboard

Purpose: platform statistics for the super admin.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12.1 | Get summary | GET | `/api/super-admin/dashboard/summary` | Admin token | none | 200, store counts | ☐ Pass ☐ Fail |
| 12.2 | Store registrations, last 7 days | GET | `/api/super-admin/dashboard/store-registrations` | Admin token | none | 200, 7 daily counts | ☐ Pass ☐ Fail |
| 12.3 | Store status distribution | GET | `/api/super-admin/dashboard/store-status-distribution` | Admin token | none | 200, counts by status | ☐ Pass ☐ Fail |

Note: the collection uses a cashier token for these three requests. Run them with an admin token, and check that a cashier gets 403.

### 16. Module 13: Branch analytics

Purpose: sales charts and summaries for a branch.

| # | Request | Method | Endpoint | Role / token | Key request data | Expected | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 13.1 | Daily sales chart | GET | `/api/branch-analytics/daily-sales?branchId=1` | Branch manager | branchId | 200, daily sales | ☐ Pass ☐ Fail |
| 13.2 | Top products | GET | `/api/branch-analytics/top-products?branchId=1` | Branch manager | branchId | 200, top 5 products | ☐ Pass ☐ Fail |
| 13.3 | Top cashiers | GET | `/api/branch-analytics/top-cashiers?branchId=1` | Branch manager | branchId | 200, top 5 cashiers | ☐ Pass ☐ Fail |
| 13.4 | Category sales | GET | `/api/branch-analytics/category-sales?branchId=1&date=` | Branch manager | branchId, date | 200, category sales | ☐ Pass ☐ Fail |
| 13.5 | Today overview | GET | `/api/branch-analytics/today-overview?branchId=1` | Branch manager | branchId | 200, today's totals | ☐ Pass ☐ Fail |
| 13.6 | Payment breakdown | GET | `/api/branch-analytics/payment-breakdown?branchId=1&date=` | Branch manager | branchId, date | 200, cash, card and UPI split | ☐ Pass ☐ Fail |

### 17. Coverage summary

| Module | Requests in collection |
| --- | --- |
| Auth and user service | 4 usable (3 leftovers) |
| Store | 5 (1 duplicate) |
| Branch | 5 |
| Category | 3 |
| Product | 3 |
| Orders | 6 |
| Employee | 4 |
| Inventory | 4 |
| Customer | 4 |
| Refund | 6 |
| Shift report | 6 |
| Admin dashboard | 3 |
| Branch analytics | 6 |
| Empty requests | 2 (to be deleted) |

The collection holds 64 requests. Of these, 2 are empty, 3 belong to another project, and 1 is a duplicate, which leaves 58 usable requests.

### 18. Findings

| # | Area | Finding | Suggested fix | Severity |
| --- | --- | --- | --- | --- |
| 1 | Security | Public signup accepts a `role` field, so a user could try to register as an admin. | Reject or ignore the role on `/auth/signup`. | High |
| 2 | Security | Admin dashboard requests use a cashier token. | Test with an admin token and add a 403 case for cashiers. | High |
| 3 | Authorization | Recent orders uses a cashier token, but only branch manager and branch admin should access it. | Test with a branch manager token and check that a cashier gets 403. | Medium |
| 4 | Collection | Leftover requests from another project (login OTP on port 5454, Keycloak profile, refresh token). | Delete them. | Medium |
| 5 | API | Shift start sends a branch JSON body in Postman, but the frontend sends `?branchId=`. | Check the controller and align both. | Medium |
| 6 | API | Refund date range uses `startDate` and `endDate` in Postman, but `from` and `to` in the frontend. | Check the controller and align both. | Medium |
| 7 | Orders | The frontend cart adds 18% tax, while the order request has no tax field. | Confirm the saved total matches the bill. | Medium |
| 8 | Collection | Several GET requests carry a body, and daily sales sends an extra `branchId` header. | Remove them. | Low |
| 9 | Collection | Ids such as 52, 102 and 203 are hardcoded, and a folder is named `AminDashboard`. | Use collection variables and fix the name. | Low |
| 10 | Collection | No request has test scripts or saved example responses. | Add `pm.test` checks for status and key fields. | Medium |

### 19. Endpoints not yet in the collection

Forgot password and reset password, get all stores and store moderation (approve or decline), get product by id, product search and delete, delete for category, branch, inventory, order and refund, customer get by id and update, employee update and delete, store analytics, subscription plans, subscriptions and payments.

### 20. Negative and security tests to add

Duplicate email on signup, invalid email or short password, wrong password on login, protected endpoint without a token, cashier creating a product or category, order with more quantity than stock, refund above the order total, starting a second shift while one is active, and a request for an id that does not exist.

### 21. Evidence

Save the Postman run results and screenshots under `reports/06-testing/screenshots/`, one image per folder. The full test case table with 96 cases is kept in `POS_Backend_Test_Cases.xlsx`.

### 22. Conclusion

The Postman collection gives good coverage of the core flows: authentication, store setup, catalogue, orders, refunds, shifts and branch analytics. Before final submission, the team should fix the security findings (1 to 3), remove the leftover requests, add tests to every request, and cover the endpoints listed in section 19. After the runs, the Result column of each table should be filled in, and the pass count recorded here.
