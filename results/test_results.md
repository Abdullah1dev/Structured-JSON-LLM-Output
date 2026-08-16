# JSON Extraction Test Results

## Overview

Five different customer support messages were tested using the JSON extraction prompt.

Each response was required to:

- Return valid JSON only.
- Follow the predefined schema.
- Contain exactly five fields.
- Use `null` when information was unavailable.
- Use a predefined `issue_type`.
- Use only `low`, `medium`, or `high` for urgency.
- Avoid inventing customer information.

---

# Test Case 1 — Payment Issue

### Input

> Hi, my name is Ahmed Khan and I was charged twice for my order. Please check this and issue a refund if necessary. You can contact me at ahmed.khan@example.com.

### Model Output

```json
{
  "customer_name": "Ahmed Khan",
  "email": "ahmed.khan@example.com",
  "issue_type": "Payment Issue",
  "urgency": "high",
  "summary": "Customer was charged twice for the same order and is requesting assistance with a possible refund."
}
```

### Validation

**Result:** Valid JSON

All five required fields are present and the values follow the defined schema.

---

# Test Case 2 — Damaged Product

### Input

> Hello, I'm Sara Ali. My laptop arrived today but the screen is cracked and the device is not usable. My email is sara.ali@example.com. I need help as soon as possible.

### Model Output

```json
{
  "customer_name": "Sara Ali",
  "email": "sara.ali@example.com",
  "issue_type": "Damaged Product",
  "urgency": "high",
  "summary": "Customer received a laptop with a cracked screen and cannot use the device."
}
```

### Validation

**Result:** Valid JSON

All five required fields are present. The model correctly identified the damaged product and classified the issue as high urgency.

---

# Test Case 3 — Account Issue

### Input

> I can't log into my account. I've tried resetting my password several times, but the password reset link isn't working.

### Model Output

```json
{
  "customer_name": null,
  "email": null,
  "issue_type": "Account Issue",
  "urgency": "medium",
  "summary": "Customer cannot log into their account because the password reset link is not working."
}
```

### Validation

**Result:** Valid JSON

The customer did not provide a name or email address. The model correctly returned `null` for both fields instead of inventing information.

---

# Test Case 4 — Shipping Issue

### Input

> My order was supposed to arrive three days ago, but I still haven't received it. Can you please tell me where my package is? My email is ali@example.com.

### Model Output

```json
{
  "customer_name": null,
  "email": "ali@example.com",
  "issue_type": "Shipping Issue",
  "urgency": "medium",
  "summary": "Customer's order is three days late and they are requesting an update on the package."
}
```

### Validation

**Result:** Valid JSON

The model correctly extracted the email address and identified the delayed order as a shipping issue.

---

# Test Case 5 — Product Inquiry

### Input

> Hi, I wanted to know whether you offer international shipping for your products. I'm considering placing an order soon.

### Model Output

```json
{
  "customer_name": null,
  "email": null,
  "issue_type": "Product Inquiry",
  "urgency": "low",
  "summary": "Customer wants to know whether international shipping is available."
}
```

### Validation

**Result:** Valid JSON

The customer did not provide a name or email address, so both fields were correctly returned as `null`. The model identified the message as a product inquiry with low urgency.

---

# Test Summary

| Test Case | Issue Type | Urgency | Name | Email | JSON Valid |
|---|---|---|---|---|---|
| 1 | Payment Issue | High | ✓ | ✓ | ✓ |
| 2 | Damaged Product | High | ✓ | ✓ | ✓ |
| 3 | Account Issue | Medium | ✗ | ✗ | ✓ |
| 4 | Shipping Issue | Medium | ✗ | ✓ | ✓ |
| 5 | Product Inquiry | Low | ✗ | ✗ | ✓ |

---

# Overall Result

All five test cases produced responses that followed the required JSON structure.

The model successfully:

- Returned JSON without additional text.
- Included all five required fields.
- Used `null` when customer information was unavailable.
- Classified customer issues using the predefined categories.
- Classified urgency using the allowed values.
- Generated concise summaries.
- Avoided inventing missing customer information.

## Final Result

**5/5 responses successfully followed the required JSON structure.**

However, visual inspection alone is not sufficient to guarantee that the responses are machine-readable. The next step is to validate each JSON response programmatically using Python's `json.loads()` function.

This will confirm whether the model outputs can actually be parsed and consumed by an application.