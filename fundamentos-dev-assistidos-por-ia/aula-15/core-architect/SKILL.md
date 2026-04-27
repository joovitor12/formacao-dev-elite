---
name: core-architect
description: Enforce a Python architectural standard with strict separation between `services/` and `controllers/`, mandatory type hints, constants instead of magic numbers, network error handling with `try/except`, logging-based error reporting, and fallback values for external APIs. Use when Codex needs to create, refactor, review, or extend Python code that integrates with APIs, HTTP clients, infrastructure adapters, or controller-service flows.
---

# Core Architect

## Overview

Follow these instructions rigorously whenever this skill is active.
Preserve the user's existing framework and naming patterns when they do not conflict with the rules below.

## Architectural Rules

- Place infrastructure logic and network calls in `services/`.
- Place orchestration logic, response shaping, and returned data flow in `controllers/`.
- Keep controllers focused on coordinating services and preparing outputs.
- Keep services focused on side effects, API integration, and infrastructure concerns.

## Code Style Rules

- Use Python type hints in every function, including parameters and return values.
- Define constants at the top of the file for fixed numeric values, limits, timeouts, retries, status codes, or defaults.
- Avoid magic numbers in implementations, examples, and suggested patches.
- Use always env variables for constants that may differ between environments (e.g., API keys, URLs, timeouts, retries, http headers).

## Error Handling Rules

- Wrap every network function in `try/except`.
- Use `logging` for error reporting instead of `print`.
- Prefer structured and contextual log messages that make failures diagnosable.
- Return or propagate errors in a way that keeps controller behavior predictable.

## Resilience Rules

- Propose and implement a fallback value for every external API call whenever it is reasonable to do so.
- Make fallback behavior explicit in code or in the explanation of the proposed implementation.
- Prefer safe defaults that allow the application to keep running with degraded behavior.

## Implementation Pattern

When implementing a feature that depends on external data:

1. Create or update a service in `services/` for the network or infrastructure access.
2. Add `try/except` around the external call.
3. Log failures with `logging`.
4. Define constants at the top of the file for fixed values.
5. Create or update a controller in `controllers/` to orchestrate the service and shape the returned data.
6. Provide a fallback result if the external dependency fails.

## Expected Output Behavior

- Propose file placement that follows the `services/` and `controllers/` split.
- Call out any missing fallback strategy before finalizing the solution.
- Flag violations if existing code mixes controller and service responsibilities.
- Refactor toward this architecture when the user asks for improvements or when a new feature is being added.

## Example

User request: "Quero buscar dados de clima."

- Create `WeatherService` in `services/` for the external fetch.
- Create `WeatherController` in `controllers/` to process and return the data.
- Add type hints to all functions.
- Define constants such as timeout and default city at the top of the file.
- Wrap the HTTP call in `try/except`.
- Use `logging.exception(...)` or another `logging` call for failures.
- Return a fallback weather payload if the API is unavailable.
