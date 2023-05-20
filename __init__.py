from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

@loadable_mod
class AWSWMod(Mod):
    name = "Seb Mod"
    version = "1.0"
    author = "Venus"
    dependencies = ["MagmaLink"]

    def mod_load(self):
        ml.find_label("gamestart") \
            .search_python("d2unplayed = True") \
            .hook_to("venus_BB") \
            .search_say("Alright, that's it.", 3900) \
            .link_from("venus_BB_end")
            

    def mod_complete(self):
        pass
