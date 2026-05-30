from __future__ import annotations


IDENTITIES = {
    "shared_kitchen_host": {
        "title": "Shared Kitchen Host",
        "challenge_type": "Connection Challenge",
        "task_id": "shared_kitchen_host_task",
        "short_description": "Create one small moment of warmth in a shared everyday space.",
        "story": (
            "Today, you are someone who makes ordinary places feel easier to enter. "
            "You do not need to become the center of attention. Your role is to make "
            "one small invitation feel possible."
        ),
    },
    "bike_messenger": {
        "title": "Bike Messenger",
        "challenge_type": "Connection Challenge",
        "task_id": "bike_messenger_task",
        "short_description": "Notice the small signals that help people move through the city.",
        "story": (
            "Today, you are a messenger moving through Amsterdam with attention. "
            "Your job is to collect one helpful observation and pass it forward."
        ),
    },
    "canal_letter_writer": {
        "title": "Canal Letter Writer",
        "challenge_type": "Belonging Challenge",
        "task_id": "canal_letter_writer_task",
        "short_description": "Write a quiet message from one city edge to another.",
        "story": (
            "Today, you are not just a student walking through Amsterdam. You are "
            "someone collecting quiet messages from the city, one canal at a time."
        ),
    },
    "city_signal_collector": {
        "title": "City Signal Collector",
        "challenge_type": "Belonging Challenge",
        "task_id": "city_signal_collector_task",
        "short_description": "Find signs that the city is already making room for you.",
        "story": (
            "Today, you are a collector of signals. Your role is to notice small "
            "proof that belonging can be built from repeated contact with a place."
        ),
    },
    "museum_apprentice": {
        "title": "Museum Apprentice",
        "challenge_type": "Value Challenge",
        "task_id": "museum_apprentice_task",
        "short_description": "Enter a cultural space as someone with a viewpoint worth bringing.",
        "story": (
            "Today, you are an apprentice of attention. You are here to notice what "
            "only you would notice, and to treat your viewpoint as part of the city."
        ),
    },
    "second_hand_explorer": {
        "title": "Second-hand Explorer",
        "challenge_type": "Value Challenge",
        "task_id": "second_hand_explorer_task",
        "short_description": "Find an object that carries a story and connect it to your own.",
        "story": (
            "Today, you are an explorer of objects with previous lives. Your role is "
            "to find something small and let it remind you that value can travel."
        ),
    },
}


IDENTITIES_BY_CHALLENGE = {
    challenge_type: [
        identity_id
        for identity_id, identity in IDENTITIES.items()
        if identity["challenge_type"] == challenge_type
    ]
    for challenge_type in {
        "Connection Challenge",
        "Belonging Challenge",
        "Value Challenge",
    }
}


CHALLENGE_EXPLANATIONS = {
    "Connection Challenge": (
        "You may want more everyday contact with people, but the first step into a "
        "new social moment can feel unclear."
    ),
    "Belonging Challenge": (
        "You may be looking for a stronger emotional connection with Amsterdam, "
        "rather than only knowing how to move through it."
    ),
    "Value Challenge": (
        "You may be asking where your perspective, skills, or presence fit into "
        "this city right now."
    ),
}
