# CTRL-CREATE

CTRL-CREATE is an AI-assisted support and emergency routing prototype designed to identify distress indicators from user input and route verified cases toward appropriate support.

## Project Flow

Voice Input
↓
Speech-to-Text
↓
Text Input
↓
NLP Analysis
↓
Distress Score
↓
Severity Score
↓
Human Verification
↓
Case Routing
↓
Active Emergency / Past Experience

## Features

- Voice input processing
- Speech-to-text conversion using Whisper
- Multilingual NLP analysis
- Distress score calculation
- Severity classification
- Mandatory human verification
- Emergency service routing
- Certified counsellor routing
- DLSA legal aid routing

## Emergency Routing

Verified active emergency cases can be routed toward:

- Police
- Fire Service
- Ambulance

## Support Routing

Past experience cases can be routed toward:

- Certified Counsellor
- DLSA Legal Aid

## Safety

The system is designed as an AI-assisted decision-support prototype.

AI-generated distress indicators and severity estimates do not independently trigger emergency action. Human verification is required before routing.

## Technologies

- Python
- Hugging Face Transformers
- Whisper
- NLP
- PyTorch

## Project Status

This repository contains a working prototype of the core workflow.

Some planned integrations such as real-time location sharing, external emergency-service APIs, production-grade NLP models, and external counselling/legal-aid integrations are not yet implemented.
