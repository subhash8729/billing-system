# Week 1 Report: Setup, Backend and Role Allocation

**Week:** 1 (planned 6 to 12 Jul 2026)
**Focus:** repository and folder structure, backend upload, roles and module allocation, frontend setup, GitHub training for the team
**Status:** Done

This is the Week 1 report. The main project README links to every weekly report, and each week gets its own folder here: `reports/04-weekly-progress/week-XX/`.

## 1. Goals and outcome

| Goal | Outcome |
| --- | --- |
| Create the team repository and report folders | Done |
| Upload the Spring Boot backend | Done |
| Decide roles and allocate modules to team members | Done |
| Set up the React + Vite frontend and Redux Toolkit | Done (part 1), part 2 in progress |
| Write the idea, abstract and feature list | Done |
| Teach GitHub to the team | Done |
| Test the API with Postman | Test report written, results to record |

## 2. Repository folder structure

```
billing-system/
├── pos-backend/              Spring Boot backend (package com.zosh)
├── pos-frontend-vite/        React + Vite frontend
├── reports/                  One folder per marks component
│   ├── 01-idea-abstract/
│   ├── 02-srs/
│   ├── 03-design/
│   ├── 04-weekly-progress/   Weekly reports (week-01, week-02, ...)
│   ├── 05-implementation/
│   ├── 06-testing/
│   ├── 07-presentation/
│   ├── 08-demo-viva/
│   └── 09-timeline/
└── README.md                 Main README, updated every week
```

## 3. Backend added

The full Spring Boot backend was added to `pos-backend/`. It runs on `http://localhost:5000` and uses MySQL.

**Package layout (`com.zosh`):** configurations, controller, domain (enums), event, exception, mapper, messaging, modal (entities), payload (request, response and DTOs), repository, service (with `impl` and `gateway`), util.

**Backend models (entities)**

| Area | Models |
| --- | --- |
| Users and access | User, PasswordResetToken |
| Store setup | Store, StoreContact, Branch, Category |
| Catalogue and stock | Product, Inventory |
| Sales | Customer, Order, OrderItem, Refund |
| Cashier work | ShiftReport, PaymentSummary |
| Subscriptions and payments | SubscriptionPlan, Subscription, PaymentOrder, Payment |

**Enums (domain):** UserRole, StoreStatus, OrderStatus, PaymentType, PaymentStatus, PaymentOrderStatus, PaymentGateway, BillingCycle, SubscriptionStatus.

**Modules:** auth, user, store, branch, employee, category, product, inventory, customer, order, refund, shift report, branch analytics, store analytics, admin dashboard, subscription plans, subscriptions, payments (Razorpay and Stripe) and email.

## 4. Roles

| Role | Area in the app | What the role does |
| --- | --- | --- |
| `ROLE_ADMIN` (super admin) | `/super-admin` | Approves stores, manages subscription plans, sees the platform dashboard |
| `ROLE_STORE_ADMIN` | `/store` | Creates the store, subscribes to a plan, manages branches, staff, products, inventory and analytics |
| `ROLE_STORE_MANAGER` | `/store` | Manages staff, categories, products and inventory |
| `ROLE_BRANCH_ADMIN` | `/branch` | Runs a branch: orders, refunds, inventory, employees, reports |
| `ROLE_BRANCH_MANAGER` | `/branch` | Same branch dashboard as the branch admin |
| `ROLE_BRANCH_CASHIER` | `/cashier` | Sells at the POS terminal, handles returns, views orders and customers, works in shifts |
| `ROLE_CUSTOMER` | none yet | Defined in the code, no dashboard yet |

After login, `App.jsx` reads the role and shows only that role's pages. Every other path shows a "page not found" screen.

## 5. Module allocation

| Module | Owner (GitHub) | Status |
| --- | --- | --- |
| Repository setup, frontend folder structure | subhash8729 (Subhash Dhaka) | Done |
| Backend upload, Redux Toolkit part 1, reports, Postman testing, commit log, timeline | bohra0022 | Done |
| Branch Manager pages (customers, dashboard and cashier performance, employees, inventory) | choubisavishvas-web | In progress |
| Cashier pages (sidebar pages, cart, components) | iamvkb7 | In progress |
| Onboarding page (owner details) | tanyasingh077 | In progress |
| Redux Toolkit part 2 and `globleState.js` | To be confirmed | Pending |
| Super Admin pages, Store admin pages | To be confirmed | Not started |

The Branch Manager, Cashier and Onboarding teammates work inside `pos-frontend-vite/src/pages/`, each in their own folder, so their changes do not collide.

## 6. Frontend details

**Stack:** React 19, Vite 7, Tailwind CSS 4, shadcn/ui (Radix), React Router 7, Redux Toolkit, Axios, Recharts, @react-pdf/renderer.

**Source layout (`pos-frontend-vite/src/`)**

| Folder | Purpose |
| --- | --- |
| `pages/` | Screens, one folder per role: `SuperAdminDashboard`, `store`, `Branch Manager`, `cashier`, plus `auth`, `common`, `onboarding` |
| `routes/` | One route file per role (`SuperAdminRoutes`, `StoreRoutes`, `BranchManagerRoutes`, `CashierRoutes`, `AuthRoutes`) |
| `Redux Toolkit/` | `globleState.js` and `features/<name>/` with a slice and thunks per feature |
| `components/` | Shared UI components |
| `utils/` | `api.js` (Axios client), date, payment and role helpers |
| `context/`, `hooks/`, `lib/`, `assets/` | Shared context, hooks, helpers and images |

