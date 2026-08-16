# Structured AI JSON Extractor

An AI-powered structured-output system that converts unstructured customer support messages into **clean, predictable, machine-readable JSON**.

The project demonstrates how prompt engineering, schema design, edge-case testing, and programmatic validation can be combined to make LLM outputs more reliable for real-world applications.

---

## 🎯 Project Objective

Large Language Models are excellent at generating natural language, but real applications often require structured data that can be directly consumed by software.

For example, instead of returning:

> "The customer appears to have a payment issue and needs urgent assistance."

the system produces:

```json
{
  "customer_name": "Ahmed Khan",
  "email": "ahmed.khan@example.com",
  "issue_type": "Payment Issue",
  "urgency": "high",
  "summary": "Customer was charged twice for the same order."
}
```

This makes the AI response easier to parse, validate, store, and use inside an application.

---

# 🚀 Features

- Structured JSON output generation
- Custom JSON schema design
- Strict output-format prompting
- Customer support message extraction
- Issue classification
- Urgency classification
- Missing information handling
- Ambiguous information handling
- Tricky-input testing
- Prompt improvement based on failures
- Programmatic JSON validation
- Schema validation
- Original vs improved prompt comparison

---

# 🧠 JSON Schema

The system extracts five fields:

```json
{
  "customer_name": "string or null",
  "email": "string or null",
  "issue_type": "string",
  "urgency": "low | medium | high",
  "summary": "string"
}
```

### Fields

| Field | Description |
|---|---|
| `customer_name` | Customer's name or `null` if unavailable/ambiguous |
| `email` | Customer's email or `null` if unavailable/ambiguous |
| `issue_type` | Predefined category describing the primary issue |
| `urgency` | `low`, `medium`, or `high` |
| `summary` | Concise summary of the customer's problem |

---

# 📋 Supported Issue Types

The system supports the following issue categories:

```text
Payment Issue
Shipping Issue
Damaged Product
Account Issue
Technical Issue
Refund Request
Product Inquiry
Other
```

---

# 🏗️ Project Workflow

The complete workflow is:

```text
Customer Support Message
          │
          ▼
    Structured Prompt
          │
          ▼
       LLM Model
          │
          ▼
      JSON Response
          │
          ▼
     JSON Parsing
          │
          ▼
    Schema Validation
          │
          ▼
 Application-Ready Data
```

---

# 📁 Project Structure

```text
Structured-AI-JSON-Extractor/
│
├── inputs/
│   └── tricky_input.md
│
├── prompts/
│   ├── json_extraction_prompt.md
│   └── improved_prompt.md
│
├── results/
│   ├── test_results.md
│   └── tricky_result.md
│
├── validator.py
├── comparison.md
├── conclusion.md
└── README.md
```

---

# 🧪 Testing

Five different customer support messages were used for the initial testing phase.

The messages represented different scenarios:

1. Payment issue
2. Damaged product
3. Account issue
4. Shipping issue
5. Product inquiry

Each response was checked for:

- Valid JSON syntax
- Required fields
- Allowed issue types
- Allowed urgency values
- Correct data types
- Proper handling of missing information

### Test Result

```text
5/5 tests passed
```

All five responses successfully followed the required JSON structure.

---

# 🔥 Deliberate Break Test

After testing normal inputs, a deliberately messy customer message was introduced.

The input contained:

- Multiple possible names
- Multiple possible email addresses
- Multiple customer issues
- Strong urgency indicators
- Emotional language
- Excessive punctuation
- A refund request

Example:

```text
URGENT!!! Hey, I'm John... or maybe Jonathan 😂.
Someone charged my card THREE times for the same order!!!
I think my email was john123@gmail.com...
wait, it might be john@gmail.com.
Anyway FIX THIS NOW!!!
Also, my package hasn't arrived and I think the product might be damaged.
I need my money back ASAP!!!
```

This test was designed to determine how the model behaves when information is ambiguous and multiple issues are present.

---

# 🛠️ Prompt Improvement

The tricky-input test revealed that the original prompt needed more explicit rules for edge cases.

The improved prompt introduced rules for:

### Ambiguous Information

If multiple possible values exist and the correct value cannot be determined confidently:

```json
"customer_name": null
```

or:

```json
"email": null
```

The model is instructed **not to guess**.

### Multiple Issues

If a customer reports multiple problems:

1. Identify the primary issue.
2. Use that issue as `issue_type`.
3. Mention important secondary issues inside `summary`.

