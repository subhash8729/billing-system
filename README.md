# Multi-Tenant POS System

---

## 📅 Weekly Plan

> [!IMPORTANT]
> **10-week plan, starting Monday 6 July 2026.** This table is updated every week, and each week has its own report in `reports/04-weekly-progress/`.

| Week | Dates (2026) | Focus | Status today | Report |
| --- | --- | --- | --- | --- |
| **Week 1** | 6 to 12 Jul | Setup, backend upload, roles and module allocation, frontend setup, GitHub training | ✅ Done | [Week 1](reports/04-weekly-progress/week-01/README.md) |
| **Week 2** | 13 to 19 Jul | Design diagrams, SRS, Redux part 2, Branch Manager and Cashier pages | 🔄 In progress |  |
| **Week 3** | 20 to 26 Jul | Frontend auth and super admin | ⏳ Planned |  |
| **Week 4** | 27 Jul to 2 Aug | Frontend store admin | ⏳ Planned |  |
| **Week 5** | 3 to 9 Aug | Frontend branch manager and cashier | ⏳ Planned |  |
| **Week 6** | 10 to 16 Aug | Payments and subscriptions | ⏳ Planned |  |
| **Week 7** | 17 to 23 Aug | Testing | ⏳ Planned |  |
| **Week 8** | 24 to 30 Aug | Code quality and fixes | ⏳ Planned |  |
| **Week 9** | 31 Aug to 6 Sep | Presentation and viva prep | ⏳ Planned |  |
| **Week 10** | 7 to 13 Sep | Final demo and submission | ⏳ Planned |  |

To add a week, copy `reports/04-weekly-progress/WEEK_TEMPLATE.md` to `week-0N/README.md`, fill it in, and link it in this table.

---

A cloud-based Point of Sale system where many stores share one platform. Each store manages its own branches, staff, products, stock, customers and sales, and its data stays separate from other stores.

- **Super admin** approves stores and manages subscription plans.
- **Store admin and manager** set up branches, staff, categories, products and inventory.
- **Branch manager** tracks branch orders, refunds, stock and analytics.
- **Cashier** sells at the POS terminal, handles returns and works in shifts.

## Tech stack

| Part | Technology |
| --- | --- |
| Backend | Spring Boot, Spring Security with JWT, JPA / Hibernate, Maven, Spring Mail |
| Database | MySQL |
| Payments | Razorpay and Stripe |
| Frontend | React 19, Vite 7, Tailwind CSS 4, shadcn/ui (Radix), React Router 7 |
| State and API | Redux Toolkit, Axios |
| Charts and bills | Recharts, @react-pdf/renderer |
| API testing | Postman |

## Repository structure

```
billing-system/
├── pos-backend/          Spring Boot backend (package com.zosh)
├── pos-frontend-vite/    React + Vite frontend
├── reports/              Project reports for submission
│   ├── 01-idea-abstract/
│   ├── 02-srs/
│   ├── 03-design/
│   ├── 04-weekly-progress/
│   ├── 05-implementation/
│   ├── 06-testing/
│   ├── 07-presentation/
│   ├── 08-demo-viva/
│   └── 09-timeline/
└── README.md
```

## Roles

| Role | Area in the app |
| --- | --- |
| `ROLE_ADMIN` (super admin) | `/super-admin` |
| `ROLE_STORE_ADMIN`, `ROLE_STORE_MANAGER` | `/store` |
| `ROLE_BRANCH_ADMIN`, `ROLE_BRANCH_MANAGER` | `/branch` |
| `ROLE_BRANCH_CASHIER` | `/cashier` |
| `ROLE_CUSTOMER` | defined, no dashboard yet |

## Backend

Layers: controller, service (and impl), repository, modal (entities), payload (DTOs), mapper, domain (enums), event, exception and util.

**Modules:** auth, user, store, branch, employee, category, product, inventory, customer, order, refund, shift report, branch analytics, store analytics, admin dashboard, subscription plans, subscriptions, payments (Razorpay and Stripe) and email.

**Run it**

1. Install a JDK and MySQL, and create the database.
2. Put your own database values in `pos-backend/src/main/resources/application.yml`. Do not commit real passwords or keys.
3. Start the server:
   ```bash
   cd pos-backend
   ./mvnw spring-boot:run
   ```
4. The API runs at `http://localhost:5000`, which is the address the frontend expects.

A `docker-compose.yml` is included in `pos-backend/src/main/resources/`.

## Frontend

**Run it**

```bash
cd pos-frontend-vite
npm install
npm run dev
```
It opens at `http://localhost:5173`. The API address is set in `src/utils/api.js`.

**Routing:** after login, `App.jsx` reads the user's role and shows only that role's pages: Super Admin, Store, Branch Manager or Cashier. Each role has its own layout and route file in `src/routes/`.

**Redux Toolkit** (`src/Redux Toolkit/features/`): adminDashboard, auth, branch, branchAnalytics, cart, category, customer, employee, inventory, onboarding, order, payment, product, refund, sale, shiftReport, store, storeAnalytics, subscription, subscriptionPlan, transaction and user. The store file is `globleState.js`.

## Progress

| Area | Status |
| --- | --- |
| Backend source code | Done, in `pos-backend/` |
| Frontend config, API client and utils | Done |
| Redux Toolkit, part 1 (adminDashboard to order) | Done |
| Redux Toolkit, part 2 and `globleState.js` | Pending |
| Branch Manager pages | In progress (Customers page added) |
| Cashier pages | In progress |
| Super Admin, Store and Auth pages | To be added |
| Idea, abstract and feature documents | Done |
| Postman testing report (2 parts) | Done, results to be recorded |
| Commit log and weekly progress | Done, updated as we go |
| UML, ER and architecture diagrams | Made, to be committed |
| SRS (IEEE), presentation, timeline | Pending |

## Reports

- Idea and abstract: `reports/01-idea-abstract/PROJECT_IDEA_AND_ABSTRACT.md`
- Features and tech stack: `reports/05-implementation/FEATURES_AND_TECH_STACK.md`
- Postman API testing: `reports/06-testing/POSTMAN_TESTING_API.md`
- Commit log: `reports/04-weekly-progress/commit_log.csv`
- Weekly reports: `reports/04-weekly-progress/week-01/README.md`
- Timeline: `reports/09-timeline/TIMELINE.md`

## Known issues

- Logout removes the `token` key, but login stores `jwt`, so the session is not cleared.
- The API address is hardcoded in `src/utils/api.js`. It should come from an environment variable.
- `package.json` lists `rechart`, which is a mistake. The real package is `recharts`.
- The Exports and Commissions pages are prototypes with mock data, and Exports is not routed yet.
- Public signup accepts a `role` field, so the backend must reject admin roles.

## Team workflow

- Work on `main` with small, focused commits, and run `git pull --rebase origin main` before every push.
- Commit message format: `type(scope): what changed`, for example `feat(redux): add order slice and thunks`.
- Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.
- Never commit passwords, tokens, `.env` files or `node_modules/`.

## Team

| Member | Work |
| --- | --- |
| subhash8729 | Repository setup, backend, Redux Toolkit part 2 |
| bohra0022 | Backend upload, Redux Toolkit part 1, reports, Postman testing, commit log |
| Teammate | Branch Manager pages |
| Teammate | Cashier pages |

*Update the Team and Progress tables as the work moves forward.*
