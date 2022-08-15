init python in bangovore_four_anna4:
    autocannibalism = False

    chestcavity_unasked = True
    rib_uneaten = True
    liver_uneaten = True
    round_uneaten = True
    rump_uneaten = True
    groin_uneaten = True

    blood_loss = 0
    player_awoken = 0


label bangovore_four_anna4_bloodloss_check:
    python in bangovore_four_anna4:
        if rib_uneaten == False:
            blood_loss += 0.02
        if liver_uneaten == False:
            blood_loss += 0.10
        if round_uneaten == False:
            blood_loss += 0.12
        if rump_uneaten == False:
            blood_loss += 0.05
        if groin_uneaten == False:
            blood_loss += 0.12

    show grey:
        alpha (bangovore_four_anna4.blood_loss)
    with dissolvemed

    if bangovore_four_anna4.blood_loss <= 0:
        m "I breathed in, then out. So far I felt fine, though I knew that was very soon to change."
    elif bangovore_four_anna4.blood_loss < 0.05:
        m "My open wound ached dully, blood dribbling out to stain the couch."
    elif bangovore_four_anna4.blood_loss < 0.10:
        m "Blood glistened across my lower body. My blood."
    elif bangovore_four_anna4.blood_loss < 0.15:
        m "The couch was ruined by this point, stained and spattered with my blood as my open flesh throbbed."
    elif bangovore_four_anna4.blood_loss < 0.20:
        m "The couch beneath my rear was slick with my blood, my lower body soaked. I was astonished I still felt so close to fine with gaping holes in me."
    elif bangovore_four_anna4.blood_loss < 0.25:
        m "Lightheadedness took hold, and I slipped a little in my blood slickening the couch cushions."
    elif bangovore_four_anna4.blood_loss < 0.30:
        m "I could feel droplets of blood running down my numb feet, but my energy to move my legs or deal with the sensation was gone."
    elif bangovore_four_anna4.blood_loss < 0.35:
        show black with dissolve
        $ renpy.pause (0.1)
        hide black with dissolve
        m "I blinked for just a moment, but when I reopened my eyes my vision already felt dimmer, fading away."
    elif bangovore_four_anna4.blood_loss < 0.40:
        m "My heart beat a mile a minute, trying to pump the diminishing volume of blood in my veins."
    else:
        if bangovore_four_anna4.player_awoken == 0:
            $ bangovore_four_anna4.player_awoken = 1
            show black with dissolveslow
            An rage c "Hey!"
            show anna sad c
            hide black
            with dissolve
            An "Don't quit on me yet. There's still more to sample."
            m "My response was definitely unintelligible, an exhausted mutter."
        elif bangovore_four_anna4.player_awoken == 1:
            show black
            show anna sad c
            with dissolveslow
            $ bangovore_four_anna4.player_awoken = 2
            play sound "fx/slap1.wav"
            hide black with None
            m "Her claws left scratches across my face where she slapped me."
            An "Just a little longer. Please?"
            menu:
                "N... No more.":
                    $ renpy.pause (0.5)
                    An "..."
                    An normal c "Alright."

                    $ renpy.pop_call()

                    jump bangovore_four_anna4_kiss_of_death_messy
                "...trying...":
                    $ renpy.pause (0.5)
        else:
            $ renpy.pause (0.5)
            show anna sad c
            show black
            with dissolveslow
            $ renpy.pause (0.5)
            An "...[player_name]?"
            stop music fadeout 2.0

            $ renpy.pause (0.5)
            play sound "fx/slap1.wav"
            $ renpy.pause (0.8)
            play sound "fx/slap2.wav"
            $ renpy.pause (0.8)

            An sad c "..."
            $ renpy.pause (0.8)
            An sad c "...Thank you."
            jump bangovore_four_anna4_epilogue
    return