This provides predictable behavior while keeping the existing schema.

---

# 🔍 Original vs Improved Prompt

| Criteria | Original | Improved |
|---|---|---|
| Valid JSON | ✅ | ✅ |
| Schema compliance | ✅ | ✅ |
| Missing information | ✅ | ✅ |
| Ambiguous name handling | ✅ | ✅ |
| Ambiguous email handling | ✅ | ✅ |
| Multiple issue handling | Limited | Improved |
| Primary issue selection | Basic | Explicit |
| Secondary issue handling | Basic | Explicit |
| Urgency rules | Basic | More explicit |
| Predictability | Good | Better |

The improved prompt did not change the fundamental JSON schema.

Instead, it added clearer behavioral rules for difficult inputs.

---

# ✅ Programmatic Validation

The project includes `validator.py` to verify that model responses are actually usable by software.

The validator uses Python's built-in JSON parser:

```python
json.loads(response)
```

It also validates:

- JSON structure
- Required fields
- Issue categories
- Urgency values
- Data types
- Nullable fields

This is important because an LLM response can be valid JSON while still violating an application's expected schema.

---

# 💡 Why Structured Outputs Matter

In a real AI application, the LLM output may be passed directly into another system:

```text
LLM
 ↓
JSON
 ↓
Backend API
 ↓
Database
 ↓
Business Logic
```

For example, a customer support system could use the extracted data to:

- Automatically categorize support tickets.
- Prioritize urgent requests.
- Store customer information.
- Route tickets to the correct department.
- Trigger automated workflows.
- Generate support dashboards.

This makes structured outputs highly useful for production AI systems.

---

# 🧩 Example Use Case

A customer sends:

```text
Hi, I'm Ahmed. I was charged twice for my order.
Please fix this immediately.
My email is ahmed@example.com.
```

The system can convert it into:

```json
{
  "customer_name": "Ahmed",
  "email": "ahmed@example.com",
  "issue_type": "Payment Issue",
  "urgency": "high",
  "summary": "Customer was charged twice for an order and is requesting immediate assistance."
}
```

The backend can then process this data without needing to interpret a natural-language response.

---

# 📊 Results

### Normal Test Cases

```text
Tests performed: 5
Tests passed:    5
Success rate:    100%
```

### Tricky Test

```text
Original Prompt:
Valid JSON + reasonable handling

Improved Prompt:
Valid JSON + more explicit edge-case handling
```

The experiment demonstrated that prompt quality affects the predictability of model behavior, particularly when inputs contain ambiguity or multiple issues.

---

# 🧠 Key Learnings

Through this project, I learned:

- How to design an output schema for an LLM.
- How to constrain LLM responses using prompts.
- Why predictable output is important for AI applications.
- How to handle missing and ambiguous information.
- How to test LLMs with normal and edge-case inputs.
- How to validate JSON responses programmatically.
- Why valid JSON is different from valid application data.
- How to improve prompts based on observed model behavior.
- How structured outputs can connect LLMs with backend systems.

---

# 🔮 Future Improvements

This project can be extended into a complete AI-powered customer support pipeline.

Possible improvements include:

- Direct integration with Gemini/OpenAI APIs.
- Pydantic-based schema validation.
- Automatic retry when model output is invalid.
- Function calling / native structured outputs.
- REST API using FastAPI.
- Database integration.
- Automatic support-ticket creation.
- Multi-label issue classification.
- Confidence scoring.
- Human-in-the-loop review.
- Integration with CRM systems.
- Production deployment.

---

# 🏁 Conclusion

This project demonstrates that building reliable AI applications requires more than simply asking an LLM a question.

A production-oriented AI workflow should define:

```text
Schema
   +
Prompt Rules
   +
Edge-Case Handling
   +
Validation
   =
Reliable Structured AI Output
```

The experiment successfully transformed unstructured customer messages into structured JSON and demonstrated how explicit prompt rules can improve model behavior when dealing with ambiguous and messy real-world inputs.

The project provides a foundation for building larger AI systems where LLM outputs need to be consumed reliably by APIs, databases, agents, and automated workflows.

---

## 📌 Project Status

**Completed**

- Schema design ✅
- Prompt design ✅
- Five test cases ✅
- JSON validation ✅
- Tricky-input testing ✅
- Prompt improvement ✅
- Comparison analysis ✅
- Documentation ✅