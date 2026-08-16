# Original Prompt vs Improved Prompt Comparison

## Overview

This experiment tested whether a carefully designed prompt can make an LLM produce reliable and predictable JSON output when processing customer support messages.

The original prompt was first tested on five normal customer messages and successfully produced valid JSON responses.

A deliberately messy customer message was then introduced to identify weaknesses in the prompt. After analyzing the result, the prompt was improved and the same tricky input was tested again.

---

# Comparison Objective

The comparison focuses on:

- JSON validity
- Schema compliance
- Handling missing information
- Handling ambiguous information
- Handling multiple issues
- Urgency classification
- Information reliability
- Consistency of output

---

# Original Prompt

The original prompt required the model to:

- Return only valid JSON.
- Follow the predefined five-field schema.
- Use `null` when information was unavailable.
- Select an issue type from the predefined categories.
- Classify urgency as `low`, `medium`, or `high`.
- Avoid inventing customer information.

The original prompt performed successfully on all five normal test cases.

### Normal Test Result

| Metric | Result |
|---|---|
| Test cases | 5 |
| Valid JSON responses | 5/5 |
| Schema compliance | 5/5 |
| Overall result | PASS |

---

# Tricky Input

The following deliberately messy input was used to test the limits of the original prompt:

> URGENT!!! Hey, I'm John... or maybe Jonathan 😂. Someone charged my card THREE times for the same order!!! I think my email was john123@gmail.com... wait, it might be john@gmail.com. Anyway FIX THIS NOW!!! Also, my package hasn't arrived and I think the product might be damaged. I need my money back ASAP!!!

This input contained:

- An ambiguous customer name.
- Multiple possible email addresses.
- Multiple customer issues.
- Strong urgency indicators.
- Emotional language.
- Excessive punctuation.
- A refund request.
- Potentially conflicting information.

---

# Original Prompt Result

The original prompt produced:

```json
{
  "customer_name": null,
  "email": null,
  "issue_type": "Payment Issue",
  "urgency": "high",
  "summary": "Customer reports being charged three times for the same order and also reports a missing package and potentially damaged product."
}
```

## Analysis

The original prompt handled most of the difficult information correctly.

### Ambiguous Name

The input contained:

```text
John... or maybe Jonathan
```

The model returned:

```json
"customer_name": null
```

This was the correct behavior because the name could not be determined confidently.

### Ambiguous Email

The input contained:

```text
john123@gmail.com
john@gmail.com
```

The model returned:

```json
"email": null
```

Again, this avoided guessing.

### Multiple Issues

The customer mentioned:

1. Being charged three times.
2. A package that had not arrived.
3. A potentially damaged product.
4. A request for a refund.

The original schema allowed only one `issue_type`.

The model selected:

```json
"issue_type": "Payment Issue"
```

This was reasonable because the repeated charge was the most clearly stated primary problem.

However, the original prompt did not explicitly explain how to handle multiple issues.

This was identified as the main area for improvement.

---

# Improvements Made

The improved prompt added explicit instructions for ambiguous and multi-issue situations.

### 1. Ambiguous Names

The improved prompt specifies:

> If multiple possible names are provided or the name is ambiguous, return `null`.

This makes the expected behavior explicit.

---

### 2. Ambiguous Emails

The improved prompt specifies:

> If multiple possible email addresses are provided and the correct one cannot be determined, return `null`.

This prevents the model from selecting an email arbitrarily.

---

### 3. Multiple Issues

The improved prompt explicitly states:

> If multiple issues are present, select the issue that appears to be the customer's primary concern.

This makes the classification behavior more predictable.

---

### 4. Secondary Issues

The improved prompt also instructs the model to include important secondary issues in the summary.

This prevents relevant information from being lost simply because the schema allows only one `issue_type`.

---

### 5. Stronger Urgency Rules

The improved prompt explicitly identifies words such as:

- urgent
- immediately
- ASAP
- right now

as indicators of high urgency.

This makes urgency classification more consistent.

---

# Improved Prompt Result

After applying the improvements, the exact same tricky input was tested again.

The improved model produced:

```json
{
  "customer_name": null,
  "email": null,
  "issue_type": "Payment Issue",
  "urgency": "high",
  "summary": "Customer reports being charged three times for the same order, has not received the package, believes the product may be damaged, and is requesting a refund."
}
```

---

# Side-by-Side Comparison

| Criteria | Original Prompt | Improved Prompt |
|---|---|---|
| Valid JSON | PASS | PASS |
| Required fields | PASS | PASS |
| Ambiguous name handling | PASS | PASS |
| Ambiguous email handling | PASS | PASS |
| Primary issue selection | Reasonable | Explicitly defined |
| Multiple issue handling | Limited | Improved |
| Secondary issue handling | Basic | Explicit |
| Urgency classification | PASS | More clearly defined |
| Prevents guessing | PASS | Stronger instructions |
| Predictability | Good | Better |
| Schema compliance | PASS | PASS |

---

# Key Difference

The most important difference was **not the JSON format itself**.

Both prompts produced valid JSON.

The improvement came from making the model's behavior more explicit when dealing with ambiguous and messy input.

The improved prompt transformed implicit behavior into explicit rules:

```text
Ambiguous information
        ↓
Don't guess
        ↓
Return null
```

and:

```text
Multiple issues
        ↓
Identify primary issue
        ↓
Include secondary issues in summary
```

---

# Validation Comparison

The outputs were also checked programmatically using Python's `json.loads()`.

The validation process checked:

- JSON syntax
- Required fields
- Allowed issue types
- Allowed urgency values
- Data types
- Nullable fields

### Results

| Test | Original Prompt | Improved Prompt |
|---|---|---|
| Normal Test 1 | PASS | — |
| Normal Test 2 | PASS | — |
| Normal Test 3 | PASS | — |
| Normal Test 4 | PASS | — |
| Normal Test 5 | PASS | — |
| Tricky Input | PASS with limitations | PASS with improved handling |

---

# What This Experiment Demonstrated

The experiment demonstrated that simply asking an LLM to return JSON is not enough for reliable application development.

A strong structured-output prompt should also define:

- The exact schema.
- Allowed values.
- Missing-value behavior.
- Ambiguity handling.
- Classification rules.
- Output restrictions.
- Rules for edge cases.

This makes the model's output more predictable and easier for an application to consume.

---

# Overall Comparison

The original prompt was already effective for normal customer support messages and successfully produced valid JSON for all five standard test cases.

The tricky input revealed that real-world messages can contain ambiguity and multiple issues that are not always covered by a basic schema.

The improved prompt addressed these weaknesses by explicitly defining how ambiguous information and multiple issues should be handled.

Therefore, the **improved prompt provides more predictable and reliable behavior for messy real-world inputs**, while maintaining the same valid JSON structure.

---

# Final Result

### Original Prompt

**5/5 normal tests passed.**

The prompt successfully generated valid, structured JSON.

### Improved Prompt

The improved prompt successfully handled the deliberately messy input while maintaining:

- Valid JSON.
- Schema compliance.
- No invented customer information.
- Consistent urgency classification.
- Better handling of multiple issues.

## Final Conclusion

The experiment shows that **structured output requires more than requesting JSON**.

Defining a clear schema together with explicit rules for ambiguity, missing information, allowed values, and edge cases makes LLM output significantly more predictable and suitable for integration into real applications.