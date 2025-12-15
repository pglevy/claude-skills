# Spec-Driven Development Skill

## Overview

This skill provides comprehensive guidance for implementing a specification-first approach to software development, inspired by methodologies like Kiro. It helps structure development around clear requirements, technical design, and implementation planning.

## What's Included

### Core Documentation (SKILL.md)
- Three-spec structure (requirements, design, tasks)
- EARS notation for writing testable requirements
- Workflow phases from requirements to execution
- Property-based testing concepts for correctness validation
- Best practices for spec organization and iteration

### Reference Materials

**ears-examples.md** - Extensive EARS notation examples including:
- Domain-specific examples (e-commerce, SaaS, social media)
- Pattern variations (state-based, event-driven, conditional)
- Performance, security, and validation requirements
- Anti-patterns to avoid
- Checklist for writing effective requirements

**workflow-examples.md** - Complete workflow walkthroughs showing:
- Building a user authentication feature from scratch
- Iterating on existing specs (adding 2FA)
- Converting EARS requirements to property-based tests
- Real-world examples with actual code

### Templates

Three markdown templates ready to use:
- **requirements-template.md** - User stories and EARS acceptance criteria
- **design-template.md** - Technical architecture and implementation considerations  
- **tasks-template.md** - Implementation plan with phases and dependencies

### Helper Script

**init_spec.py** - Python script to initialize new spec directories:
```bash
python scripts/init_spec.py <feature-name> --path ./specs
```

Automatically creates the three-file spec structure with templates.

## Key Concepts

### EARS Notation
Easy Approach to Requirements Syntax - a structured format for testable requirements:

```
WHEN [condition/event]
THE SYSTEM SHALL [expected behavior]
```

Benefits:
- Clear and unambiguous
- Directly testable
- Easy traceability
- Reduces misunderstandings

### Three-Spec Structure

1. **requirements.md** - User stories with EARS acceptance criteria
2. **design.md** - Technical architecture, diagrams, data models
3. **tasks.md** - Discrete implementation tasks with dependencies

### Property-Based Testing

Validates universal properties of system behavior across comprehensive input spaces:
- Traditional: "User adds Item #5 to cart → Item #5 in cart"
- Property-based: "For ANY user and ANY item → adding to cart makes it appear"

### Workflow Phases

```
Requirements → Design → Implementation Planning → Execution
```

Each phase builds on the previous, with clear decision points and outputs.

## When to Use This Skill

**Ideal for:**
- Features with clear business requirements
- Systems requiring traceability (compliance, auditing)
- Team collaboration across product and engineering
- Complex features needing upfront planning
- Projects where requirements clarity is critical

**Less suitable for:**
- Rapid prototyping and experimentation
- Simple, well-understood tasks
- Throwaway code or spikes

## How to Use

1. **Initialize a spec**: Use the init_spec.py script or create the three files manually
2. **Document requirements**: Write user stories with EARS acceptance criteria
3. **Design the solution**: Document architecture, data models, and considerations
4. **Plan implementation**: Break down into discrete, trackable tasks
5. **Execute**: Work through tasks, updating status and refining specs as needed

## Installation

The .skill file is a zip archive containing all materials. Extract it to access:
- Templates in `assets/`
- Reference documentation in `references/`
- Helper scripts in `scripts/`
- Main skill documentation in `SKILL.md`

## Best Practices

- Store specs in version control with your code
- Create separate specs for different features
- Reference specs in pull requests and during implementation
- Update specs when requirements change (they're living documents)
- Use EARS notation for all testable requirements
- Keep tasks to 1-4 hours of work each

## Example Spec Structure

```
specs/
├── user-authentication/
│   ├── requirements.md   # User stories with EARS criteria
│   ├── design.md         # Architecture and data models
│   └── tasks.md          # Implementation plan
├── payment-processing/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
└── admin-dashboard/
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

## Benefits

- **Alignment**: Clear requirements reduce misunderstandings
- **Traceability**: Link implementation to specific requirements
- **Testability**: EARS format maps directly to test cases
- **Collaboration**: Common language for product and engineering
- **Documentation**: Specs serve as technical documentation
- **Quality**: Property-based testing catches edge cases

## Credits

This skill is inspired by the spec-based development approach documented by Kiro, particularly their use of EARS notation, three-file specifications, and property-based testing for correctness validation.
