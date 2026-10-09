# Project Timeline: Multi-Tenant POS System

The project runs for 10 weeks. Week 1 starts on Monday 5 Oct 2026 (an assumed start date, change it if the official date is different). Weeks 2 to 10 are a suggested plan and are updated as the work moves forward. The editable version, with week dates calculated from the start date, is in `Project_Timeline.xlsx` in this folder.

## Timeline chart

```mermaid
gantt
    title POS System 10-week timeline
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section Done
    Week 1 Setup and documents                :done, w1, 2026-10-05, 7d
    section In progress
    Week 2 Design and SRS                     :active, w2, 2026-10-12, 7d
    section Planned
    Week 3 Frontend auth and super admin      :w3, 2026-10-19, 7d
    Week 4 Frontend store admin               :w4, 2026-10-26, 7d
    Week 5 Frontend branch manager and cashier :w5, 2026-11-02, 7d
    Week 6 Payments and subscriptions         :w6, 2026-11-09, 7d
    Week 7 Testing                            :w7, 2026-11-16, 7d
    Week 8 Code quality and fixes             :w8, 2026-11-23, 7d
    Week 9 Presentation and viva prep         :w9, 2026-11-30, 7d
    Week 10 Final demo and submission         :w10, 2026-12-07, 7d
```

## Week by week

| Week | Dates | Phase | Tasks | Status |
| --- | --- | --- | --- | --- |
| 1 | 5 to 11 Oct | Setup and documents | Team repo and report folders, backend upload, idea and abstract, feature list, frontend config, Redux Toolkit part 1, Postman testing report, commit log | Done |
| 2 | 12 to 18 Oct | Design and SRS | Commit UML and ER diagrams, SRS in IEEE format, Redux part 2 and `globleState.js`, Branch Manager and Cashier pages | In progress |
| 3 | 19 to 25 Oct | Frontend: auth and super admin | Login, forgot and reset password, onboarding, landing page, super admin dashboard, stores, requests, subscription plans | Planned |
| 4 | 26 Oct to 1 Nov | Frontend: store admin | Branches, categories, products, employees, inventory, store dashboard, alerts | Planned |
| 5 | 2 to 8 Nov | Frontend: branch manager and cashier | Branch orders, refunds, inventory, reports, POS screen, returns, order history, customer lookup, shift summary | Planned |
| 6 | 9 to 15 Nov | Payments and subscriptions | Razorpay and Stripe checkout, subscription upgrade, payment status, email receipts | Planned |
| 7 | 16 to 22 Nov | Testing | Run the Postman collection with all role tokens, record results, negative and security tests, unit tests | Planned |
| 8 | 23 to 29 Nov | Code quality and fixes | Axios interceptor, logout fix, API URL in env file, remove console logs, fix security findings, update README | Planned |
| 9 | 30 Nov to 6 Dec | Presentation and viva prep | Report PPT, demo script, viva questions, final documents | Planned |
| 10 | 7 to 13 Dec | Final demo and submission | Full demo run, final checks, final commit log, submission | Planned |

## Completed so far

| Item | Evidence |
| --- | --- |
| Team repo and report folders | `ae83e2e`, `0de054b` |
| Spring Boot backend uploaded | `76f7ec5` |
| Idea, abstract and objectives | `e154036` |
| Features, modules and tech stack | `2016d55` |
| Frontend config, API client and utils | `b4a6f5a` |
| Redux Toolkit part 1 (11 features) | `6891d41` to `5e1ae71` |
| Commit log | `ba6b43c` |
| Postman testing report, 2 parts | `ba99aad`, `c61014c` |
| Branch Manager Customers page | teammate commit |

Made but not committed yet: the 20 UML and ER diagrams, the API test case sheet (96 cases), and the updated README.
In progress: Cashier pages (teammate), Redux Toolkit part 2 and `globleState.js` (Subhash).

## Marks status

| Component | Marks | Status |
| --- | --- | --- |
| Idea & Abstract | 5 | Done |
| SRS / Documentation | 10 | Not started |
| Design (Use-case, Class, ER) | 10 | Diagrams made, commit pending |
| Weekly Progress | 25 | Ongoing, updated every week |
| Implementation & Code Quality | 20 | In progress |
| Testing | 10 | Report written, results to record |
| Presentation | 10 | Not started |
| Demo & Viva | 10 | Not started |
