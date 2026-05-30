from __future__ import annotations


CHALLENGE_TYPES = [
    "Connection Challenge",
    "Belonging Challenge",
    "Value Challenge",
]


QUESTIONS = [
    {
        "id": "q1_answer",
        "label": "How long have you been living in Amsterdam?",
        "options": [
            "Less than 1 month",
            "1-3 months",
            "3-12 months",
            "More than 1 year",
        ],
        "scores": {},
    },
    {
        "id": "q2_answer",
        "label": "When you enter a new social setting, what shows up first?",
        "options": [
            "I want to meet people, but I do not know how to begin.",
            "I feel like everyone already belongs except me.",
            "I am not sure what value I bring here.",
        ],
        "scores": {
            "I want to meet people, but I do not know how to begin.": {"Connection Challenge": 2},
            "I feel like everyone already belongs except me.": {"Belonging Challenge": 2},
            "I am not sure what value I bring here.": {"Value Challenge": 2},
        },
    },
    {
        "id": "q3_answer",
        "label": "What do you most hope the city can give you right now?",
        "options": [
            "More chances to meet people without pressure.",
            "A feeling that this place can become mine too.",
            "A clearer sense that I have something to contribute.",
        ],
        "scores": {
            "More chances to meet people without pressure.": {"Connection Challenge": 2},
            "A feeling that this place can become mine too.": {"Belonging Challenge": 2},
            "A clearer sense that I have something to contribute.": {"Value Challenge": 2},
        },
    },
    {
        "id": "q4_answer",
        "label": "What feels hardest to do at the moment?",
        "options": [
            "Starting conversations with people I do not know well.",
            "Feeling emotionally at home in familiar places.",
            "Trusting that my presence matters in groups or projects.",
        ],
        "scores": {
            "Starting conversations with people I do not know well.": {"Connection Challenge": 2},
            "Feeling emotionally at home in familiar places.": {"Belonging Challenge": 2},
            "Trusting that my presence matters in groups or projects.": {"Value Challenge": 2},
        },
    },
    {
        "id": "q5_answer",
        "label": "Which kind of task would feel most helpful today?",
        "options": [
            "A small interaction with another person.",
            "A reflective walk or quiet city ritual.",
            "A task that lets me observe, choose, or make meaning.",
        ],
        "scores": {
            "A small interaction with another person.": {"Connection Challenge": 1},
            "A reflective walk or quiet city ritual.": {"Belonging Challenge": 1},
            "A task that lets me observe, choose, or make meaning.": {"Value Challenge": 1},
        },
    },
    {
        "id": "q6_answer",
        "label": "How social should your task be?",
        "options": [
            "Some social contact is okay if it is low pressure.",
            "I would prefer something quiet and independent.",
            "I want something that helps me notice my own point of view.",
        ],
        "scores": {
            "Some social contact is okay if it is low pressure.": {"Connection Challenge": 1},
            "I would prefer something quiet and independent.": {"Belonging Challenge": 1},
            "I want something that helps me notice my own point of view.": {"Value Challenge": 1},
        },
    },
]