label bangovore_four_anna4:
    m "Her claw lingered along my clavicle."
    An "What if we took this even farther?"

    c "Farther than sex? That is what you meant, right?"
    c "How far are you talking?"

    An smirk "Fuck the council. If they're going to arrest me anyway, why don't I bring something of theirs crashing down first?"
    An normal "Your people need our generators badly, don't you? Or you wouldn't be taking such a lopsided deal. We could undermine the dragon position."
    An sad "And it would make sure that I'm not alone when I die."

    c "What are you talking about?"

    An smirk "I'm talking about eating you."

    menu:
        "No!":
            c "I'd very much prefer not to be eaten, thank you!"
            c "Can we have sex without you suggesting killing me?!"
            jump bangovore_four_anna4_return
        "... Oh.":
            $ renpy.pause (0.5)
            An "You know, most people would reject that out of hand."
            c "Yeah, I... guess they would."
            An "But you don't."
            c "Maybe."
            An normal "If I mean so much to you, why not make it permanent? Become part of me? Fuck all your responsibilities?"
            menu:
                "Accept.":
                    pass
                "Reject.":
                    c "There's more than just the deal at stake, Anna. I... I can't."
                    show anna sad with dissolve
                    $ renpy.pause (0.5)
                    An "Will you at least fuck me?"
                    c "I don't know. It's a hell of a mood killer you just brought up."
                    m "She tugged on my neckline again, straining the top button."
                    c "H-Hey! I told you I'd do that!"
                    jump bangovore_four_anna4_return



    c "Okay. There's just... something I should tell you first. A responsibility I have to pass on."
    An sad "Fine. What?"
    c "There's a meteor coming to wipe out dragonkind, in a couple of weeks."
    c "Your people can stop it, but all your generators put together won't be enough power. You'll need the help of the generators in the underground facility, powering the portal right now."
    An face "And you didn't think to mention this to anybody until me, now?"
    c "It's... complicated. I only found out recently anyway."
    An sad "I see."
    An normal "Well, maybe bringing those generators and your warning to the council will buy me some brief period longer of freedom."
    An sad "But it won't save me."
    An smirk "So fuck them. I want you in me."
    c "I want that too."

    # TODO: Ripping sound effect.
    m "Anna tore through the buttons of my shirt, her clawtip leaving an angry red scratch down my torso."
    if bangok_four_playerhasdick is None:
        m "Then she poked her claws into the waistband of my pants, tearing open my crotch to reveal..."
        menu:
            "Then she poked her claws into the waistband of my pants, tearing open my crotch to reveal..."
            "My rock-hard shaft.":
                $ bangok_four_playerhasdick = True
                m "Then she poked her claws into the waistband of my pants, tearing open my crotch to reveal{fast} my rock-hard shaft."
            "My slick, dampening pussy.":
                $ bangok_four_playerhasdick = True
                m "Then she poked her claws into the waistband of my pants, tearing open my crotch to reveal{fast} my slick, dampening pussy."
    
    elif bangok_four_playerhasdick == True:
        m "Then she poked her claws into the waistband of my pants, tearing open my crotch to reveal my rock-hard shaft."
    else:
        m "Then she poked her claws into the waistband of my pants, tearing open my crotch to reveal my slick, dampening pussy."

    An "You're turned on by this."
    if bangok_four_playerhasdick == True:
        m "She ran a claw along the bottom of my shaft, drawing out a drop of pre."
        An "This will make a nice snack."

    play sound "fx/undress.ogg"
    $ renpy.pause (0.5)
    m "I kicked off the remains of my ruined clothes, standing naked before Anna."

    # An normal "Want to do something pleasurable first?"
    # An smirk "One last fuck?"

    # menu:
    #     "Accept.":
    #         jump todo_bangovore_four_anna4_out_of_content
    #     "Reject.":
    #         c "No. I'm ready."
    #         An smirk "Good."

    $ renpy.pause (0.5)
    An "Now we have so many choices."
    An normal "Are you afraid of a bit of pain, [player_name]? Want to go out quickly?"
    An smirk "Or do you want it to go slowly? Maybe even try a little of yourself along the way?"

    menu:
        "I'll try a bit.":
            $ renpy.pause (0.5)
            $ bangovore_four_anna4.autocannibalism = True
            An smirk "Cute."
        "I'm all yours.":
            $ renpy.pause (0.5)
            $ bangovore_four_anna4.autocannibalism = False
            An normal "Suit yourself."
        "Just put me out quickly.":
            $ renpy.pause (0.5)
            An sad "..."
            $ renpy.pause (0.5)
            An "Are you sure? There's no going back to going slow once we go fast. You'll be..."
            menu:
                "I'm sure.":
                    $ renpy.pause (0.5)
                    jump bangovore_four_anna4_kiss_of_death_clean
                # "I'm not sure.":
                #     jump todo_bangovore_four_anna4_out_of_content

    show o:
        ypos -300
    with ease
    show anna normal:
        zoom 1.2
        ypos 1.1
    with ease
    m "Taking me by the hand, Anna led me over to the couch, then pushed me down into the seat."
    m "She handed me one of the pillows."
    An "Bite the corner if you feel like making too much noise."

