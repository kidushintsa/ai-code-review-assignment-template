# AI Code Review Assignment (Python)

## Candidate

- Name: Kidus Hintsa Nega
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- Incorrect average calculation:
  The original code divides by the total number of orders instead of the number of non-cancelled orders, producing incorrect results

- Division by zero risk:
  If all orders are cancelled or the list is empty, the original code divides by zero, causing a runtime error (ZeroDivisionError).

### Edge cases & risks

- Empty list input:
  An empty list causes a division-by-zero

- All orders cancelled:
  No valid orders exist, division by 0 still occurs.

### Code quality / design issues

- confusing variable name:
  variable "count" should have been named more discriptively such as "valid_order_count".

- Poor separation of concerns:
  Business logic and data validation are mixed.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Count only non-cancelled orders.

- Prevent division by zero by checking valid order count.

- Improve variable naming from "count" to "valid_order_count"

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Normal orders
  Scenario: A list with several orders where some are completed and some are cancelled.

  Why: To verify that the function correctly sums only valid orders and calculates the correct average.

- All orders cancelled

  Scenario: A list where every order has "status": "cancelled".

  Why: To check that the function does not crash (no division by zero) and returns 0 as expected.

- Empty list

  Scenario: The function receives an empty list [].

  Why: To confirm it handles empty input safely without errors and returns 0.

- Single valid order

  Scenario: Only one non-cancelled order in the list.

  Why: Ensures the function works correctly with minimal input and doesn’t divide incorrectly.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- Factually incorrect:
  The original code divides by the total number of orders, not the number of non-cancelled orders.

- Ignores edge cases:
  Does not mention empty input or division-by-zero risk.

### Rewritten explanation

- This function calculates the average order value by summing the amounts of all non-cancelled orders and dividing by the number of valid (non-cancelled) orders,
  If no valid orders exist, the function safely returns 0 to avoid division errors.

Cancelled orders are excluded from both the total amount and the count to ensure accurate results.

## 4) Final Judgment

- Decision: Request Changes

- Justification: The original implementation contains a critical division-by-zero bug and calculates the average incorrectly when cancelled orders are present.

- Confidence & unknowns: High confidence after fixes. Assumnig consistent data structure and numeric order amounts.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- Non-string elements:
  The original function will raise a TypeError if the input list contains non-string items.

- Invalid email formats:
  Any string without "@" is ignored, but simple "@" alone counts as valid — may not match real-world expectations.

### Edge cases & risks

- Invalid email formats:
  simple "@" alone counts as valid, may not match real-world expectations

### Code quality / design issues

- Variable naming:
  "count" is generic, "valid_email_count" is clearer.

- Validation logic is minimal:
  Only checks for "@", does not validate the domain part
  or structure of the email.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Add type check to ensure only strings are counted.

- regex for better accuracy.

- Improve variable naming from "count" to "valid_email_count"

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Empty list
  Scenario: The input list is [].

  Why: To confirm the function handles empty input safely and returns 0.

- Non-string entries
  Scenario: A list contains numbers, None, or other non-string types, e.g., [123, None].

  Why: To make sure the function does not crash and only counts valid strings.

- Malformed emails
  Scenario: Strings that are not proper emails, e.g., ["@domain.com", "kk@", "just"].

  Why: To confirm that invalid formats are ignored.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- Vague about what “valid” means, Does not clarify the logic used for checking validity.

- Does not mention that non-string inputs may cause errors in the original version.

### Rewritten explanation

- This function counts how many strings in the input list appear to be valid emails.
  An email is considered valid if it contains "@" and a "." in the domain part.

  It Returns 0 if no valid emails are found or if the list is empty, and Non-string entries and invalid email formats are ignored.

## 4) Final Judgment

- Decision: Request Changes

- Justification:
  Original code works for basic strings but fails for non-string elements and counts minimal "@" strings as valid. The corrected version safely handles non-strings and improves validation.

- Confidence & unknowns:
  High confidence can handle real world Real-world validation.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- Division by total length instead of valid measurements:
  Original code divides by len(values) even if some entries are None, producing an incorrect average.

- Type conversion risk:
  Original code assumes all non-None values can be converted to float, which can raise ValueError or TypeError.

### Edge cases & risks

- Empty list leads to division by zero (ZeroDivisionError).

- All values None means returns 0 / count, which is incorrect.

- Mixed types such as non-numeric strings or objects cause runtime errors in the original code.

### Code quality / design issues

- Variable naming: count is misleading; valid_count is more descriptive.

- Validation logic: Original code does not skip invalid entries safely.

- Error handling: casting (float(v)) might throw error if the input is uncastable, and the orignal code didn't handle that

## 2) Proposed Fixes / Improvements

### Summary of changes

- Count only successfully converted numeric values.

- Skip None and any values that cannot be converted to float using try/except.

- Avoid division by zero by returning 0 if no valid measurements exist.

- Improve variable names (valid_count instead of count) for clarity.

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

- Normal numeric list
  Scenario: [10, 20, 30]

  Why: Verify average calculation works with all valid values.

- List with None values:
  Scenario: [10, None, 20]

  Why: Ensure None is ignored and average uses only valid entries.

- Mixed types (numeric strings, invalid strings, objects):
  Scenario: [10, "20", "abc", [1,2], None]

  Why: Test that only convertible values are counted and function does not crash.

- Empty list
  Scenario: empthy list([])

  Why: Ensure function returns 0 safely.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- Does not mention that invalid types (non-numeric strings or objects) could previously cause runtime errors.

- Could be clearer about division by number of valid entries, not total entries.

### Rewritten explanation

- This function computes the average of valid numeric measurements.
  It ignores None values and skips any entries that cannot be converted to a float.
- Returns 0 if there are no valid measurements, ensuring safe handling
  of empty or invalid input, finally, Only values successfully converted to floats are included in the average.

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject

- Justification: Fixed version safely handles None, invalid types, and empty lists while computing the correct average

- Confidence & unknowns: High confidence for numeric or numeric-string input. Edge cases with complex objects are safely ignored.
