init:
    image bangovore_four_xsebastian_belly normal = "bg/bangovore/sebbelly.png"
    image bangovore_four_xsebastian_belly hose = im.Composite(
        (1920,1080),
        (0,0), "bg/bangovore/sebbelly.png",
        (0,0), "bg/bangovore/sebbelly_hose.png",
    )
    image bangovore_four_xsebastian_belly hose direct = im.Composite(
        (1920,1080),
        (0,0), "bg/bangovore/sebbelly.png",
        (0,0), "bg/bangovore/sebbelly_hose_direct.png",
    )
    image bangovore_four_xsebastian_belly hose direct cum = im.Composite(
        (1920,1080),
        (0,0), "bg/bangovore/sebbelly.png",
        (0,0), "bg/bangovore/sebbelly_hose_direct.png",
        (0,0), "bg/bangovore/sebbelly_cumspray.png",
    )
    image bangovore_four_xsebastian_belly hose direct cum cumoverlay = im.Composite(
        (1920,1080),
        (0,0), "bg/bangovore/sebbelly.png",
        (0,0), "bg/bangovore/sebbelly_hose_direct.png",
        (0,0), "bg/bangovore/sebbelly_cumspray.png",
        (0,0), "bg/bangovore/sebbelly_cumoverlay.png",
    )

    python:
        bangovore_four_xsebastian_undiscussed = True
        bangovore_four_xsebastian_unplayed = True

