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

- Rename variable name "count" to "valid_order_count"

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

-

### Edge cases & risks

-

### Code quality / design issues

-

## 2) Proposed Fixes / Improvements

### Summary of changes

-

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

-

### Rewritten explanation

-

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

-

### Edge cases & risks

-

### Code quality / design issues

-

## 2) Proposed Fixes / Improvements

### Summary of changes

-

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

-

### Rewritten explanation

-

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
