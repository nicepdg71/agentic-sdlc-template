# System Architecture

## Architecture Overview
High-level description of system components, communication protocols, and deployment topology.

## Component Diagram
```mermaid
graph TD
    Client --> API Gateway
    API Gateway --> ServiceA
    API Gateway --> ServiceB
    ServiceA --> Database[(Primary DB)]
```
