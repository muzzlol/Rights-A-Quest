define v = Character('Vikram', color="#c8ffc8")
define l = Character('Landlord', color="#f9ffca")

label start:
    scene bg apartment
    show landlord at right
    show vikram at left
    
    l "I'm glad you like the apartment, Vikram. Just sign here, and it's all yours."
    
    v "I see there's a clause here about a 'no visitors after 9 PM' policy and an unexpected monthly maintenance fee. We didn't discuss these terms earlier."
    menu:
        "Sign the agreement without objecting":
            jump sign_without_objection
            
        "Question the landlord about the new terms":
            jump question_landlord
            
        "Suggest revising the agreement":
            jump suggest_revising
label sign_without_objection:
    v "Alright, I'll sign it."
    l "Excellent! I'm sure you won't regret this."
    # Outcome narration
    "A few weeks later, Vikram is fined for having friends over past 9 PM, and the added fees strain his budget."
    "Vikram learns the hard way about the importance of thoroughly reviewing and negotiating rental agreements before signing."
    return
label question_landlord:
    v "These terms weren't mentioned before. Can you explain why they're included now?"
    l "Ah, those are standard policies. Don't worry about it."
    
    menu:
        "Accept the landlord's explanation and sign":
            jump sign_without_objection
            
        "Refuse to sign until the terms are discussed further":
            jump refuse_to_sign
label refuse_to_sign:
    v "I'm uncomfortable signing this with terms I wasn't aware of. Let's discuss a fair solution."
    l "I see your point. Let's go over it together and make the necessary changes."
    # Outcome narration
    "Vikram's insistence on discussing the terms leads to a better understanding and a more equitable rental agreement."
    return
label suggest_revising:
    v "I believe we need to revise these terms. They weren't part of our initial agreement."
    l "I see your point. Let's go over it together and make the necessary changes."
    # Outcome narration
    "This choice demonstrates the importance of negotiation and understanding one's rights, resulting in a positive living situation for Vikram."
    return
