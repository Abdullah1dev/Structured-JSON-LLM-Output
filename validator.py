import json


# Model outputs from the five test cases
responses = [
    # Test Case 1
    """
    {
        "customer_name": "Ahmed Khan",
        "email": "ahmed.khan@example.com",
        "issue_type": "Payment Issue",
        "urgency": "high",
        "summary": "Customer was charged twice for the same order and is requesting assistance with a possible refund."
    }
    """,

    # Test Case 2
    """
    {
        "customer_name": "Sara Ali",
        "email": "sara.ali@example.com",
        "issue_type": "Damaged Product",
        "urgency": "high",
        "summary": "Customer received a laptop with a cracked screen and cannot use the device."
    }
    """,

    # Test Case 3
    """
    {
        "customer_name": null,
        "email": null,
        "issue_type": "Account Issue",
        "urgency": "medium",
        "summary": "Customer cannot log into their account because the password reset link is not working."
    }
    """,

    # Test Case 4
    """
    {
        "customer_name": null,
        "email": "ali@example.com",
        "issue_type": "Shipping Issue",
        "urgency": "medium",
        "summary": "Customer's order is three days late and they are requesting an update on the package."
    }
    """,

    # Test Case 5
    """
    {
        "customer_name": null,
        "email": null,
        "issue_type": "Product Inquiry",
        "urgency": "low",
        "summary": "Customer wants to know whether international shipping is available."
    }
    """
]


# Allowed values defined by our schema
allowed_issue_types = {
    "Payment Issue",
    "Shipping Issue",
    "Damaged Product",
    "Account Issue",
    "Technical Issue",
    "Refund Request",
    "Product Inquiry",
    "Other"
}

allowed_urgency = {
    "low",
    "medium",
    "high"
}

required_fields = {
    "customer_name",
    "email",
    "issue_type",
    "urgency",
    "summary"
}


def validate_response(response, test_number):
    print(f"\nTest Case {test_number}")
    print("-" * 40)

    # Step 1: Try to parse the response
    try:
        data = json.loads(response)
        print("✓ Valid JSON")
    except json.JSONDecodeError as error:
        print("✗ Invalid JSON")
        print(f"Error: {error}")
        return False

    # Step 2: Check that the response is an object
    if not isinstance(data, dict):
        print("✗ Response is not a JSON object")
        return False

    # Step 3: Check required fields
    if set(data.keys()) != required_fields:
        print("✗ Schema fields do not match")
        print(f"Expected: {required_fields}")
        print(f"Received: {set(data.keys())}")
        return False

    print("✓ All required fields are present")

    # Step 4: Validate issue type
    if data["issue_type"] not in allowed_issue_types:
        print("✗ Invalid issue_type")
        return False

    print("✓ Valid issue_type")

    # Step 5: Validate urgency
    if data["urgency"] not in allowed_urgency:
        print("✗ Invalid urgency")
        return False

    print("✓ Valid urgency")

    # Step 6: Validate nullable fields
    if data["customer_name"] is not None and not isinstance(
        data["customer_name"], str
    ):
        print("✗ customer_name must be a string or null")
        return False

    if data["email"] is not None and not isinstance(
        data["email"], str
    ):
        print("✗ email must be a string or null")
        return False

    # Step 7: Validate summary
    if not isinstance(data["summary"], str):
        print("✗ summary must be a string")
        return False

    print("✓ Data matches schema")

    return True


# Run validation for all five responses
results = []

for number, response in enumerate(responses, start=1):
    result = validate_response(response, number)
    results.append(result)


# Final result
print("\n" + "=" * 50)
print("FINAL VALIDATION RESULT")
print("=" * 50)

passed = sum(results)
total = len(results)

print(f"Tests passed: {passed}/{total}")

if passed == total:
    print("✓ All responses passed validation.")
    print("✓ All responses are valid JSON and follow the schema.")
else:
    print("✗ Some responses failed validation.")