label bangovore_four_anna4_chow_down:
    if bangovore_four_anna4.blood_loss <= 0:
        if bangovore_four_anna4.autocannibalism == True:
            An smirk "So many places to sample. Where do you want to start?"
        else:
            An smirk "So many places to sample. Where do you want me to start?"

    call bangovore_four_anna4_bloodloss_check from bangovore_four_anna4_chow_down_bloodloss_check

    if bangovore_four_anna4.blood_loss < 0.4:
        label bangovore_four_anna4_chow_down_menu1_pagination:
        menu:
            "Rib." if bangovore_four_anna4.rib_uneaten == True:
                $ bangovore_four_anna4.rib_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "Liver." if bangovore_four_anna4.liver_uneaten == True:
                $ bangovore_four_anna4.liver_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "Heart." if bangovore_four_anna4.chestcavity_unasked == True:
                jump bangovore_four_anna4_chow_down_chestcavity
            "Lung." if bangovore_four_anna4.chestcavity_unasked == True:
                jump bangovore_four_anna4_chow_down_chestcavity
            "Leg." if bangovore_four_anna4.round_uneaten == True:
                $ bangovore_four_anna4.round_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "Rump." if bangovore_four_anna4.rump_uneaten == True:
                $ bangovore_four_anna4.rump_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "Groin." if bangovore_four_anna4.groin_uneaten == True:
                jump bangovore_four_anna4_chow_down_groin
            "Wherever you like.":
                if bangovore_four_anna4.groin_uneaten == True:
                    if bangok_four_playerhasdick == True:
                        if bangovore_four_anna4.blood_loss < 0.1:
                            m "Anna cupped my balls, flicking my hard shaft with a claw."
                        elif bangovore_four_anna4.blood_loss < 0.2:
                            m "Anna cupped my balls, flicking my limpening shaft with a claw."
                        else:
                            m "Anna cupped my balls, flicking my soft shaft with a claw."
                    else:
                        m "Anna rubbed her palm over my lower lips."
                    An "You're not going to need this anymore. Since you're giving me the choice..."
                    jump bangovore_four_anna4_chow_down_groin

    else:
        label bangovore_four_anna4_chow_down_menu2_pagination:
        menu:
            "... rib..." if bangovore_four_anna4.rib_uneaten == True:
                $ bangovore_four_anna4.rib_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "... liver..." if bangovore_four_anna4.liver_uneaten == True:
                $ bangovore_four_anna4.liver_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "... heart..." if bangovore_four_anna4.chestcavity_unasked == True:
                jump bangovore_four_anna4_chow_down_chestcavity
            "... lung..." if bangovore_four_anna4.chestcavity_unasked == True:
                jump bangovore_four_anna4_chow_down_chestcavity
            "... leg..." if bangovore_four_anna4.round_uneaten == True:
                $ bangovore_four_anna4.round_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "... rump..." if bangovore_four_anna4.rump_uneaten == True:
                $ bangovore_four_anna4.rump_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "... groin..." if bangovore_four_anna4.groin_uneaten == True:
                $ bangovore_four_anna4.groin_uneaten = False
                jump todo_bangovore_four_anna4_out_of_content
            "... don't... care..." if bangovore_four_anna4.player_awoken == 0:
                jump bangovore_four_anna4_chow_down
            "... wherever..." if bangovore_four_anna4.player_awoken == 1:
                jump bangovore_four_anna4_chow_down
    jump bangovore_four_anna4_chow_down


label bangovore_four_anna4_chow_down_chestcavity:
    $ renpy.pause (0.5)
    $ bangovore_four_anna4.chestcavity_unasked = False
    m "Anna ran a claw along my left clavicle."
    if bangovore_four_anna4.blood_loss > 0:
        show anna sad c with dissolve
    else:
        show annna sad with dissolve
    An "Getting through your ribcage would {i}hurt{/i}... more than I'm trying to hurt you while you're still conscious."
    An "Let's stick to what I can carve out for now."

    jump bangovore_four_anna4_chow_down


label bangovore_four_anna4_chow_down_groin:
    $ renpy.pause (0.5)
    $ bangovore_four_anna4.groin_uneaten = False
    hide anna with easeoutbottom
    m "Anna nestled her head between my legs, flicking her tongue over my soonn-to-be removed genitals."
    if bangovore_four_anna4.blood_loss <= 0:
        An smirk "Fast or slow? Claws or teeth?"
        menu:
            "Claws.":
                jump bangovore_four_anna4_chow_down_groin_claws
            "Teeth.":
                jump bangovore_four_anna4_chow_down_groin_teeth
            "Which would you prefer?":
                An normal "None of this carving nonsense. We'll do it the natural way."
                jump bangovore_four_anna4_chow_down_groin_teeth
    if bangovore_four_anna4.blood_loss < 0.4:
        An smirk c "Fast or slow? Claws or teeth?"
        menu:
            "Claws.":
                jump bangovore_four_anna4_chow_down_groin_claws
            "Teeth.":
                jump bangovore_four_anna4_chow_down_groin_teeth
            "Which would you prefer?":
                An normal c "None of this carving nonsense. We'll do it the natural way."
                jump bangovore_four_anna4_chow_down_groin_teeth
    else:
        jump bangovore_four_anna4_chow_down_groin_teeth

