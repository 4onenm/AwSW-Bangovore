from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

def bangovore_four_anna4():
    ( ml.find_label('a4romance')
        .search_menu("If you say so.")
        .branch()
        .search_say("Not like that! You'll ruin them. I'll do it.")
        .hook_to('bangovore_four_anna4', return_link=True, condition='persistent.nsfwtoggle == True and annagoodending == False')
    )

    ( ml.find_label('bangok_anon_anna4_start')
        .search_if('bangok_four_anna2.unplayed == True')
        .link_from('bangovore_four_anna4_bangok_sex')
    )

    ( ml.find_label('annagoodending')
        .search_python('_game_menu_screen = None', depth=300)
        .link_from('bangovore_four_anna4_bangok_epilogue_end')
    )

    # Paginate Anna nom menus
    m1 = ( ml.find_label('bangovore_four_anna4_chow_down_menu1_pagination'))
    ml.ast_link.utils._create_hook(node_from=m1.node, func=ml.pages._show_charmenu, tag="bangovore_four_anna4_chow_down_menu1_paginator") 
    m2 = ( ml.find_label('bangovore_four_anna4_chow_down_menu2_pagination'))
    ml.ast_link.utils._create_hook(node_from=m2.node, func=ml.pages._show_charmenu, tag="bangovore_four_anna4_chow_down_menu2_paginator") 


def bangovore_four_xsebastian():
    ( ml.find_label('sebastianskip')
        .search_menu("It's pretty cold.")
        .branch()
        .search_menu("I'll take it.")
        .link_behind_from('bangovore_four_xsebastian_noromance')
        .branch()
        .search_say("Is that better?")
        .hook_to('bangovore_four_xsebastian_choice', return_link=False, condition='persistent.nsfwtoggle == True')
        .search_say("Sure.")
        .link_behind_from('bangovore_four_xsebastian_choice_end')
    )


def link_scenes():
    bangovore_four_anna4()
    bangovore_four_xsebastian()

@loadable_mod
class BangOVoreMod(Mod):
    name = "BangOVore"
    version = "v0.0"
    author = "4onen"
    nsfw = True
    dependencies = ["MagmaLink", "?BangOk"]

    @staticmethod
    def mod_load():
        link_scenes()

    @staticmethod
    def mod_complete():
        pass