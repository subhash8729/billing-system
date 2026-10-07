# Multi-Tenant POS System: Idea and Abstract

## Idea
Small and medium retailers often use separate, disconnected billing tools for each shop. This project is a cloud-based, multi-tenant Point of Sale system where many stores can register on one platform. Each store manages its own branches, products, staff, customers and sales, and its data stays isolated from other stores.

## Abstract
The system lets a store owner register a store, choose a subscription plan, and set up branches and employees. Cashiers use a POS terminal to search products, build a cart, apply discounts, take payment by cash, card or UPI, and generate a bill. Managers track inventory and shift summaries, process refunds, and view sales analytics at branch and store level. A super admin approves stores, manages subscription plans, and monitors the whole platform. The backend is built with Spring Boot, secured with Spring Security and JWT, and stores data in MySQL. Online subscription payments are supported through Razorpay and Stripe.

## Problem Statement
- Manual or disconnected billing causes errors and slow checkout.
- Owners cannot see sales and stock across branches in one place.
- Small stores cannot afford a custom-built system.

## Objectives
- Provide a fast, simple checkout for cashiers.
- Give owners real-time stock, sales and shift reports.
- Support many stores on one platform with role-based access.
- Offer paid plans that limit branches, users and features.

## Users and Roles
Super Admin, Store Admin, Store Manager, Branch Admin, Branch Manager, Cashier.
