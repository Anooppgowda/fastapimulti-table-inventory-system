# Advanced E-Commerce Inventory & Order Management System

A production-ready, multi-table backend REST API built using Python's modern **FastAPI** framework, **SQLAlchemy ORM**, and a **MySQL** database. This system implements user registration with native password hashing, product inventory stocking, and a transactional order tracking system that automatically communicates across multiple tables to adjust product stock counts on successful checkouts.

## 📊 Database Schema Architecture

The relational layout consists of three distinct database tables interacting through explicit **Foreign Key Constraints** and business operations:



```text
  ┌─────────────────┐               ┌─────────────────┐               ┌─────────────────┐
  │      users      │               │     orders      │               │    products     │
  ├─────────────────┤               ├─────────────────┤               ├─────────────────┤
  │ id (PK)         │───(1:Many)───>│ id (PK)         │<───(Many:1)───│ id (PK)         │
  │ full_name       │               │ user_id (FK)    │               │ title           │
  │ email (Unique)  │               │ product_id (FK) │               │ price           │
  │ password        │               │ quantity_ordered│               │ stock_quantity  │
  └─────────────────┘               │ status          │               └─────────────────┘
                                    │ order_date      │
                                    └─────────────────┘
