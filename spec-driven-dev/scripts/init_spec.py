#!/usr/bin/env python3
"""
Initialize a new spec directory with template files.

Usage:
    python init_spec.py <feature-name> [--path <output-directory>]

Example:
    python init_spec.py user-authentication
    python init_spec.py payment-processing --path ./specs
"""

import argparse
import os
import sys
from pathlib import Path


REQUIREMENTS_TEMPLATE = """# {feature_name} Requirements

## User Story

As a [type of user],
I want [goal/desire]
So that [benefit/value]

## Context

[Brief description of the feature and why it's needed]

## Acceptance Criteria

### [Functional Area 1]

WHEN [condition/event]
THE SYSTEM SHALL [expected behavior]

WHEN [error condition]
THE SYSTEM SHALL [error handling behavior]

### [Functional Area 2]

WHEN [condition/event]
THE SYSTEM SHALL [expected behavior]

## Non-Functional Requirements

### Performance
- [Performance expectations]

### Security
- [Security requirements]

### Usability
- [User experience requirements]

## Out of Scope

- [What this feature explicitly does NOT include]

## Dependencies

- [Other features or systems this depends on]

## Success Metrics

- [How success will be measured]
"""


DESIGN_TEMPLATE = """# {feature_name} Design

## Overview

[High-level description of the technical approach]

## Architecture

### Components

- **[Component Name]**: [Purpose and responsibilities]

### Component Diagram

```
[Visual representation of components and their relationships]
```

## Data Flow

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant API
    participant Service
    participant Database
    
    User->>Frontend: [action]
    Frontend->>API: [request]
    API->>Service: [process]
    Service->>Database: [query]
    Database-->>Service: [data]
    Service-->>API: [result]
    API-->>Frontend: [response]
    Frontend-->>User: [display]
```

## Data Models

### [Entity Name]

```
{{
  "field1": "type",
  "field2": "type"
}}
```

**Schema Changes:**
- [Database migration needed]

## API Contracts

### [Endpoint Name]

**Request:**
```
POST /api/[endpoint]
{{
  "param1": "value"
}}
```

**Response:**
```
{{
  "status": "success",
  "data": {{}}
}}
```

## Implementation Considerations

### Security
- [Authentication/authorization approach]

### Performance
- [Caching strategy]

### Error Handling
- [Error handling strategy]

### Edge Cases
- [Edge case 1 and how to handle it]
"""


TASKS_TEMPLATE = """# {feature_name} Implementation Tasks

## Phase 1: Setup

- [ ] **Task 1.1**: [Task description]
  - **Expected outcome**: [What "done" looks like]
  - **Dependencies**: None
  - **References**: requirements.md (section name)

## Phase 2: Core Implementation

- [ ] **Task 2.1**: [Task description]
  - **Expected outcome**: [What "done" looks like]
  - **Dependencies**: Task 1.1
  - **References**: design.md (component name)

## Phase 3: Testing & Deployment

- [ ] **Task 3.1**: [Task description]
  - **Expected outcome**: [What "done" looks like]
  - **Dependencies**: Task 2.1

## Task Status Legend

- [ ] Not started
- [→] In progress
- [✓] Completed
- [⚠] Blocked

## Notes

- [Any general notes about the implementation]
"""


def create_spec_directory(feature_name: str, output_path: str = ".") -> None:
    """Create a spec directory with template files."""
    # Create feature directory
    feature_dir = Path(output_path) / feature_name
    
    if feature_dir.exists():
        print(f"Error: Directory '{feature_dir}' already exists")
        sys.exit(1)
    
    feature_dir.mkdir(parents=True)
    
    # Format feature name for display (replace hyphens with spaces and title case)
    formatted_name = feature_name.replace("-", " ").replace("_", " ").title()
    
    # Create template files
    files = {
        "requirements.md": REQUIREMENTS_TEMPLATE.format(feature_name=formatted_name),
        "design.md": DESIGN_TEMPLATE.format(feature_name=formatted_name),
        "tasks.md": TASKS_TEMPLATE.format(feature_name=formatted_name),
    }
    
    for filename, content in files.items():
        filepath = feature_dir / filename
        filepath.write_text(content)
        print(f"Created: {filepath}")
    
    print(f"\n✓ Spec directory initialized at: {feature_dir}")
    print("\nNext steps:")
    print(f"1. Edit {feature_dir}/requirements.md with your user stories and acceptance criteria")
    print(f"2. Document the technical approach in {feature_dir}/design.md")
    print(f"3. Break down implementation into tasks in {feature_dir}/tasks.md")


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new spec directory with template files"
    )
    parser.add_argument(
        "feature_name",
        help="Name of the feature (e.g., user-authentication)"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Output directory path (default: current directory)"
    )
    
    args = parser.parse_args()
    
    # Validate feature name
    if not args.feature_name:
        print("Error: Feature name cannot be empty")
        sys.exit(1)
    
    # Convert to lowercase and replace spaces with hyphens
    feature_name = args.feature_name.lower().replace(" ", "-")
    
    create_spec_directory(feature_name, args.path)


if __name__ == "__main__":
    main()
