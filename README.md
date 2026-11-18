# MediLedger AI — Explainable AI Medical Triage & Zero-PII Web3 Health Passport

**Hackathon:** CODEFESTTHON 2026 (Devfolio Online)  
**Tracks:** AI/ML · HealthTech · Web3/Blockchain

## Overview
**MediLedger AI** solves emergency room triage bottlenecks and patient data privacy by combining:
1. **Explainable Clinical AI Triage Engine (`backend/triage_engine.py`)**: Computes transparent urgency tiers (`CRITICAL_IMMEDIATE`, `URGENT_24H`, `ROUTINE_OUTPATIENT`) from symptom severity and vital anomalies (SpO2 hypoxia, tachycardia, pyrexia).
2. **Zero-PII On-Chain Health Passport**: Generates deterministic SHA-256 medical attestation proofs (`0x...`) without exposing raw patient identity on-chain.

## Run Locally & Test
```bash
python -m unittest discover -s tests -v
python backend/triage_engine.py
```
Then visit `http://127.0.0.1:8084`.
