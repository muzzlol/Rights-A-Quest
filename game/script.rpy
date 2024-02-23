label start:
    scene bg dorm
    show vikram neutral at center
    show landlord happy at right

    "Landlord: \"I'm glad you like the dorm, Vikram. Just sign here, and it's all yours.\""

    show vikram concerned
    "Vikram notices something concerning in the agreement."
    "Vikram: \"I see there's a clause here about a 'no visitors after 9 PM' policy and an unexpected monthly maintenance fee. We didn't discuss these terms earlier.\""

    menu:
        "How should Vikram respond?":
            "Sign the agreement without objecting.":
                jump sign_without_objection

            "Question the landlord about the new terms.":
                jump question_landlord

            "Suggest revising the agreement.":
                jump suggest_revising

label sign_without_objection:
    "Vikram signs the agreement, feeling uneasy."
    "A few weeks later, he's fined for having friends over past 9 PM, and the added fees strain his budget."
    "Outcome: Vikram learns the hard way about the importance of thoroughly reviewing and negotiating rental agreements before signing."
    jump end_scenario

label question_landlord:
    "Vikram: \"These terms weren't mentioned before. Can you explain why they're included now?\""
    "Landlord: \"Ah, those are standard policies. Don't worry about it.\""