label bangovore_four_xsebastian_choice:
    menu:
        "Sure.":
            $ renpy.pause (0.5)
            jump bangovore_four_xsebastian_choice_end
        "No, still a bit chilly.":
            $ renpy.pause (0.5)

    scene bangok_four_xsebastian_cave2_dk
    show sebastian normal b dk:
        xanchor 0.5
        yanchor 1.0
        zoom 1.7
        xpos 0.8
        ypos 1.4
        # rotate 35
    with dissolveslow

    Sb "Well, I think those layers you're wearing are helping you, otherwise I'd suggest taking them off to be closer to my body heat."
    $ renpy.pause (1.0)
    Sb drop b dk "There is {i}one{/i} more thing I could do for you."
    c "Oh?"
    Sb "I could keep you warm in my belly."
    c "{i}Eat{/i} me?!"
    Sb normal b dk "It's a technique taught in the police academy, for carrying someone and keeping your hands free if you have to, and have the time."
    Sb drop b dk "I was trained on... smaller dragons than you. But you also have fewer sharp bits sticking out of you."
    $ bangovore_four_xsebastian_undiscussed = False
    menu:
        "No. Please don't eat me.":
            c "I'll take shivering over being digested, thanks."
            Sb drop b dk "I mean, you wouldn't be..."
            Sb normal b dk "Nevermind. You were the one complaining about being cold."
            c "Alive is better than cold!"
            $ renpy.pause (1.0)
            c "I don't have to worry about you eating me once I go to sleep, right?"
            Sb normal b dk "If it did kill you, that wouldn't exactly be protecting you, would it?"
            c "..."
            Sb normal b dk "Just get some sleep. I promise I will not eat you."
            $ renpy.pause (0.5)
            c "Fine."
            jump bangovore_four_xsebastian_noromance
        "That's possible?":
            $ renpy.pause (0.5)
    Sb "I wouldn't be suggesting it if it wasn't."
    c "Wouldn't someone suffocate in your stomach? Or be digested?"
    Sb "For your first point, one of the pieces of equipment we can go out into the field with is an air hose, specifically for this. The strap of the headlight I'm carrying serves a double purpose as that."
    Sb shy b dk "Larger dragons can swallow some air to give their, ah, occupant some breathing room. Smaller dragons like me can't do that enough for it to be safe, hence the hose."
    Sb "For your second point, bile responses are only semi-autonomic. We can decide not to digest something, in which case it just sits there."
    Sb smile b dk "You were probably having too much fun to notice, but we haven't had anything for dinner."
    m "My stomach rumbled, validating his statement."
    Sb normal b dk "I should be relatively comfortable, compared to your shivering out here."
    menu:
        "I'm not curious enough to try it.":
            c "That's very much not something humans can do."
            Sb normal b dk "Up to you."
            c "Thanks for offering your body to keep me warm, though."
            Sb smile b dk "Just doing my job."
            jump bangovore_four_xsebastian_choice_end
        "I'm too curious.":
            pass
    c "How, exactly? Can you unhinge your jaw?"
    Sb smile b dk "Yes. That's... sort-of how it works."
    Sb normal b dk "I'll need you to remove your layers, though. I'm not sure I can choke down cloth, nor how well it'll last in there."
    menu:
        "Back out.":
            c "W-Wait, I'm not sure I can do that."
            Sb normal b dk "Why not?"
            c "Undressing in front of others implies a somewhat more intimate relationship for humans."
            Sb normal b dk "Up to you. You were the one complaining about being cold."
            c "Forget that, then. I'm good, thanks."
            jump bangovore_four_xsebastian_noromance
        "Undress.":
            $ renpy.pause (0.5)
            $ bangovore_four_xsebastian_unplayed = False
            $ bangok_four_xsebastian_unplayed = False
    play sound "fx/undress.ogg"
    $ renpy.pause (0.8)
    c "Thanks for this, Sebastian."
    show sebastian smile dk 
    m "Sebastian removed his hat, and undid the strap of a battery-powered headlamp beneath."
    Sb smile dk "Just doing my job."
    Sb shy dk "That said, I do think I should mention..."
    Sb normal dk "Some dragons do consider this a little intimate."
    Sb normal dk "I don't want to give you the wrong impression that this is normal."
    c "A human taking off their clothes for someone is intimate, too."
    Sb shy dk "O-Oh. I... wasn't aware."
    c "If that makes you uncomfortable, I could put them back on. If you don't want this to be intimate, I mean."
    $ renpy.pause (0.8)
    Sb smile dk "Well, I am one of those dragons who considers it intimate. Are you saying you feel the same way?"
    c "I'd love to be inside you, if you'd have me."
    show sebastian normal dk at Position(xpos=0.7) with ease
    m "Sebastian gently pushed me back against the bed of rocks. Then he began laying me out flat, arranging my arms and legs."
    Sb "Stay still, fold your legs once your hips are inside, hold your breath once your face is in my mouth, don't move your arms until you see the air hose."
    Sb "I can't give you instructions while I'm swallowing, so repeat that back to me, to make sure you've got it."
    show sebastian at Position(ypos=1.6) with ease
    show sebastian at Position(ypos=1.8) with ease
    hide sebastian with easeoutbottom
    m "I repeated his instructions back while he crawled down to my feet."
    Sb smile dk "Have fun."
    play soundloop "fx/bangovore/dragongulping.ogg" fadein 0.3
    m "He engulfed my feet in his wet maw in one swift motion, the walls of his throat stretching around my feet and forcing them tightly together."
    m "His teeth left pinpricks in my thighs as he hoisted up my lower body, gulping down more of my legs as he worked his way up."
    m "A primal part of my brain told me to panic and fight, but Seb's instructions repeated in my head, and I kept my cool as he wrapped his claws around my waist."
    if bangok_four_playerhasdick is None:
        m "His snout bumped into...{nw}"
        menu:
            m "His snout bumped into...{fast}"
            "My hard penis.":
                $ bangok_four_playerhasdick = True
            "My wet crotch.":
                $ bangok_four_playerhasdick = False
    if bangok_four_playerhasdick == True:
        m "His snout bumped into my hard penis, teeth ghosting over my sack as he hoisted my hips up."
        m "With a grunt, hot breath wafting around over my engulfed lower body, he pulled me further into his maw, teeth rubbing up the underside of my shaft as he pressed it to my belly."
    else:
        m "His snout bumped into my wet crotch, teeth pressing against my clit as he hoisted my hips up."
        m "With a grunt, hot breath wafting around over my engulfed lower body, he pulled me further into his maw, teeth rubbing up to my navel."

    show sebastian smile dk:
        xanchor 0.25
        yanchor 0.20
        zoom 4.0
        transform_anchor True
        xpos 0.5
        ypos 1.0
    with easeinbottom
    stop soundloop fadeout 0.5
    m "Sebastian caught my eye as he reached my upper chest, teeth tight over my arms folded on my chest. Then grasping my shoulders, he lifted me into the air, using gravity to force the rest of me down his maw."
    play sound "fx/bangovore/dragongulping.ogg"
    scene black with dissolveslow
    scene bangovore_four_xsebastian_belly normal:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        block:
            ease 4.0 zoom 1.5
            ease 4.0 zoom 1.0
            ease 4.0 zoom 1.5
            ease 4.0 zoom 1.0
            pause 2.0
            repeat
    with dissolveslow
    stop sound fadeout 0.5
    play soundloop "fx/bangovore/breathingslow.ogg" fadein 1.0
    m "I folded my legs, sliding whole into his tight, warm, stretched-out throat. Holding my breath, I squeezed down his tight gullet, until I settled with my legs in the massaging, hot, clammy innards of his belly."
    m "His breathing and internal muscles kneaded me from all sides, removing all the tension from my body as I sank into the warmth I'd asked for."
    show bangovore_four_xsebastian_belly hose with dissolve
    m "Just when my lungs began to remind me I needed to breathe, I felt the metal tip and cold plastic surface of the breathing hose bop me in the face."
    show bangovore_four_xsebastian_belly hose direct with dissolve
    m "I took the hose into my mouth, breathing out into Sebastian's fleshy walls to push for a little more space, then sucking down a breath of fresh air from the outside world."
    m "Then the world rocked, as Sebastian settled onto one side."
    $ renpy.pause (0.8)
    Sb smile dk "... There."
    m "His voice was lower, distorted by passing through his body's flesh to reach me."
    $ renpy.pause (0.5)
    m "A pressure rubbed against my back, his hand pressing against his belly."
    Sb smile b dk "Finally warm now?"
    m "I was suffused with heat, almost too hot as I discovered that his warm scales had been insulating, hiding his true body heat deep in his core."
    if bangok_four_playerhasdick == True:
        m "His shifting walls kneaded this heat into me, leaving my body flushed and aroused, dick rock hard between my legs."
    else:
        m "His shifting walls kneaded this heat into me, leaving my body flushed and aroused, slit slick and ready between my legs."
    menu:
        "Masturbate.":
            $ renpy.pause (0.5)
        "Try to sleep.":
            $ renpy.pause (0.5)
            m "Settling into the rhythm of Sebastian's breathing, I suckled on the cold air from outside, trying to get some rest."
            $ renpy.pause (0.5)
            m "Sebastian rubbed my back for a while longer, then yawned, shifting around me."
            $ renpy.pause (1.0)
            Sb "I'm going to get some sleep."
            $ renpy.pause (1.0)
            Sb "Goodnight."
            $ renpy.pause (1.0)
            jump bangovore_four_xsebastian_choice_end

    c "(He did say he was okay with this being intimate.)"
    if bangok_four_playerhasdick == True:
        stop soundloop fadeout 1.0
        m "I couldn't help myself. It took a little maneuvering to reach down and grasp my length with my hand slicked with Sebastian's stomach juices."
        play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
        m "Then I began pumping with my hand, masturbating in Sebastian's belly."
    else:
        stop soundloop fadeout 1.0
        m "I couldn't help myself. It took a little maneuvering to reach down and slip my hand between my legs."
        play soundloop "fx/bangok_poundofsalt.ogg" fadein 1.0
        m "Then I began pumping, fingerbanging myself in Sebastian's belly."

    Sb disapproval b dk "Huh? [player_name]? W-What are you up to in there?"
    $ renpy.pause (1.0)
    Sb shy b dk "Oh. Like this that much, hm?"
    Sb smile b dk "I guess you wouldn't mind, then, if I had some fun with myself up here?"

    scene bangovore_four_xsebastian_belly hose direct:
        xalign 0.5
        yalign 0.5
        zoom 1.8
    show black:
        alpha 0.0
        linear 0.5 alpha 0.5
        alpha 0.5
    with dissolve
    m "Sebastian bent over, compressing my tiny space even further."
    show bangovore_four_xsebastian_belly hose direct:
        zoom 1.8
        ease 0.3 zoom 2.0
        ease 0.35 zoom 1.8
        repeat
    with None
    m "Then he began to move in rhythmic motions, clenching then releasing as he curled around me again and again."
    $ renpy.pause (1.0)
    Sb shy b sleep dk "Mmnh. Yes. Keep moving..."
    $ renpy.pause (1.0)
    m "I was more than happy to oblige his request, thrusting a little with my hips as I brought myself over that tantalizing peak."

    $ renpy.pause (1.0)
    stop soundloop fadeout 0.5
    play sound "fx/extinguish.ogg"
    show black:
        alpha 1.0
    with dissolve
    c "Ah!"
    if bangok_four_playerhasdick == True:
        m "I came, my cum smearing between my body, legs, and Sebastian's stomach walls as I stuttered to a stop, but his squeezing undulations continued."
    else:
        m "I came, my juices squelching around my hand and dribbling onto the lining of Sebastian's stomach as it continued to squeeze around me."
    $ renpy.pause (1.0)
    hide black with dissolveslow
    Sb shy b sleep dk "C-Close..."

    show bangovore_four_xsebastian_belly hose direct:
        ease 0.3 zoom 2.0
        zoom 2.0
    with None
    play sound "fx/bangovore/muffledgrowl.ogg"
    m "Sebastian curled tighter than ever around me, shuddering from his own climax."
    $ renpy.pause (0.5)
    play sound2 "fx/extinguish.ogg"
    show bangovore_four_xsebastian_belly hose direct cum cumoverlay with dissolve
    m "Then wet, sticky packets of whiteness spurted from his esophagus, dribbling down over my face and head."
    $ renpy.pause (0.5)
    show bangovore_four_xsebastian_belly hose direct cum cumoverlay:
        zoom 2.0
        ease 2.0 zoom 1.0
        zoom 1.0
        block:
            ease 4.0 zoom 1.5
            ease 4.0 zoom 1.0
            ease 4.0 zoom 1.5
            ease 4.0 zoom 1.0
            pause 2.0
            repeat
    with None
    $ renpy.pause (2.0)
    play soundloop "fx/bangovore/breathingslow.ogg" fadein 1.0
    m "Sebastian relaxed, again rubbing my back through his stretched-out belly."
    stop soundloop fadeout 0.5
    m "Then his breathing hitched."
    Sb shy b dk "Oh no."
    Sb drop b dk "[player_name], are you okay? I-I didn't evem get your permission before I started sucking myself off."
    $ renpy.pause (0.5)
    Sb drop b dk "[player_name]?"
    m "I elbowed his side to let him know I was still here, inside him."
    Sb disapproval b dk "Do you want out? I don't want to keep you trapped in there if..."
    Sb drop b dk "Well, I understand if you're upset."
    Sb drop b dk "Do you need me to get you out of there? Or do you still want to sleep inside me?"

    # TODO: Maybe a cough-up options?
    m "I relaxed again into his warmth. At the moment, there was nowhere I'd rather be."

    Sb drop b dk "I'm not feeling..."
    Sb shy b dk "Oh, you'd rather stay?"
    Sb shy b dk "I'm not keeping you there without a positive affirmation. You want to stay in there?"
    m "I nudged his side again."
    Sb shy b dk "Oh."
    Sb smile b dk "A-Alright."
    play soundloop "fx/bangovore/breathingslow.ogg" fadein 2.0
    $ renpy.pause (4.0)
    Sb smile b dk "Goodnight, [player_name]."
    stop soundloop fadeout 10.0
    $ renpy.pause (4.0)

    $ mp.sebastianromance = True
    $ mp.save()
    jump bangovore_four_xsebastian_noromance

