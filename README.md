# SOC Brute-Force Detection and Investigation

## Overview
This project demonstrates a beginner Security Operations Centre (SOC) workflow for analysing Windows failed logon events and identifying potentially suspicious authentication patterns.

## Objectives
- Understand Windows Security Event ID 4625 (failed logon).
- Analyse authentication events and identify repeated failures.
- Develop detection logic for suspicious login patterns.
- Document findings and recommend security improvements.

## Tools and Technologies
- Windows Event Viewer
- Windows Security Logs
- Python (planned)
- Git and GitHub
- MITRE ATT&CK (for evidence-based technique mapping)

## Methodology
1. Collect and review relevant Windows authentication events.
2. Examine timestamps, account names, logon types and status codes.
3. Look for repeated failures within a defined time window.
4. Correlate related events before classifying activity.
5. Document findings, limitations and recommendations.

## Current Progress
- [x] GitHub repository created
- [x] Initial Windows failed-logon events reviewed
- [ ] Sanitised sample dataset prepared
- [ ] Detection script implemented and tested
- [ ] Investigation report completed

## Important Note
Repeated failed logons do not automatically prove a brute-force attack. Findings must be validated using event context and supporting evidence. Public examples will use sanitised or synthetic data.

## Disclaimer
This project is for educational and defensive cybersecurity purposes. Testing will be limited to systems and environments I am authorised to use.
