# Banking Backend: Plan

> **Project Goal:** A transactional banking backend to model transactional systems involving multiple users, balances, and ownership, using Monopoly-style interactions as a test scenario.

Not to support full Monopoly gameplay.  
Nor to simulate Monopoly.

---

### Table of Contents
* [Objectives](#objectives)
* [Target Features](#target-features)
* [Database Schema](#database-schema)
* [Progress Tracking](#progress-tracking)
* [System Constraints](#system-constraints)
* [Appendix: Design Decisions](#appendix-design-decisions)

---

### Objectives
The aim of the project is to make a transactional banking system that uses databases to store the information.  
To bring purpose to this system I will design it, so that, it can support Monopoly-style interactions.  

This project will **not** simulate the game.

**Core Features:**
* **Account Storage:** 
    * Usernames.
    * Hashed passwords.
    * Real-time balances.
* **Transfers:** 
    * Player-to-player payments.
    * Bank-to-player payments. [^1](#1-bank-to-player-payouts)
* **Property Tracking:** [^2](#2-property-sets-and-houses)
    * Buying.
    * Trading between users.
    * Mortgaging assets.

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
Users:
* id
* username (unique)
* password_hash
* balance

Properties:
* id
* name
* value
* owner_id (foreign key -> users.id)

Transactions:
* id
* sender_id
* receiver_id
* amount
* timestamp

---

### Progress Tracking
- [ ] Phase 1: Core Structure
    - [ ] Define Database Schema
    - [ ] "Users"
    - [ ] Authentication
    - [ ] Banking and Balance
    - [ ] Logic for P2P Transfers
- [ ] Phase 2: Properties
    - [ ] "Properties" - rent per house, cost of house
    - [ ] Mortgaging properties
    - [ ] Houses [^3](#3-maximum-house-number)
- [ ] Phase 3: Sessions
    - [ ] Allow for a game session to be created
    - [ ] Reset/Start system
- [ ] (extra) Phase 4: Additional features
    - [ ] Auctions
    - [ ] A communication system to support trades

> Plans might change as the app is designed with inspiration to Monopoly, however supporting full Monopoly-like gameplay is not my primary objective.

Phase 1 is complete when:
- users can register and login
- authentication is enforced
- money can be transferred correctly
- balances remain consistent
Phase 2 is complete when:
- properties can be bought
- users are deducted the correct amount for properties
- test: 2 users cannot own the same property
*Phase 3 and 4 coming in the future*

---

### System Constraints
* Users cannot have negative balance
* Transfers must be atomic
* Users can only access their own data

---

### Appendix: Design Decisions

#### [^1]: Bank-to-player payouts
In the traditional game players gain M200 for passing "GO".  
This will not be implemented as it focuses too much on the game, over my original goal of a backend banking system.

#### [^2]: Property Sets and Houses
Basic owneship and optional attributes (house count, sets) will be tracked.  
The purpose of the App is **not** to fully support the gameplay.

#### [^3]: Maximum House Number
In the traditional game there are 32 houses and 12 hotels.  
I plan to keep the same constraints.

---
[↑ Back to Top](#banking-backend-plan)