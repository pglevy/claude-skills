# EARS Notation Reference

This reference provides detailed examples and patterns for writing requirements in EARS (Easy Approach to Requirements Syntax) notation.

## EARS Syntax Patterns

### Basic Pattern
```
WHEN [condition/event]
THE SYSTEM SHALL [expected behavior]
```

### Pattern Variations

**State-based requirements:**
```
WHEN the system is in [state]
THE SYSTEM SHALL [behavior]
```

**Event-driven requirements:**
```
WHEN [user/system] performs [action]
THE SYSTEM SHALL [response]
```

**Conditional requirements:**
```
WHEN [condition A] AND [condition B]
THE SYSTEM SHALL [behavior]
```

**Error handling:**
```
WHEN [error condition occurs]
THE SYSTEM SHALL [error handling behavior]
```

## Domain-Specific Examples

### E-Commerce

**Product Browsing:**
```
WHEN a user searches for a product
THE SYSTEM SHALL display results ranked by relevance

WHEN a user applies filters to search results
THE SYSTEM SHALL update the displayed products to match all active filters

WHEN no products match the search criteria
THE SYSTEM SHALL display a "no results found" message with suggested alternatives
```

**Shopping Cart:**
```
WHEN a user adds an item to their cart
THE SYSTEM SHALL increase the cart count badge and display a confirmation message

WHEN a user updates the quantity of a cart item
THE SYSTEM SHALL recalculate the subtotal and total immediately

WHEN a user attempts to checkout with an out-of-stock item
THE SYSTEM SHALL notify the user and prevent checkout completion
```

**Payment Processing:**
```
WHEN a user submits payment information
THE SYSTEM SHALL validate the card number format before processing

WHEN a payment is successfully processed
THE SYSTEM SHALL send a confirmation email within 5 minutes

WHEN a payment fails
THE SYSTEM SHALL display the specific error reason and offer retry options
```

### Social Media Application

**User Interactions:**
```
WHEN a user posts content
THE SYSTEM SHALL publish it to their followers' feeds immediately

WHEN a user likes a post
THE SYSTEM SHALL increment the like count and notify the post author

WHEN a user receives a notification
THE SYSTEM SHALL display a badge on the notifications icon
```

**Privacy & Security:**
```
WHEN a user sets their profile to private
THE SYSTEM SHALL hide their posts from non-followers

WHEN a user reports content
THE SYSTEM SHALL flag it for review and hide it from the reporter

WHEN suspicious login activity is detected
THE SYSTEM SHALL require two-factor authentication
```

### SaaS Application

**User Management:**
```
WHEN an admin invites a new user
THE SYSTEM SHALL send an invitation email with a 7-day expiration

WHEN a user's trial period expires
THE SYSTEM SHALL restrict access to paid features and display an upgrade prompt

WHEN a user is assigned a new role
THE SYSTEM SHALL update their permissions immediately
```

**Data & Analytics:**
```
WHEN a user requests a data export
THE SYSTEM SHALL generate the file and email a download link within 1 hour

WHEN system usage exceeds 80% of the plan limit
THE SYSTEM SHALL notify the account owner

WHEN a webhook endpoint fails 3 consecutive times
THE SYSTEM SHALL disable it and notify the configuration owner
```

## Complex Requirements

### Multi-Condition Requirements

```
WHEN a user is authenticated AND has an active subscription AND is within their usage quota
THE SYSTEM SHALL allow API access

WHEN a form is submitted AND contains valid data AND passes spam checks
THE SYSTEM SHALL process the submission and send confirmation

WHEN a file is uploaded AND is under 50MB AND has an allowed extension
THE SYSTEM SHALL accept the upload and begin processing
```

### Time-Based Requirements

```
WHEN a session is inactive for 30 minutes
THE SYSTEM SHALL automatically log the user out

WHEN a scheduled report is due
THE SYSTEM SHALL generate and email it within 5 minutes of the scheduled time

WHEN a reminder is set for a future date
THE SYSTEM SHALL display it at the specified time
```

### Performance Requirements

```
WHEN a user searches the database
THE SYSTEM SHALL return results within 500ms for queries under 1000 records

WHEN a page loads
THE SYSTEM SHALL display above-the-fold content within 2 seconds

WHEN concurrent users exceed 10,000
THE SYSTEM SHALL maintain response times under 1 second through auto-scaling
```

### Data Validation Requirements

```
WHEN a user enters an email address
THE SYSTEM SHALL validate it matches the email regex pattern

WHEN a password is created
THE SYSTEM SHALL enforce minimum 12 characters with at least one uppercase, lowercase, number, and special character

WHEN a date range is selected
THE SYSTEM SHALL ensure the end date is not before the start date
```

## Anti-Patterns (What to Avoid)

### Too Vague
❌ **Bad:**
```
WHEN a user logs in
THE SYSTEM SHALL work properly
```

✓ **Good:**
```
WHEN a user submits valid credentials
THE SYSTEM SHALL authenticate the user and redirect to the dashboard within 2 seconds
```

### Implementation Details Instead of Requirements
❌ **Bad:**
```
WHEN a user submits a form
THE SYSTEM SHALL call the validateForm() function and POST to /api/submit
```

✓ **Good:**
```
WHEN a user submits a form with invalid data
THE SYSTEM SHALL display field-level validation errors and prevent submission
```

### Combining Multiple Requirements
❌ **Bad:**
```
WHEN a user creates an account
THE SYSTEM SHALL validate the email, hash the password, create the user record, send a welcome email, and log them in
```

✓ **Good:** (Split into separate requirements)
```
WHEN a user creates an account with an invalid email
THE SYSTEM SHALL display an email validation error

WHEN a user creates an account with valid data
THE SYSTEM SHALL hash the password using bcrypt before storage

WHEN a new account is successfully created
THE SYSTEM SHALL send a welcome email within 5 minutes

WHEN a new account is successfully created
THE SYSTEM SHALL automatically log the user in
```

### Missing Error Conditions
❌ **Incomplete:** (Only happy path)
```
WHEN a user uploads a file
THE SYSTEM SHALL save it to storage
```

✓ **Complete:** (Include error cases)
```
WHEN a user uploads a file under 50MB
THE SYSTEM SHALL save it to storage and return a success message

WHEN a user uploads a file over 50MB
THE SYSTEM SHALL reject the upload and display a size limit error

WHEN file upload fails due to network error
THE SYSTEM SHALL allow the user to retry and preserve their progress
```

## Writing Effective Requirements

### Checklist for Each Requirement

- [ ] Is the condition/trigger clear and unambiguous?
- [ ] Is the expected behavior specific and measurable?
- [ ] Can this requirement be directly tested?
- [ ] Does it avoid implementation details?
- [ ] Are edge cases and error conditions covered?
- [ ] Is it independent of other requirements?
- [ ] Does it map to a user story or business need?

### Coverage Checklist

For each feature, ensure EARS requirements cover:

- [ ] Happy path scenarios
- [ ] Error conditions and edge cases
- [ ] Input validation
- [ ] Authorization/permissions
- [ ] Performance expectations
- [ ] Data persistence requirements
- [ ] User notifications and feedback
- [ ] Integration points with other systems
