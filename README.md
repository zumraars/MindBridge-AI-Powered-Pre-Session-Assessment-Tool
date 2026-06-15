# MindBridge-AI-Powered-Pre-Session-Assessment-Tool# MindBridge — AI-Powered Pre-Session Assessment Tool

> A responsible AI system designed to assist mental health professionals with structured pre-session intake, symptom screening, and crisis detection — built with compliance, transparency, and human oversight at its core.

---

## What is MindBridge?

MindBridge is an AI chatbot that conducts structured pre-session assessments before a client meets with a mental health professional. It collects preliminary information, applies standardized screening scales, detects potential crisis signals, and generates a printable summary for the clinician — reducing session overhead while keeping the human professional fully in control.

The project was built using the **Anthropic Claude API** and deployed via **Netlify**.

---

## Core Features

| Feature | Description |
|---|---|
| Structured intake flow | Guided conversation collecting presenting concerns, mood, sleep, recent events |
| Symptom screening | Applies validated scales (PHQ-9 style severity indicators) |
| Crisis detection | Flags high-risk language patterns; does not proceed autonomously |
| Clinician summary | Generates a printable, structured pre-session report |
| Anonymous design | No persistent personal data storage by default |
| AI disclosure | Transparent disclosure that the user is speaking with an AI system |

---

## Why This Project Exists

Mental health professionals spend significant intake time on structured screening that could be partially systematized — freeing session time for deeper clinical work. MindBridge explores how AI can support (not replace) that process, with strict boundaries on what the AI is and is not permitted to do.

---

## Tech Stack

- **LLM:** Anthropic Claude API (claude-sonnet)
- **Frontend:** HTML / CSS / JavaScript
- **Deployment:** Netlify
- **Data handling:** Stateless by design; no database; session data cleared post-summary

---

## Project Documentation

- [System Architecture](./architecture.md) — How the system is structured and why
- [Compliance Framework](./compliance.md) — KVKK, GDPR, and EU AI Act approach
- [Design Decisions](./design-decisions.md) — Key choices around crisis detection, AI boundaries, and human oversight

---

## Status

Case study / research prototype. Not deployed for clinical use. Built for learning, compliance research, and demonstrating responsible AI design patterns in a high-stakes domain.

---

*Built by Zümra Arslanhan — AI & Machine Learning, Kocaeli University*
