# Tricky Input Test Result

## Input

> URGENT!!! Hey, I'm John... or maybe Jonathan 😂. Someone charged my card THREE times for the same order!!! I think my email was john123@gmail.com... wait, it might be john@gmail.com. Anyway FIX THIS NOW!!! Also, my package hasn't arrived and I think the product might be damaged. I need my money back ASAP!!!

---

## Model Output

```json
{
  "customer_name": null,
  "email": null,
  "issue_type": "Payment Issue",
  "urgency": "high",
  "summary": "Customer reports being charged three times for the same order and also reports a missing package and potentially damaged product."
}