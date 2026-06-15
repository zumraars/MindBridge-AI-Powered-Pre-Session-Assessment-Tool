# MindBridge — System Architecture

## Overview

MindBridge is designed as a **stateless, session-bound** AI assistant. Every architectural decision flows from one constraint: this system operates in a high-stakes domain (mental health) where AI failure has real human consequences.

---

## System Components

```
User (Client)
     │
     ▼
[Frontend — Netlify]
  - Consent screen (mandatory before any interaction)
  - AI disclosure banner (persistent)
  - Chat interface
     │
     ▼
[Anthropic Claude API]
  - System prompt with strict role boundaries
  - Structured intake flow (guided, not open-ended)
  - Crisis signal detection layer
  - Summary generation
     │
     ▼
[Clinician Output]
  - Printable pre-session summary
  - Severity indicators
  - Crisis flags (if triggered)
```

---

## Key Architectural Decisions

### 1. Stateless by Design
MindBridge stores no personal data between sessions. The session context exists only in the browser during the active conversation and is cleared when the session ends. This was chosen to:
- Minimize KVKK / GDPR data minimization obligations
- Eliminate the need for a database and its associated security surface
- Ensure the system cannot accumulate a psychological profile of a user over time

### 2. System Prompt as Governance Layer
The Claude API system prompt functions as the primary governance mechanism. It defines:
- What the AI is permitted to ask
- What it is explicitly prohibited from doing (diagnosis, treatment recommendations, crisis counseling)
- The required response format for the clinician summary
- How to handle out-of-scope inputs

The system prompt is treated as a policy document, not just a technical configuration.

### 3. Human-in-the-Loop Architecture
MindBridge is not an autonomous system. It has one output: a structured summary for a human clinician. The AI never takes action, never stores data, and never communicates a conclusion to the client directly. Every output is mediated by a professional.

### 4. Crisis Detection as a Hard Boundary
If the system detects high-risk language (explicit self-harm ideation, suicidal statements, expressions of immediate danger), it:
1. Does **not** attempt to provide crisis support (outside its competence boundary)
2. Immediately surfaces a crisis resource message with emergency contacts
3. Flags the session summary with a high-priority crisis indicator
4. Terminates the intake flow

This is a deliberate design choice: the system knows what it cannot do and stops rather than improvising.

### 5. Deployment on Netlify
Chosen for simplicity, HTTPS by default, and no server-side persistence. The frontend communicates directly with the Anthropic API via a serverless function, keeping the architecture minimal.

---

## What This Architecture Prioritizes

| Priority | Implementation |
|---|---|
| User safety | Crisis detection, hard scope limits, no autonomous action |
| Data minimization | Stateless design, no database |
| Transparency | Persistent AI disclosure, consent-first flow |
| Clinician control | All outputs go to the professional, not directly to the client |
| Auditability | Structured output format; every session produces a readable log |
