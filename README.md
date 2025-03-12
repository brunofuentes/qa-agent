# QA-Agent

A multi-step AI Agent System for QA Testing.

## Overview

QA-Agent uses multiple AI agents to create End-to-End Testing. Each agent handles a specific part of the process, working together to provide better answers than a single AI could.

## Quick Start

1. Install Playwright locally (needed for browser agent): `npm install -g playwright`
2. Clone this repo
3. Install dependencies: `poetry install`
4. Set up API keys in `.env` (Currently: GOOGLE_API_KEY and ANTHROPIC_API_KEY)
5. Run: `poetry run python main.py`

## Development Status

🚧 **This project is currently under active development** 🚧

The project is in its early stages and features are being actively developed. Some functionality may be incomplete or subject to change.

Current focus:
- Validate AI Agent for Gherkin scenario generation
- Validate AI Agent for Browser automation
- Validate AI Agent for Playwright test generation