**Redux Toolkit features (22):** adminDashboard, auth, branch, branchAnalytics, cart, category, customer, employee, inventory, onboarding, order, payment, product, refund, sale, shiftReport, store, storeAnalytics, subscription, subscriptionPlan, transaction, user.

**Conventions the team follows**
- A feature folder holds `<name>Slice.js` and `<name>Thunks.js`.
- Thunks call the API through `utils/api.js` and send the JWT as a Bearer token.
- Each role keeps its screens in its own `pages/` folder and its URLs in its own route file.
- Commit messages follow `type(scope): what changed`.

**Run it:** `cd pos-frontend-vite`, then `npm install`, then `npm run dev`. It opens at `http://localhost:5173`.

## 7. UI design (Figma)

| Item | Detail |
| --- | --- |
| Figma file | Add the link here |
| Screens designed | List the screens, for example login, POS terminal, dashboards |
| Theme | Light and dark mode through `next-themes` |
| Component library | shadcn/ui on Tailwind CSS |

Each page follows its Figma frame. If a page differs from the design, note it here.

## 8. GitHub training for the team

Everyone on the team was shown how to use GitHub for the shared repo. Topics covered:

| Topic | What was covered |
| --- | --- |
| Clone and remotes | Clone the repo, `origin` is the team repo |
| Daily flow | Pull, change, add, commit, push |
| Commit messages | `feat`, `fix`, `docs`, `chore`, `refactor`, `test` with a short description |
| Access | Collaborator invitation and the personal access token used as the password |
| Staying in sync | `git pull --rebase origin main` before every push |
| Safety | No passwords, tokens or `.env` files in commits, and no `git init` in the home folder |
| Fixing errors | 403, `rejected ... fetch first`, `divergent branches` |

**Cheat sheet**
```bash
git clone https://github.com/subhash8729/billing-system.git
cd billing-system
git pull --rebase origin main        # get the latest work first
git status                           # see what changed
git add <folder or file>             # stage only your own work
git commit -m "feat(scope): what changed"
git push origin main
git log --oneline | head             # check your commits
```

| Problem | Fix |
| --- | --- |
| `403 Permission denied` | Accept the collaborator invitation and use a classic token with the `repo` permission |
| `rejected ... fetch first` | Run `git pull --rebase origin main`, then push again |
| `divergent branches` | Pull with `--rebase`, or reset to `origin/main` if you have no local commits |
| Commits not showing | Run `git log` to check, and run `git push` since commits stay local until pushed |
| Wrong author on commits | Set `user.name` and `user.email` (an email verified on GitHub) before the first commit. Never force-push `main` without telling the team |

## 9. Commits in Week 1

The commit hashes below are the current ones. They changed once when the history was rewritten to fix the author emails. The full list, with authors and dates, is in `reports/04-weekly-progress/commit_log.csv`, which `make_commit_log.py` builds from Git.

**bohra0022**

| Commit | Message |
| --- | --- |
| see `commit_log.csv` | docs: add project idea, abstract and objectives |
| `13dc390` | docs: add features, modules and tech stack |
| `4584088`, `80c721c` | Reports folder with commit log, and folder structure for submission |
| `ef6144e` | backend added 2nd time |
| `dbcae3a` | chore: set up React + Vite config, API client and shared utils |
| `7ab1196`, `0abb5fc`, `06b282a`, `09a4708`, `26e7b01`, `8d7cd95`, `b04b449`, `ed775da`, `e426064`, `c579b5a`, `9809d35` | 11 Redux Toolkit feature commits (adminDashboard, auth, branch, branchAnalytics, cart, category, customer, employee, inventory, onboarding, order) |
| `046f470`, `67e0b4c`, `8360f7e` | Commit log updates |
| `9e2ca1a`, `8172cb7` | Postman API testing report, parts 1 and 2 |
| `11645a2` | docs: add UML, ER and architecture diagrams to design report |
| `b0ebffe` | docs: update README with project overview, structure and progress |
| `75398a4`, `28069ac` | 10-week timeline with Gantt chart, and timeline and marks tracker sheet |
| `4430a3c`, `7ce4830`, `cdd3a24`, `b4bee2d`, `65daf38` | Week 1 report, weekly template, README weekly plan |

**Team**

| Commit | Author | Message |
| --- | --- | --- |
| `ddf392b`, `751e82d` | subhash8729 | Frontend folder structure |
| `3197520`, `bb95311`, `db9c60b` | choubisavishvas-web | Branch Manager customer pages, dashboard and cashier performance |
| `3d1187e`, `deff443`, `655d718`, `2d48633`, `7974ef5`, `7faddd4`, `76a311a` | iamvkb7 | Cashier sidebar pages, cart and components |
| `7307504` | tanyasingh077 | Onboarding owner details page |

## 10. Problems faced and fixes

| Problem | Fix |
| --- | --- |
| Pushes to the team repo returned 403 | Accepted the collaborator invitation and used a classic token |
| Local `main` and GitHub `main` diverged after the repo was rebuilt | Reset the local `main` to `origin/main`, then pulled with `--rebase` |
| A Git repo was created by mistake in the home folder | Moved it out of the way and worked only inside the cloned repo |
| Helper commands failed silently in a new terminal window | Defined the paths and helper function again in the same command block |
| Commits had a wrong author email and did not show under the right GitHub account | Rewrote the history with the correct email and force-pushed. All commit hashes changed, so the team reset their local copies to `origin/main` and the commit log was rebuilt |

## 11. Plan for Week 2

- Commit the UML and ER diagrams to `reports/03-design/`.
- Write the SRS in IEEE format.
- Finish Redux Toolkit part 2 and `globleState.js`.
- Push the Branch Manager and Cashier pages.
- Record the Postman test results.