label bangovore_four_anna4_chow_down_groin_teeth:
    if bangovore_four_anna4.blood_loss < 0.4:
        m "I put a corner of the pillow in my mouth, steeling myself for the pain."
    m "Teeth ghosted over my crotch and taint, as Anna dug her tongue deeper."
    play sound "fx/bite.wav"
    show white with dissolve
    m "Then she bit down, pulling back to rip my flesh away from my pelvis."
    if bangovore_four_anna4.blood_loss < 0.4:
        m "I screamed into the pillow until my breath ran out, the explosion of pain from the bundle of nerves more than I could prepare for."
    else:
        m "My head lolled back, mouth open in a silent scream as the pain, worse than any so far, blocked out the world for a moment."
    jump bangovore_four_anna4_chow_down_groin_merge
label bangovore_four_anna4_chow_down_groin_claws:
    if bangovore_four_anna4.blood_loss < 0.4:
        m "I put a corner of the pillow in my mouth, steeling myself for the pain."
    m "Bracing her arms against my legs to keep them spread, Anna lined up her claws on both hands."
    play sound "fx/gore.ogg"
    show white with dissolve
    m "Then she dug her claws in, cutting from my crotch toward my taint to eventually rip my genitals free."
    if bangovore_four_anna4.blood_loss < 0.4:
        m "I screamed into the pillow until my breath ran out, then took another and kept going as the sawing pain from the bundle of nerves lit my whole lower body afire."
    else:
        m "My head lolled back, mouth open in a silent scream as the pain, worse than any so far, blocked out the world for several seconds as she cut."
    jump bangovore_four_anna4_chow_down_groin_merge
label bangovore_four_anna4_chow_down_groin_merge:
    show anna smirk c behind grey
    hide white
    with dissolveslow
    jump todo_bangovore_four_anna4_out_of_content




label bangovore_four_anna4_kiss_of_death_clean:
    hide anna with dissolve
    $ renpy.pause (0.3)
    show anna bangok lipbite:
        # transform_anchor True
        anchor (0.5, 1.0)
        zoom 3.0 ypos 2600 xpos 0.8
    with dissolve
    $ renpy.pause (1.3)
    m "Anna leaned in, lips parting for a final kiss."
    show anna bangok blush with dissolve
    m "I let her tongue tangle with mine for a moment."
    show anna bangok blush:
        ease 1.5 zoom 3.0 ypos 2900
        zoom 3.0 ypos 2900
    with None
    $ renpy.pause (1.3)
    m "Then she slipped lower, running her scaly lips and tongue across my cheek, then down my neck."
    show anna bangok orgasm with dissolve
    m "She opened her jaws wide around my neck."
    play sound "fx/slice.ogg"
    play sound2 "fx/bite.wav"
    show anna rage c with None
    show white with dissolvemed
    $ renpy.pause (1.3)
    play sound2 "fx/impact3.ogg"
    $ renpy.pause (1.3)
    show black with dissolveslow
    jump bangovore_four_anna4_epilogue



label bangovore_four_anna4_epilogue:
    stop music fadeout 2.0

    scene black with dissolveslow

    $ renpy.pause (2.0)

    nvl clear

    window show

    play music "mx/schizophrenia.ogg"
    n "My murder at Anna's jaws went unresolved, as Anna came forward with news of the comet and the generators in the underground facility."
    n "The generators were retrieved and placed under heavy guard, rendering the portal inoperable while the dragons prepared their defense."
    n "Without the facility generators, nor any he had stolen thus far, Reza's escape attempt on the day of the fireworks failed. Eventually Maverick tracked him down and slaughtered him, earning a dismissal from the force."
    n "In the weeks that followed, the dragons prepared for the comet."
    n "When the time came, the dragons executed their plan, and by utilizing the underground building's generators, the comet was ultimately diverted and never hit Earth."
    n "After they recovered and power was restored to the portal, they discovered humanity's coordinates had been deleted or lost."

    window hide
    nvl clear
    window show

    n "Though I remained part of Anna until the end, the end did come."
    n "It didn't take a genius to connect her knowledge of the comet and the generators back to my gruesome demise."
    n "As soon as ceremonies around the comet diversion were complete, for my death and a host of other crimes, she was locked away, doomed to die on a medical gurney in a prison as she'd expected."

    window hide
    nvl clear

    show annasick at Pan((300, 169), (0, 0), 12.0) with fade
    $ renpy.pause (7.0)
    An "But at least I'm not alone."
    stop music fadeout 2.0
    scene black with dissolveslow
    $ annadead = True
    $ renpy.pause (2.0)

    $ renpy.pause (1.0)

    jump bangovore_four_anna4_bangok_epilogue_end



label todo_bangovore_four_anna4_out_of_content:
    play sound "fx/system3.wav"
    s "Out of content."
    $ renpy.error("Out of content.")