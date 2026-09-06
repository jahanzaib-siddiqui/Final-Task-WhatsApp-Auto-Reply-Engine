# WhatsApp Auto-Reply Engine

## Automated FAQ Reply Engine – NitroXhift Studios Solutions

An AI/NLP-based automated reply engine developed as an individual Week contribution for the **WhatsApp Auto-Reply Bot** project at **NitroXhift Studios Solutions**.

The system receives a user's message, analyzes its meaning using lightweight Natural Language Processing (NLP), matches it with the most relevant FAQ category, and returns an appropriate predefined response.

---

## 📌 Project Overview

The purpose of this project is to develop the **Automated Reply Engine** component of a WhatsApp Auto-Reply Bot.

Instead of relying only on exact keyword matching, the system uses **TF-IDF vectorization and Cosine Similarity** to identify the most relevant FAQ even when users phrase their questions differently.

For example:

> "What time do you open?"

can be matched with:

> "What are your working hours?"

The system then returns the corresponding FAQ response.

---

## 🎯 Objectives

The main objectives of this project are:

- Build an automated FAQ response engine.
- Process incoming user messages.
- Match messages with predefined FAQ categories.
- Use lightweight NLP for intelligent matching.
- Return the most relevant response.
- Provide a default response for unknown questions.
- Expose the reply engine through a FastAPI endpoint.
- Prepare the system for future WhatsApp API integration.

---

## 🏗️ System Architecture

```text
                    User Message
                         │
                         ▼
                ┌─────────────────┐
                │    FastAPI      │
                │   REST API      │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Processing │
                │  & Cleaning     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  FAQ Dataset    │
                │      CSV        │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │   TF-IDF        │
                │  Vectorization  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Cosine Similarity│
                │    Matching     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Best FAQ Match  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Automated Reply │
                └─────────────────┘
