from __future__ import annotations


TASKS = {
    "shared_kitchen_host_task": {
        "identity_id": "shared_kitchen_host",
        "title": "Make One Small Invitation",
        "mission": (
            "In a shared kitchen, common room, cafe, or study space, create one tiny "
            "opening for connection. This can be asking someone what they are making, "
            "offering a seat, or sharing one useful local tip."
        ),
        "location": "A shared kitchen, campus common room, cafe, or study space.",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=student+cafe+Amsterdam",
        "safety_note": (
            "Keep it brief and optional. If someone seems busy or uninterested, simply "
            "continue with your day."
        ),
        "reflection_prompt": "What made the interaction easier or harder than expected?",
        "pass_forward_prompt": "Leave one low-pressure opening line for the next Shared Kitchen Host.",
    },
    "bike_messenger_task": {
        "identity_id": "bike_messenger",
        "title": "Collect a Helpful Route Signal",
        "mission": (
            "Take a short walk or bike ride along a route you often use. Notice one "
            "thing that would help a newcomer: a calmer crossing, a safer bike lane, "
            "a useful landmark, or a place to pause."
        ),
        "location": "A familiar route near your home, campus, or daily commute.",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=Amsterdam+bike+route",
        "safety_note": "Do not use your phone while biking. Stop safely before writing anything down.",
        "reflection_prompt": "What did this route teach you about moving through Amsterdam?",
        "pass_forward_prompt": "Leave one route tip for the next Bike Messenger.",
    },
    "canal_letter_writer_task": {
        "identity_id": "canal_letter_writer",
        "title": "Write From the Canal Edge",
        "mission": (
            "Find a quiet canal spot. Sit or stand there for ten minutes. Write one "
            "sentence to someone who will arrive in Amsterdam after you."
        ),
        "location": "Any canal near your campus, home, or a place you pass often.",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=quiet+canal+Amsterdam",
        "safety_note": "Choose a public, well-lit place where you feel comfortable staying for a few minutes.",
        "reflection_prompt": "What did this place make you feel?",
        "pass_forward_prompt": "Leave one sentence for the next Canal Letter Writer.",
    },
    "city_signal_collector_task": {
        "identity_id": "city_signal_collector",
        "title": "Find Three Belonging Signals",
        "mission": (
            "Walk for fifteen minutes and collect three small signals that people are "
            "making space for one another: a sign, a bench, a public notice, a library "
            "corner, a shop window, or a kind gesture."
        ),
        "location": "A street, library, market, or neighborhood square in Amsterdam.",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=public+library+Amsterdam",
        "safety_note": "Stay in public spaces and avoid photographing strangers without permission.",
        "reflection_prompt": "Which signal felt most welcoming, and why?",
        "pass_forward_prompt": "Leave one place where the next City Signal Collector should look.",
    },
    "museum_apprentice_task": {
        "identity_id": "museum_apprentice",
        "title": "Choose One Object That Notices You Back",
        "mission": (
            "Visit a museum, gallery, public artwork, or campus exhibition. Choose one "
            "object or image and write what you noticed that someone else might miss."
        ),
        "location": "A museum, gallery, public artwork, or free campus exhibition.",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=free+museum+Amsterdam",
        "safety_note": "Check opening hours and costs before you go. A public artwork is enough for this demo.",
        "reflection_prompt": "What did your viewpoint add to the object?",
        "pass_forward_prompt": "Leave one observation prompt for the next Museum Apprentice.",
    },
    "second_hand_explorer_task": {
        "identity_id": "second_hand_explorer",
        "title": "Find an Object With a Previous Life",
        "mission": (
            "Visit a second-hand shop, swap shelf, market, or free library. Find one "
            "object that seems to carry a story. You do not need to buy it."
        ),
        "location": "A second-hand shop, market, swap shelf, or free library.",
        "maps_url": "https://www.google.com/maps/search/?api=1&query=second+hand+shop+Amsterdam",
        "safety_note": "Only go during normal opening hours and keep the task small.",
        "reflection_prompt": "What story did you imagine for this object, and how did it connect to you?",
        "pass_forward_prompt": "Leave one object-hunting tip for the next Second-hand Explorer.",
    },
}
