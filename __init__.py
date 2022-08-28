from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml
from bangok_four import register_fetish

def bangovore_four_bryce3():
    ( ml.find_label('bangok_four_bryce3_mcbottom_train_epilogue')
        .search_say("I hope not. Came up with a couple ideas while packing the trash.")
        .hook_to('bangovore_four_bryce3_mcbottom_train_epilogue', return_link=True, condition='persistent.nsfwtoggle == True and persistent.bangovore_softvore == True')
    )


def bangovore_four_xsebastian():
    ( ml.find_label('sebastianskip')
        .search_menu("It's pretty cold.")
        .branch()
        .search_menu("I'll take it.")
        .link_behind_from('bangovore_four_xsebastian_noromance')
        .branch()
        .search_say("Is that better?")
        .hook_to('bangovore_four_xsebastian_choice', return_link=False, condition='persistent.nsfwtoggle == True and persistent.bangovore_softvore == True')
        .search_say("Sure.")
        .link_behind_from('bangovore_four_xsebastian_choice_end')
    )


def link_scenes():
    bangovore_four_bryce3()
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
        register_fetish("Soft Vore", 'bangovore_softvore',
            active_image="image/ui/bangovore/icons/bangovore_softvore_active.png",
            inactive_image="image/ui/bangovore/icons/bangovore_softvore_inactive.png",
        )

        link_scenes()

    @staticmethod
    def mod_complete():
        pass
