# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define red = Character("Little Red")
define mother = Character("Mother")
define wolf = Character("Mr. Wolf")
define fake = Character("Grandma?")
define grandma = Character("Grandma")

# The game starts here.

label start:
    #################
    ##### ACT 1 #####
    #################

    play music "audio/scene1.ogg"
    scene cottage

    voice "the-sun-shines-gently-over-a-s-british-male-2025-04-01.ogg"
    "The sun shines gently over a small cottage at the edge of the forest."

    play sound "audio/chirp.ogg"

    voice "birds-chirp-in-the-distance-a-british-male-2025-04-01.ogg"
    "Birds chirp in the distance, and the air is filled with the warm scent of freshly baked bread."

    scene cottage inside

    voice "inside-the-cottage-a-young-gi-british-male-2025-04-01.ogg"
    "Inside the cottage, a young girl in a red hood stands before her mother, a wicker basket in her hands."

    show mother_normal
    with dissolve

    voice "little-red-my-dear-your-g-american-female-2025-04-01.ogg"
    mother "Little Red, my dear, your grandmother isn't feeling well. This basket has fresh bread, honey, and warm tea for her."

    hide mother_normal
    show red_smile
    with dissolve

    voice "i-ll-take-it-to-her-right-away-energetic-girl-2025-04-01.ogg"
    red "I'll take it to her right away, Mother"

    show red_smile at left
    show mother_normal at right
    with dissolve

    voice "good-girl-but-listen-carefull-american-female-2025-04-01.ogg"
    mother "Good girl. But listen carefully, stay on the path, and don't talk to strangers. The woods can be dangerous"

    hide red_smile
    show red_normal at left
    with dissolve
    voice "i-know-i-know-you-ve-told-me-energetic-girl-2025-04-01.ogg"
    red "I know, I know! You've told me a hundred times"

    hide mother_normal
    show mother_concern at right
    with dissolve
    voice "and-i-ll-tell-you-a-hundred-mo-american-female-2025-04-01.ogg"
    mother "And I'll tell you a hundred more. Promise me, dear"

    menu:
        "Of course, Mother. I'll be careful.":
            hide red_normal
            show red_smile at left
            with dissolve
            voice "of-course-mother-i-ll-be-car-energetic-girl-2025-04-01.ogg"
            red "Of course, Mother. I'll be careful."
            jump choice1_option1
        
        "I can handle myself. I'll be fine.":
            hide red_normal
            show red_smile at left
            with dissolve
            voice "i-can-handle-myself-i-ll-be-f-energetic-girl-2025-04-01.ogg"
            red "I can handle myself. I'll be fine."
            jump choice1_option2
        
    label choice1_option1:

        $ menu_flag = True

        hide mother_concern
        show mother_normal at right
        with dissolve
        voice "that-s-my-good-girl-now-off-y-american-female-2025-04-01.ogg"
        mother "That's my good girl. Now off you go, and be safe"

        jump choice1_done

    label choice1_option2:

        $ menu_flag = True

        hide mother_concern
        show mother_normal at right
        with dissolve
        voice "even-the-bravest-must-be-caref-american-female-2025-04-01.ogg"
        mother "Even the bravest must be careful, my dear. Promise me."


        voice "alright-alright-i-promise-energetic-girl-2025-04-01.ogg"
        red "Alright, alright, I promise."

        jump choice1_done

    label choice1_done:

    scene cottage
    with fade
    
    play audio "audio/door-close.ogg"
    voice "with-her-basket-in-hand-littl-british-male-2025-04-01.ogg"
    "With her basket in hand, Little Red walks outside the cottage and steps onto the worn dirt path."

    scene path
    with fade

    play audio "audio/wind.ogg"
    voice "the-morning-air-is-crisp-carr-british-male-2025-04-01.ogg"
    "The morning air is crisp, carrying the scent of wildflowers and damp earth. Birds chatter in the trees, and the leaves rustle with the whispers of the wind."

    voice "as-she-walks-her-hood-swaying-british-male-2025-04-01.ogg"
    "As she walks, her hood swaying with each step. The world feels peaceful.. for now."

    #################
    ##### ACT 2 #####
    #################

    scene dark wood
    with fade

    play music "audio/scene2.ogg"

    voice "the-deeper-little-red-ventures-british-male-2025-04-01.ogg"
    "The deeper Little Red ventures into the woods, the quieter the world becomes."

    play audio "audio/leaf.ogg"
    voice "the-cheerful-songs-of-birds-fa-british-male-2025-04-01.ogg"
    "The cheerful songs of birds fade into distant echoes, replaced by the creaking of tree limbs and the soft crunch of leaves beneath her feet."

    voice "then-from-the-shadows-a-voic-british-male-2025-04-01.ogg"
    "Then, from the shadows, a voice as smooth as honey drifts through the air."

    scene dark wood2
    with dissolve

    show wolf_normal
    with dissolve
    voice "well-well-what-do-we-have-american-male-2025-04-01.ogg"
    wolf "Well, well... What do we have here? A little girl, all alone in the woods?"

    hide wolf_normal
    show red_confused
    with dissolve
    voice "oh-hello-sir-i-m-just-on-my-energetic-girl-2025-04-01.ogg"
    red "Oh! Hello, sir. I'm just on my way to Grandma's house"

    hide red_confused
    show wolf_smile
    with dissolve
    voice "ah-how-sweet-and-what-s-in-t-american-male-2025-04-01.ogg"
    wolf "Ah, how sweet! And what's in the basket, little one? A gift for dear old Grandma?"

    hide wolf_smile
    show red_smile
    with dissolve
    voice "yes-bread-honey-and-tea-sh-energetic-girl-2025-04-01.ogg"
    red "Yes! Bread, honey, and tea. She's not feeling well, so I'm bringing her something warm."

    hide red_smile
    show wolf_smile
    with dissolve
    voice "such-a-thoughtful-girl-you-kn-american-male-2025-04-01.ogg"
    wolf "Such a thoughtful girl! You know, there's a lovely patch of flowers just ahead. A fresh bouquet would surely make your grandmother feel even better."

    hide wolf_smile
    show red_confused
    with dissolve
    voice "that-does-sound-nice-energetic-girl-2025-04-01.ogg"
    red "That does sound nice..."

    menu:
        "I'm just going straight to Grandma's.":
            hide red_confused
            show red_normal
            with dissolve
            voice "i-m-just-going-straight-to-gra-energetic-girl-2025-04-01.ogg"
            red "I'm just going straight to Grandma's."
            jump choice2_option1
        
        "I suppose one little detour won't hurt.":
            hide red_confused
            show red_normal
            with dissolve
            voice "i-suppose-one-little-detour-wo-energetic-girl-2025-04-01.ogg"
            red "I suppose one little detour won't hurt."
            jump choice2_option2
        
    label choice2_option1:

        $ menu_flag = True

        hide red_normal
        show wolf_normal
        with dissolve
        voice "oh-my-how-responsible-but-do-american-male-2025-04-01.ogg"
        wolf "Oh my, how responsible! But don't you think a few flowers would make her even happier?"
        hide wolf_normal
        with dissolve

        jump choice2_done

    label choice2_option2:

        $ menu_flag = True

        hide red_normal
        show wolf_smile
        with dissolve
        voice "that-s-the-spirit-little-one-american-male-2025-04-01.ogg"
        wolf "That's the spirit, little one! Just follow that path there, you'll find the most beautiful flowers you've ever seen."
        hide wolf_smile
        with dissolve

        jump choice2_done

    label choice2_done:
    
    voice "little-red-although-hesistant-british-male-2025-04-01.ogg"
    "Little Red, although hesistant, considers the wolf's words. The forest seems peaceful, but unseen eyes are watching, waiting."

    #################
    ##### ACT 3 #####
    #################

    scene grandma house
    with fade

    play music "audio/scene3.ogg"
    
    voice "the-forest-thins-as-little-red-british-male-2025-04-01.ogg"
    "The forest thins as Little Red approaches the familiar cottage. The wooden house stands quiet, its shutters slightly ajar. A soft breeze rustles the trees, and for the first time, Little Red hesitates."

    voice "something-feels-off-british-male-2025-04-01.ogg"
    "Something feels... off."

    play audio "audio/knock.ogg"
    voice "still-she-shakes-the-feeling-british-male-2025-04-01.ogg"
    "Still, she shakes the feeling away and knocks lightly on the door."

    show red_normal
    with dissolve
    voice "grandma-it-s-me-little-red-energetic-girl-2025-04-01.ogg"
    red "Grandma? It's me, Little Red! I've brought you some treats!"

    hide red_normal
    with dissolve

    voice "come-in-my-dear-i-m-in-bed-british-female-2025-04-01.ogg"
    fake "Come in, my dear... I'm in bed. I feel so very weak today."

    voice "little-red-pushes-the-door-ope-british-male-2025-04-01.ogg"
    "Little Red pushes the door open."

    play audio "audio/door-close.ogg"
    
    scene grandma house inside
    with fade

    voice "the-room-is-dim-the-curtains-british-male-2025-04-01.ogg"
    "The room is dim, the curtains drawn."

    voice "grandma-lies-in-bed-her-face-british-male-2025-04-01.ogg"
    "Grandma lies in bed, her face half-hidden by the blankets. Her breathing is slow and heavy."

    show red_confused
    with dissolve
    voice "grandma-are-you-alright-you-energetic-girl-2025-04-01.ogg"
    red "Grandma, are you alright? You look... different today."

    hide red_confused
    show grandma_evil
    with dissolve
    voice "oh-child-it-s-just-this-awfu-british-female-2025-04-01.ogg"
    fake "Oh, child, it's just this awful illness. Come closer, let me see you properly."

    hide grandma_evil
    show red_confused
    with dissolve
    voice "grandma-what-big-eyes-you-h-energetic-girl-2025-04-01.ogg"
    red "Grandma... what big eyes you have."

    hide red_confused
    show grandma_evil
    with dissolve
    voice "all-the-better-to-see-you-with-british-female-2025-04-01.ogg"
    fake "All the better to see you with, my dear."

    hide grandma_evil
    show red_confused
    with dissolve
    voice "and-what-big-ears-you-have-energetic-girl-2025-04-01.ogg"
    red "And what big ears you have."

    hide red_confused
    show grandma_evil
    with dissolve
    voice "all-the-better-to-hear-you-wit-british-female-2025-04-01.ogg"
    fake "All the better to hear you with, my dear."

    hide grandma_evil
    show red_confused
    with dissolve
    voice "and-what-big-teeth-you-have-energetic-girl-2025-04-01.ogg"
    red "And what big teeth you have..."

    hide red_confused
    show wolf_smile
    with dissolve
    voice "all-the-better-to-eat-you-with-american-male-2025-04-01.ogg"
    wolf "All the better to eat you with!"

    play audio "audio/lunge.ogg"
    voice "the-wolf-lunges-forward-british-male-2025-04-01.ogg"
    "The Wolf lunges forward."

    hide wolf_smile
    with dissolve

    menu:
        "I... I don't understand. What's happening?":
            show red_scared
            with dissolve
            voice "i-i-don-t-understand-what-energetic-girl-2025-04-01.ogg"
            red "I... I don't understand. What's happening?"
            hide red_scared
            jump choice3_option1
        
        "I'm not afraid of you!":
            show red_normal
            with dissolve
            voice "i-m-not-afraid-of-you-energetic-girl-2025-04-01.ogg"
            red "I'm not afraid of you!"
            jump choice3_option2
        
    label choice3_option1:

        $ menu_flag = True

        play music "audio/bad.ogg"

        show wolf_smile
        with dissolve
        voice "oh-my-sweet-child-didnt-anyo-american-male-2025-04-01.ogg"
        wolf "Oh, my sweet child… didnt anyone tell you? The forest is full of dangers."

        hide wolf_smile
        show red_scared
        with dissolve
        voice "no-this-isn-t-right-you-energetic-girl-2025-04-01.ogg"
        red "No... this isn't right... You're not Grandma..."

        voice "her-breath-quickens-as-the-wol-british-male-2025-04-01.ogg"
        "Her breath quickens as the Wolf lunges. She stumbles, her back hitting the wooden wall."
        
        hide red_scared
        show red_cry
        with dissolve
        voice "i-should-have-been-more-carefu-energetic-girl-2025-04-01.ogg"
        red "I should have been more careful..."

        hide red_cry
        show wolf_smile
        with dissolve
        voice "a-sharp-toothed-grin-is-the-la-british-male-2025-04-01.ogg"
        "A sharp-toothed grin is the last thing she sees before the room fades into darkness."
        
        play audio "audio/scream.ogg"

        scene black
        with fade
        centered "BAD END"

        jump choice3_done

    label choice3_option2:

        $ menu_flag = True

        voice "little-red-s-heart-pounds-but-british-male-2025-04-01.ogg"
        "Little Red's heart pounds, but she refuses to freeze."

        scene knife

        voice "her-eyes-dart-around-the-room-british-male-2025-04-01.ogg"
        "Her eyes dart around the room—there, on the wooden table, a sharp kitchen knife rests within reach."

        voice "as-the-wolf-lunges-she-grabs-british-male-2025-04-01.ogg"
        "As the Wolf lunges, she grabs it and swings with all her strength."

        play audio "audio/slash.ogg"
        scene grandma house inside

        show wolf_normal
        with dissolve
        voice "the-impact-lands-squarely-on-h-british-male-2025-04-01.ogg"
        "The impact lands squarely on his snout, sending him reeling back with a pained yelp."

        voice "the-wolf-shaken-and-snarling-british-male-2025-04-01.ogg"
        "The Wolf, shaken and snarling, knows he has lost the advantage."

        hide wolf_normal
        with dissolve
        voice "with-a-final-glare-he-retreat-british-male-2025-04-01.ogg"
        "With a final glare, he retreats, slipping into the shadows of the forest."

        voice "panting-little-red-grips-the-british-male-2025-04-01.ogg"
        "Panting, Little Red grips the doorframe, watching as the Wolf vanishes into the trees. Silence falls over the house, broken only by the sound of a weak voice."

        play music "audio/good.ogg"

        voice "little-red-british-female-2025-04-01.ogg"
        grandma "Little Red...?"

        play audio "audio/wardrobe.ogg"
        voice "turning-back-she-rushes-to-th-british-male-2025-04-01.ogg"
        "Turning back, she rushes to the wardrobe, flinging it open. Inside, trembling but alive, is her grandmother."

        show grandma_normal
        with dissolve
        voice "oh-my-dear-girl-you-re-safe-british-female-2025-04-01.ogg"
        grandma "Oh, my dear girl, you're safe!"

        hide grandma_normal
        show red_cry
        with dissolve
        voice "i-thought-i-thought-i-lost-yo-energetic-girl-2025-04-01.ogg"
        red "I thought… I thought I lost you."

        hide red_cry
        show grandma_normal
        with dissolve
        voice "you-were-so-brave-my-dear-british-female-2025-04-01.ogg"
        grandma "You were so brave, my dear."

        hide grandma_normal
        show red_cry
        with dissolve
        voice "mother-always-warned-me-about-energetic-girl-2025-04-01.ogg"
        red "Mother always warned me about the dangers of the forest… I should have listened more carefully."

        hide red_cry
        show red_smile
        with dissolve
        voice "i-ll-be-more-careful-next-time-energetic-girl-2025-04-01.ogg"
        red "I'll be more careful next time."

        scene black
        with fade
        centered "GOOD END"

        jump choice3_done

    label choice3_done:
    return
 