# Technical Documentation
## WhatsApp Auto-Reply Bot – Automated Reply Engine

**Organization:** NitroXhift Studios Solutions  
**Project:** WhatsApp Auto-Reply Bot  
**Component:** Automated Reply Engine  
**Developer:** Muhammad Jahanzaib Siddiqui

---

## 1. Introduction

The WhatsApp Auto-Reply Engine is a Python-based automated response system developed as an individual Week contribution to the WhatsApp Auto-Reply Bot project at NitroXhift Studios Solutions.

The purpose of the engine is to receive a user's message, analyze the message using lightweight Natural Language Processing (NLP), identify the most relevant FAQ category, and return the corresponding predefined response.

The system is designed as the core response engine that can later be connected to a WhatsApp Business API or Twilio-based messaging system.

---

## 2. Objective

The main objective of this project is to develop the **Automated Reply Engine** component of the WhatsApp Auto-Reply Bot.

The system should:

- Receive an incoming user message.
- Process and clean the message.
- Compare the message with predefined FAQ information.
- Identify the most relevant FAQ category.
- Return the appropriate automated response.
- Handle questions that do not match the available FAQs.
- Provide an API interface for future messaging-platform integration.

---

## 3. Scope

The current implementation focuses on the core message-matching and automated-response functionality.

The project includes:

- FAQ dataset
- Text preprocessing
- NLP-based message matching
- TF-IDF vectorization
- Cosine Similarity
- Similarity threshold
- Automated FAQ responses
- Default response handling
- FastAPI REST API
- Jupyter Notebook demonstration

The current version does not directly connect to the production WhatsApp Business API.

The FastAPI endpoint provides the backend interface that can be integrated with WhatsApp Business API or Twilio in a future version.

---

## 4. System Architecture

The system follows this processing workflow:

```text
                User Message
                     |
                     v
              +--------------+
              |   FastAPI    |
              |   REST API   |
              +------+-------+
                     |
                     v
            +------------------+
            | Text Processing  |
            |  & Cleaning      |
            +--------+---------+
                     |
                     v
            +------------------+
            |   FAQ Dataset    |
            |      CSV         |
            +--------+---------+
                     |
                     v
            +------------------+
            | TF-IDF           |
            | Vectorization    |
            +--------+---------+
                     |
                     v
            +------------------+
            | Cosine Similarity|
            |    Matching      |
            +--------+---------+
                     |
                     v
            +------------------+
            | Best FAQ Match   |
            +--------+---------+
                     |
                     v
             Similarity Check
                 /       \
                /         \
             Match       No Match
               |             |
               v             v
         FAQ Response    Default Response