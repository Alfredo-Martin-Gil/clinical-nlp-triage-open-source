# Failure-Behaviour Requirements Draft — v0.1

## Status

This document is **requirements and governance scaffolding for future
research**. It does not describe implemented failure handling. The current
v0.3 prototype processes synthetic text offline and has no sensors, cloud
model, uncertainty engine, patient interface, or authorized clinical use.

## Current implemented behaviour

- malformed CSV schemas raise an error;
- literal configured-term matches are counted;
- zero hits produce `no_lexicon_signal_detected`;
- every row states that clinical risk is not established and patient use is
  prohibited;
- negation handling is explicitly marked `not_implemented`.

The engine does not detect missing clinical information, data corruption,
sensor failure, service degradation, or high clinical uncertainty.

## Candidate requirements for future research

A future version would need verified requirements for:

1. explicit invalid-input and degraded-state outputs;
2. separation of no detected signal from evidence of absence;
3. no automatic downgrade when required information is missing;
4. traceable failure reason codes;
5. conservative stopping behaviour when an output cannot be supported;
6. human-factors testing of warnings and abandonment behaviour.

## Prohibited interpretation

This draft must not be cited as evidence that failure controls are implemented,
effective, safe, validated, or suitable for remote or resource-limited use.

## Evidence needed

- implemented requirements linked to tests;
- predefined acceptance criteria;
- adversarial and boundary-case evaluation;
- clinical and human-factors review;
- representative, governed data and independent reference processes;
- change-control and residual-risk decisions by accountable organizations.
