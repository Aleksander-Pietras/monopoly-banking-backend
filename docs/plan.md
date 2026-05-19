## Design Evolution

The project was initially planned as a Monopoly-style banking system with property tracking.

During development, the scope was refined to focus on a transactional banking backend. Because my primary objective was to create an application that demonstrates core backend concepts such as atomic transactions, data consistency, and authentication; therefore, I ultimately decided to avoid all unnecessary domain complexity.  
As a result, property tracking and other gameplay-oriented systems were removed from scope.

---

# Banking Backend: Plan

> **Project Goal:** A transactional banking backend to model transactional systems involving multiple users, balances, and financial transactions; with support for simulated peer-to-peer banking interactions.

---

### Table of Contents
* [Objectives](#objectives)
* [Target Features](#target-features)
* [Database Schema](#database-schema)
* [Completion Criteria](#completion-criteria)
* [Progress Tracking](#progress-tracking)
* [System Constraints](#system-constraints)
* [Appendix: Design Decisions](#appendix-design-decisions)

---

### Objectives
The aim of the project is to make a transactional banking system that uses databases to store the information.  

**Core Features:**
* **Account Storage:** 
    * Usernames.
    * Hashed passwords.
    * Real-time balances.
* **Transfers:** 
    * Peer-to-Peer payments.
    * Bank-to-Peer payments.

---

### Target Features

```POST /register ```  
Create user with hashed password

```POST /login ```  
Authenticate and return token

```POST /transfer ```  
Move money between users (must be atomic)

*Information on each will written once I learn more and plan these features*

---

### Database Schema
#### Users:
* id
* username (unique)
* password_hash
* balance

#### Transactions:
* id
* sender_id
* receiver_id
* amount
* timestamp

---

### Progress Tracking

- [ ] Phase 1: Core Backend
    - [x] Define database schema
    - [x] Create users table
    - [x] User registration
    - [x] User authentication
    - [ ] Balance management
    - [ ] Atomic peer-to-peer transfers

- [ ] Phase 2: Transaction System
    - [ ] Transaction history table
    - [ ] Store transfer timestamps
    - [ ] Transaction validation
    - [ ] Prevent invalid transfers
    - [ ] Balance consistency checks

- [ ] Phase 3: API & Interface
    - [ ] Improve API structure
    - [ ] Error handling
    - [ ] Simple frontend interface (Tkinter or HTML)
    - [ ] Display balances and transfer history

- [ ] (Extra) Phase 4: Additional Features
    - [ ] Rate limiting
    - [ ] Admin account functionality
    - [ ] Logging and audit improvements

> The project scope may evolve during development; however, the primary objective remains a reliable transactional backend system focused on authentication, data consistency, and atomic financial transfers.

---

### Completion Criteria

#### Phase 1 is complete when:
- users can register and login
- passwords are hashed securely
- authentication is enforced
- money transfers function correctly
- balances remain consistent after transfers

#### Phase 2 is complete when:
- all transfers are logged
- transaction history can be queried
- invalid transfers are rejected
- transaction timestamps are stored correctly

#### Phase 3 is complete when:
- users can interact with the system through a simple interface
- balances and transactions are displayed clearly
- API responses are handled correctly by the frontend

---

### System Constraints
* Users cannot have negative balance
* Transfers must be atomic
* Users can only access their own data

---

### Appendix: Design Decisions


---
[↑ Back to Top](#banking-backend-plan)