label bangovore_four_bryce3_mcbottom_train_epilogue:
    Br flirty "How would you feel about riding in the \"belly of the beast\"?"
    c "What do you mean?"
    Br normal "My belly, obviously."
    c "Inside you?"
    Br "Yeah. What else do you think I mean?"

    menu:
        "I'd like to not get eaten, thanks.":
            label bangovore_four_bryce3_reject:
            $ renpy.pause (0.5)
            Br laugh "I'd cough you back up!"
            c "Bryce."
            Br normal "Sorry, sorry. Let me try the next idea."
            jump bangovore_four_bryce3_mcbottom_train_epilogue_return
        "Sebastian mentioned dragons could do something like that..." if bangovore_four_xsebastian_undiscussed == False:
            $ renpy.pause (0.5)
            Br normal "Did he now?"
            Br flirty "Did you two do anything?"
            if bangovore_four_xsebastian_unplayed == False:
                $ renpy.pause (0.5)
                c "... yes."
                Br laugh "Great! Well I'm an even more comfortable ride."
            else:
                menu:
                    "No, of course not! Don't eat me, please!":
                        jump bangovore_four_bryce3_reject
                    "Well... no.":
                        $ renpy.pause (0.5)
                Br flirty "Would you like to?"
                c "To get eaten?"
                Br normal "I'd cough you back up."

        "Is that safe?" if bangovore_four_xsebastian_undiscussed == True:
            $ renpy.pause (0.5)
            Br laugh "Would I be suggesting it if it weren't?"
            Br smirk "I'd cough you back up. You'll be fine."
            c "In pieces?"
            Br brow "No, whole. What, did you think I was going to tear you apart?"
            Br laugh "That'd kinda defeat the work the department's gone through protecting you the past week or so."
            c "I guess..."

    menu:
        "Accept.":
            c "Alright. You only live once, right?"
            Br smirk "That's the spirit!"
        "Reject.":
            c "No, thanks."
            Br brow "Fine, fine. Let me try the next idea."
            jump bangovore_four_bryce3_mcbottom_train_epilogue_return

    $ renpy.pause (0.8)
    show bryce stern with dissolvemed
    m "Bryce took a deep breath, then his throat began to undulate."
    $ renpy.pause (0.8)
    c "What are you doing?"
    Br normal "Swallowing air. You want to be able to breathe in there, right?"
    c "Oh. Right."
    $ renpy.pause (1.0)
    show bryce flirty with dissolve
    $ renpy.pause (0.5)

    hide bryce with dissolvemed
    m "After a few more seconds of this, Bryce winked, then circled around behind me."
    c "Wait, we're going just like that?"
    Br laugh "Hey, you said yes to this."
    c "I... I guess I did."

    scene black with CropMove(0.5, "wipedown")
    m "His maw opening around my head left me no room to back out."
    play soundloop "fx/bangovore/dragongulping.ogg"
    m "My head entered his throat, squeezed on all sides by the slimy walls of his esophagus while he struggled with my shoulders."

    if (bangok_four_bryce3_store.protection == False) or (bangok_four_bryce3_store.brycebroke == True) or (bangok_four_bryce3_store.mavbroke == True):
        if persistent.bangok_inflation == True:
            m "Pinning my arms to my sides, his teeth scraped down my torso, toward my belly bulging with draconic fluids."
        elif bangok_four_bryce3_store.brycetarget == "ass":
            m "Pinning my arms to my sides, his teeth scraped down my torso, toward my rear, still leaking draconic fluids."
        else:
            m "Pinning my arms to my sides, his teeth scraped down my torso, toward my lower lips, still leaking draconic fluids."
    else:
        m "Pinning my arms to my sides, his teeth scraped down my torso, enveloping my whole upper in his maw."

    stop soundloop fadeout 1.5
    $ renpy.pause (1.5)
    Br stern "Hrk!"
    m "My whole world flipped upside down as Bryce lifted my legs into the air, using gravity to slide me down the slick lining of his throat."
    



