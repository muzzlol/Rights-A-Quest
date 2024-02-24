define v = Character('Vikram', color="#c8ffc8")
define l = Character('Landlord', color="#f9ffca")

# Define characters and their expressions
define p = Character('Priya', color="#c8ffc8")
define b = Character('Brother', color="#f9ffca")
define a = Character('Anonymous', color="#000000")


image vikram concerned:
    "vikram concerned.png"
    zoom 1.5
image vikram neutral:
    "vikram neutral.png"
    zoom 1.5
image landlord groan:
    "landlord groan.png"
    zoom 1.5
image landlord smug:
    "landlord smug.png"
    zoom 1.5
image landlord neutral:
    "landlord neutral.png"
    zoom 1.5
# Define images for Priya's expressions and the anonymous character
image priya happy:
    "priya happy.png" 
    zoom 1.5
image priya worried:
    "priya worried.png"
    zoom 1.5
image priya worried:
    "priya worried.png"
    zoom 1.5
image priya angry:
    "priya angry.png"
    zoom 1.5
image priya consulted:
    "priya consulted.png"
    zoom 1.5
    
image anonymous:
    "anonymous.png"
    zoom 1.5
image brother neutral:
    'brother neutral.png'
    zoom 1.5

label start:
    play music "audio/steinsgate.mp3" volume 0.3
    

    menu:
        "scenario : cyberbullying":
            jump cyberbully

        "scenario : dormatory rental agreement":
            jump dorm
        
        "scenario : "
    label dorm:
        scene bg apartment
        show landlord neutral at right
        show vikram concerned at left
        
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
        show vikram concerned at left
        with dissolve
        v "Alright, I'll sign it."
        show landlord smug at right
        with dissolve
        l "Excellent! I'm sure you won't regret this."
        hide vikram concerned at left 
        with dissolve
        hide landlord smug at right
        with dissolve
        # Outcome narration
        "A few weeks later, Vikram is fined for having friends over past 9 PM, and the added fees strain his budget."
        "Vikram learns the hard way about the importance of thoroughly reviewing and negotiating rental agreements before signing."
        return
    label question_landlord:
        v "These terms weren't mentioned before. Can you explain why they're included now?"
        show landlord groan at right
        with dissolve
        l "Ah, those are standard policies. Don't worry about it."
        
        menu:
            "Accept the landlord's explanation and sign":
                jump sign_without_objection
                
            "Refuse to sign until the terms are discussed further":
                jump refuse_to_sign
    label refuse_to_sign:
        v "I'm uncomfortable signing this with terms I wasn't aware of. Let's discuss a fair solution."
        show landlord neutral at left
        with dissolve
        l "I see your point. Let's go over it together and make the necessary changes."
        hide vikram concerned at left
        with dissolve
        hide landlord neutral at right
        with dissolve

        # Outcome narration
        "Vikram's insistence on discussing the terms leads to a better understanding and a more equitable rental agreement."
        return
    label suggest_revising:
        show vikram neutral at left
        with dissolve
        v "I believe we need to revise these terms. They weren't part of our initial agreement."
        show landlord neutral at right
        with dissolve
        l "I see your point. Let's go over it together and make the necessary changes."
        hide vikram neutral at left
        with dissolve
        hide landlord neutral at left
        with dissolve
        # Outcome narration
        "This choice demonstrates the importance of negotiation and understanding one's rights, resulting in a positive living situation for Vikram."
        return

    # Assuming the previous scene has concluded
    hide vikram with fade
    hide landlord with fade

    label cyberbully:

        # Transition to Priya's scenario
        scene bg pinkroom
        show priya worried at center

        p "Who would do such a thing? And why me?"

        # Simulate receiving a message
        scene bg dimly-lit-room
        show anonymous at center
        a "Not so confident now, are you? 😈"

        scene bg pinkroom
        show priya worried at center
        p "(typing, defiant yet scared) Who are you? Why are you doing this? Please stop."

        scene bg dimly-lit-room
        show anonymous at center
        a "It's fun seeing you squirm. You can't hide from me. 🐍"
        scene bg pinkroom
        show priya worried at center
        p "(murmuring to herself) I can't just sit here and take this. But what can I do?"

        menu:
            "Option 1: Block the harasser and ignore the messages.":
                show priya worried at center
                p "It's not stopping. What have I done to deserve this?"
                # Outcome narration
                "The harassment continues, leaving Priya feeling even more vulnerable and alone."
                jump after_conversation

            "Option 2: Respond aggressively to the harasser.":
                show priya angry at center
                p "(typing, angry) Leave me alone! You have no power over me!"
                scene bg dimly-lit-room
                show anonymous at center
                a "Oh, it's on now. You'll regret that. 😡"
                # Outcome narration
                "The situation escalates, and Priya finds herself facing even more intense harassment."
                jump after_conversation

            "Option 3: Report the harassment to the platform and tell a trusted adult.":
                # Transition to the kitchen scene for a conversation with the brother
                scene bg kitchen
                show priya consulted at left
                show brother neutral at right
                p "(to her brother, hopeful yet nervous) I've been getting these awful messages. I reported it, and... I don't know what to do."
                b "You did the right thing. Let's make sure this person can't hurt you anymore. We're in this together."
                # Outcome narration
                "Priya feels supported and empowered, taking the first steps toward addressing the harassment in a healthy and constructive manner."
                jump after_conversation

        label after_conversation:
            hide priya
            hide anonymous
            hide brother
            # Conclusion of the scenario
            "No matter the choice, Priya learns about the harsh realities of cyberbullying and the importance of taking action."
            return
 
