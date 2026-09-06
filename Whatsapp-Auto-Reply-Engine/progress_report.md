
---

# `progress_report.md`

```markdown
# Progress Report

## WhatsApp Auto-Reply Bot – Automated Reply Engine

**Organization:** NitroXhift Studios Solutions  
**Project:** WhatsApp Auto-Reply Bot  
**Component:** Automated Reply Engine  
**Developer:** Muhammad Jahanzaib Siddiqui  
**Status:** Completed and Tested

---

## 1. Week Objective

The objective of this week's contribution was to design, develop, test, and document the **Automated Reply Engine** component of the NitroXhift Studios Solutions WhatsApp Auto-Reply Bot.

The main goal was to create a system that can receive an incoming user message, identify the most relevant FAQ category, and automatically return the appropriate predefined response.

---

## 2. Work Completed

During this contribution, the following tasks were completed:

- Designed the FAQ dataset structure.
- Created predefined FAQ categories.
- Added keywords for FAQ matching.
- Added predefined responses.
- Implemented text preprocessing.
- Implemented TF-IDF vectorization.
- Implemented Cosine Similarity matching.
- Added a similarity threshold.
- Implemented default responses for unknown questions.
- Developed the core Automated Reply Engine.
- Integrated the engine with FastAPI.
- Created the `/reply` API endpoint.
- Tested the API using FastAPI Swagger UI.
- Created a Jupyter Notebook for demonstration and testing.
- Prepared technical documentation.
- Prepared the project for GitHub submission.

---

## 3. Technologies Used

### Python

Python was used as the primary programming language for implementing the Automated Reply Engine.

### Pandas

Pandas was used to load and process the FAQ dataset stored in CSV format.

### NumPy

NumPy was included for numerical and data-processing operations.

### Scikit-learn

Scikit-learn was used to implement:

- TF-IDF Vectorization
- Cosine Similarity

These techniques provide the NLP-based matching mechanism.

### FastAPI

FastAPI was used to expose the reply engine as a REST API.

### Uvicorn

Uvicorn was used to run the FastAPI application locally.

### Jupyter Notebook

Jupyter Notebook was used for experimentation, testing, and demonstration of the NLP matching process.

---

## 4. Implementation Workflow

The implemented system follows this workflow:

```text
Incoming User Message
          |
          v
      FastAPI API
          |
          v
   Text Preprocessing
          |
          v
      FAQ Dataset
          |
          v
    TF-IDF Conversion
          |
          v
   Cosine Similarity
          |
          v
    Best FAQ Match
          |
          v
   Similarity Threshold
       /        \
      /          \
   Match       No Match
     |             |
     v             v
FAQ Response   Default Response