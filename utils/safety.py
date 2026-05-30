from __future__ import annotations


SENSITIVE_TERMS = [
    "suicide",
    "self-harm",
    "kill myself",
    "hurt myself",
    "diagnosis",
    "clinical",
    "therapy",
    "therapist",
    "心理疾病",
    "自杀",
    "自残",
    "诊断",
    "治疗",
]


def flag_sensitive_content(text: str) -> list[str]:
    lowered = text.lower()
    return [term for term in SENSITIVE_TERMS if term.lower() in lowered]
