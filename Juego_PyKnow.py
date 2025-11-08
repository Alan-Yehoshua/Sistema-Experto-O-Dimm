
from pyknow import *

class Juego(Fact):
    pass

class GameExpert(KnowledgeEngine):
    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="n", Multijugador="n", Genre_Casual="n"))
    def regla_0(self):
        self.declare(Fact(resultado="Baba Is You"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="n", Multijugador="n", Genre_Casual="s"))
    def regla_1(self):
        self.declare(Fact(resultado="Trombone Champ"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="n", Multijugador="s"))
    def regla_2(self):
        self.declare(Fact(resultado="Keep Talking and Nobody Explodes"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="s", Genre_Indie="n", Genre_Casual="n"))
    def regla_3(self):
        self.declare(Fact(resultado="FlatOut 2"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="s", Genre_Indie="n", Genre_Casual="s"))
    def regla_4(self):
        self.declare(Fact(resultado="Among Us"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="s", Genre_Indie="s", Genre_Casual="n"))
    def regla_5(self):
        self.declare(Fact(resultado="Beat Saber"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="n", Is_PVP="s", Genre_Indie="s", Genre_Casual="s"))
    def regla_6(self):
        self.declare(Fact(resultado="Tricky Towers"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="s", Genre_Indie="n", Gano_GOTY="n", Mixed="n"))
    def regla_7(self):
        self.declare(Fact(resultado="ATOM RPG: Post-apocalyptic indie game"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="s", Genre_Indie="n", Gano_GOTY="n", Mixed="s"))
    def regla_8(self):
        self.declare(Fact(resultado="FINAL FANTASY XIV Online"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="s", Genre_Indie="n", Gano_GOTY="s"))
    def regla_9(self):
        self.declare(Fact(resultado="The Witcher 3: Wild Hunt"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="n", Genre_Rol="s", Genre_Indie="s"))
    def regla_10(self):
        self.declare(Fact(resultado="Ruined King: A League of Legends Storyâ¢"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="n", Genre_Indie="n"))
    def regla_11(self):
        self.declare(Fact(resultado="Age of Empires II (Retired)"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="n", Genre_Indie="s", Genre_Rol="n", Genre_Casual="n"))
    def regla_12(self):
        self.declare(Fact(resultado="Dicey Dungeons"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="n", Genre_Indie="s", Genre_Rol="n", Genre_Casual="s"))
    def regla_13(self):
        self.declare(Fact(resultado="ISLANDERS"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="n", Genre_Indie="s", Genre_Rol="s", Un_jugador="n"))
    def regla_14(self):
        self.declare(Fact(resultado="Wildermyth"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="n", Genre_Indie="s", Genre_Rol="s", Un_jugador="s"))
    def regla_15(self):
        self.declare(Fact(resultado="Darkest DungeonÂ®"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="s", Mixed="n", Is_free="n", Genre_Rol="n"))
    def regla_16(self):
        self.declare(Fact(resultado="Age of Empires: Definitive Edition"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="s", Mixed="n", Is_free="n", Genre_Rol="s"))
    def regla_17(self):
        self.declare(Fact(resultado="ENDLESSâ¢ Legend"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="s", Mixed="n", Is_free="s"))
    def regla_18(self):
        self.declare(Fact(resultado="Age of Empires III: Definitive Edition"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="n", Genre_Estrategia="s", Is_PVP="s", Mixed="s"))
    def regla_19(self):
        self.declare(Fact(resultado="Age of Empires II: Definitive Edition"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="n", Genre_Deportes="n", Mixed="n", Genre_Casual="n"))
    def regla_20(self):
        self.declare(Fact(resultado="Hardspace: Shipbreaker"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="n", Genre_Deportes="n", Mixed="n", Genre_Casual="s"))
    def regla_21(self):
        self.declare(Fact(resultado="Cooking Simulator"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="n", Genre_Deportes="n", Mixed="s"))
    def regla_22(self):
        self.declare(Fact(resultado="Farming Simulator 15"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="n", Genre_Deportes="s", Genre_Carreras="n"))
    def regla_23(self):
        self.declare(Fact(resultado="Football Manager 2020"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="n", Genre_Deportes="s", Genre_Carreras="s"))
    def regla_24(self):
        self.declare(Fact(resultado="Assetto Corsa Competizione"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="s", Genre_Casual="n", Genre_Rol="n", Un_jugador="n"))
    def regla_25(self):
        self.declare(Fact(resultado="American Truck Simulator"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="s", Genre_Casual="n", Genre_Rol="n", Un_jugador="s"))
    def regla_26(self):
        self.declare(Fact(resultado="Assetto Corsa"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="s", Genre_Casual="n", Genre_Rol="s"))
    def regla_27(self):
        self.declare(Fact(resultado="Cultist Simulator"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="s", Genre_Casual="s", Un_jugador="n"))
    def regla_28(self):
        self.declare(Fact(resultado="House Flipper 2"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="n", Genre_Indie="s", Genre_Casual="s", Un_jugador="s"))
    def regla_29(self):
        self.declare(Fact(resultado="Gas Station Simulator"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="n", Un_jugador="n", Genre_Rol="n"))
    def regla_30(self):
        self.declare(Fact(resultado="Age of Mythology: Extended Edition"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="n", Un_jugador="n", Genre_Rol="s"))
    def regla_31(self):
        self.declare(Fact(resultado="Tropico 5"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="n", Un_jugador="s", Genre_Rol="n"))
    def regla_32(self):
        self.declare(Fact(resultado="Against the Storm"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="n", Un_jugador="s", Genre_Rol="s"))
    def regla_33(self):
        self.declare(Fact(resultado="Battle Brothers"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="s", Un_jugador="n"))
    def regla_34(self):
        self.declare(Fact(resultado="Anno 1800"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="s", Un_jugador="s", Genre_Rol="n"))
    def regla_35(self):
        self.declare(Fact(resultado="Imperator: Rome"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="n", Is_PVP="s", Un_jugador="s", Genre_Rol="s"))
    def regla_36(self):
        self.declare(Fact(resultado="Crusader Kings III"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="s", Un_jugador="n", Is_PVP="n"))
    def regla_37(self):
        self.declare(Fact(resultado="Factorio"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="s", Un_jugador="n", Is_PVP="s"))
    def regla_38(self):
        self.declare(Fact(resultado="The Escapists 2"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="s", Un_jugador="s", Genre_Casual="n"))
    def regla_39(self):
        self.declare(Fact(resultado="Banished"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="n", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Indie="s", Un_jugador="s", Genre_Casual="s"))
    def regla_40(self):
        self.declare(Fact(resultado="Game Dev Tycoon"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="n", Genre_Indie="n", Is_free="n"))
    def regla_41(self):
        self.declare(Fact(resultado="Counter-Strike: Source"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="n", Genre_Indie="n", Is_free="s"))
    def regla_42(self):
        self.declare(Fact(resultado="Dota 2"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="n", Genre_Indie="s", Genre_Estrategia="n"))
    def regla_43(self):
        self.declare(Fact(resultado="Chivalry: Medieval Warfare"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="n", Genre_Indie="s", Genre_Estrategia="s"))
    def regla_44(self):
        self.declare(Fact(resultado="Insurgency"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="s", Genre_Estrategia="n", Genre_Indie="n"))
    def regla_45(self):
        self.declare(Fact(resultado="Aliens vs. Predatorâ¢"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="s", Genre_Estrategia="n", Genre_Indie="s"))
    def regla_46(self):
        self.declare(Fact(resultado="Cuphead"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="s", Genre_Estrategia="s", Genre_Indie="n"))
    def regla_47(self):
        self.declare(Fact(resultado="Jagged Alliance 3"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Mixed="s", Genre_Estrategia="s", Genre_Indie="s"))
    def regla_48(self):
        self.declare(Fact(resultado="Door Kickers 2: Task Force North"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Indie="n", Genre_Simuladores="n"))
    def regla_49(self):
        self.declare(Fact(resultado="Borderlands 2"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Indie="n", Genre_Simuladores="s"))
    def regla_50(self):
        self.declare(Fact(resultado="State of Decay 2: Juggernaut Edition"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Indie="s"))
    def regla_51(self):
        self.declare(Fact(resultado="Crypt of the NecroDancer"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="n", Multijugador="n", Genre_Rol="n"))
    def regla_52(self):
        self.declare(Fact(resultado="Back 4 Blood"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="n", Multijugador="n", Genre_Rol="s"))
    def regla_53(self):
        self.declare(Fact(resultado="Dying Light"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="n", Multijugador="s", Genre_Multijugador_masivo="n"))
    def regla_54(self):
        self.declare(Fact(resultado="Counter-Strike"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="n", Multijugador="s", Genre_Multijugador_masivo="s"))
    def regla_55(self):
        self.declare(Fact(resultado="Red Orchestra 2: Heroes of Stalingrad with Rising Storm"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="s", Genre_Simuladores="n"))
    def regla_56(self):
        self.declare(Fact(resultado="Total War: THREE KINGDOMS"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="s", Genre_Simuladores="s", Genre_Multijugador_masivo="n"))
    def regla_57(self):
        self.declare(Fact(resultado="Arma 2: Operation Arrowhead"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="n", Genre_Estrategia="s", Genre_Simuladores="s", Genre_Multijugador_masivo="s"))
    def regla_58(self):
        self.declare(Fact(resultado="Rising Storm 2: Vietnam"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="n", Genre_Casual="n", Genre_Deportes="n"))
    def regla_59(self):
        self.declare(Fact(resultado="Clone Drone in the Danger Zone"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="n", Genre_Casual="n", Genre_Deportes="s"))
    def regla_60(self):
        self.declare(Fact(resultado="Rocket LeagueÂ®"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="n", Genre_Casual="s", Genre_Deportes="n"))
    def regla_61(self):
        self.declare(Fact(resultado="Overcooked! 2"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="n", Genre_Casual="s", Genre_Deportes="s"))
    def regla_62(self):
        self.declare(Fact(resultado="Fall Guys"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="s", Genre_Simuladores="n", Multijugador="n"))
    def regla_63(self):
        self.declare(Fact(resultado="Awesomenauts"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="s", Genre_Simuladores="n", Multijugador="s"))
    def regla_64(self):
        self.declare(Fact(resultado="Day of Infamy"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="s", Genre_Simuladores="s", Mixed="n"))
    def regla_65(self):
        self.declare(Fact(resultado="Hell Let Loose"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="n", Is_PVP="s", Genre_Indie="s", Genre_Estrategia="s", Genre_Simuladores="s", Mixed="s"))
    def regla_66(self):
        self.declare(Fact(resultado="Barotrauma"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="n", Genre_Rol="n", Genre_Estrategia="n", Genre_Carreras="n"))
    def regla_67(self):
        self.declare(Fact(resultado="Alien: Isolation"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="n", Genre_Rol="n", Genre_Estrategia="n", Genre_Carreras="s"))
    def regla_68(self):
        self.declare(Fact(resultado="Need for Speedâ¢ Hot Pursuit Remastered"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="n", Genre_Rol="n", Genre_Estrategia="s"))
    def regla_69(self):
        self.declare(Fact(resultado="Aliens: Dark Descent"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="n", Genre_Rol="s"))
    def regla_70(self):
        self.declare(Fact(resultado="BioShockâ¢"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="s", Genre_Estrategia="n", Genre_Rol="n", Genre_Deportes="n"))
    def regla_71(self):
        self.declare(Fact(resultado="ACE COMBATâ¢ 7: SKIES UNKNOWN"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="s", Genre_Estrategia="n", Genre_Rol="n", Genre_Deportes="s"))
    def regla_72(self):
        self.declare(Fact(resultado="Steepâ¢"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="s", Genre_Estrategia="n", Genre_Rol="s"))
    def regla_73(self):
        self.declare(Fact(resultado="S.T.A.L.K.E.R.: Call of Pripyat"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="s", Genre_Estrategia="s", Genre_Simuladores="n", Genre_Casual="n"))
    def regla_74(self):
        self.declare(Fact(resultado="Worms W.M.D"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="s", Genre_Estrategia="s", Genre_Simuladores="n", Genre_Casual="s"))
    def regla_75(self):
        self.declare(Fact(resultado="Plants vs. Zombiesâ¢ La Batalla de Neighborville"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="n", Is_PVP="s", Genre_Estrategia="s", Genre_Simuladores="s"))
    def regla_76(self):
        self.declare(Fact(resultado="Warhammer 40,000: Dawn of War III"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="n", Genre_Rol="n", Is_PVP="n", Genre_Estrategia="n"))
    def regla_77(self):
        self.declare(Fact(resultado="EVERSPACEâ¢"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="n", Genre_Rol="n", Is_PVP="n", Genre_Estrategia="s"))
    def regla_78(self):
        self.declare(Fact(resultado="Five Nights at Freddy's 4"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="n", Genre_Rol="n", Is_PVP="s", Genre_Deportes="n"))
    def regla_79(self):
        self.declare(Fact(resultado="Depth"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="n", Genre_Rol="n", Is_PVP="s", Genre_Deportes="s"))
    def regla_80(self):
        self.declare(Fact(resultado="SpeedRunners"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="n", Genre_Rol="s"))
    def regla_81(self):
        self.declare(Fact(resultado="Bastion"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="s", Genre_Estrategia="n", Is_PVP="n"))
    def regla_82(self):
        self.declare(Fact(resultado="Five Nights at Freddy's: Sister Location"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="s", Genre_Estrategia="n", Is_PVP="s"))
    def regla_83(self):
        self.declare(Fact(resultado="Wreckfest"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Rol="n", Is_PVP="n"))
    def regla_84(self):
        self.declare(Fact(resultado="Teardown"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Rol="n", Is_PVP="s"))
    def regla_85(self):
        self.declare(Fact(resultado="Isonzo"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Rol="s", Is_PVP="n"))
    def regla_86(self):
        self.declare(Fact(resultado="Kenshi"))

    @Rule(Juego(Genre_Aventura="n", Genre_Accion="s", Un_jugador="s", Genre_Indie="s", Genre_Simuladores="s", Genre_Estrategia="s", Genre_Rol="s", Is_PVP="s"))
    def regla_87(self):
        self.declare(Fact(resultado="Mount & Blade II: Bannerlord"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Gano_GOTY="n"))
    def regla_88(self):
        self.declare(Fact(resultado="Beyond: Two Souls"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="n", Gano_GOTY="s"))
    def regla_89(self):
        self.declare(Fact(resultado="It Takes Two"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Estrategia="n", Genre_Accion="n"))
    def regla_90(self):
        self.declare(Fact(resultado="Baldur's Gate: Enhanced Edition"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Estrategia="n", Genre_Accion="s"))
    def regla_91(self):
        self.declare(Fact(resultado="Borderlands 4"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Estrategia="s", Gano_GOTY="n", Genre_Multijugador_masivo="n"))
    def regla_92(self):
        self.declare(Fact(resultado="Gloomhaven"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Estrategia="s", Gano_GOTY="n", Genre_Multijugador_masivo="s"))
    def regla_93(self):
        self.declare(Fact(resultado="Elite Dangerous"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Estrategia="s", Gano_GOTY="s", Genre_Accion="n"))
    def regla_94(self):
        self.declare(Fact(resultado="Baldur's Gate 3"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="n", Genre_Rol="s", Genre_Estrategia="s", Gano_GOTY="s", Genre_Accion="s"))
    def regla_95(self):
        self.declare(Fact(resultado="Dragon Ageâ¢ Inquisition"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="n", Genre_Casual="n", Genre_Multijugador_masivo="n", Genre_Carreras="n"))
    def regla_96(self):
        self.declare(Fact(resultado="Gears 5"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="n", Genre_Casual="n", Genre_Multijugador_masivo="n", Genre_Carreras="s"))
    def regla_97(self):
        self.declare(Fact(resultado="Need for Speedâ¢ Payback"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="n", Genre_Casual="n", Genre_Multijugador_masivo="s"))
    def regla_98(self):
        self.declare(Fact(resultado="Z1 Battle Royale"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="n", Genre_Casual="s", Genre_Multijugador_masivo="n"))
    def regla_99(self):
        self.declare(Fact(resultado="Sonic Mania"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="n", Genre_Casual="s", Genre_Multijugador_masivo="s"))
    def regla_100(self):
        self.declare(Fact(resultado="DRAGON BALL XENOVERSE 2"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="s", Genre_Multijugador_masivo="n", Genre_Accion="n"))
    def regla_101(self):
        self.declare(Fact(resultado="Monster Hunter Stories 2: Wings of Ruin"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="s", Genre_Multijugador_masivo="n", Genre_Accion="s"))
    def regla_102(self):
        self.declare(Fact(resultado="Lords of the Fallen"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="s", Genre_Multijugador_masivo="s", Genre_Estrategia="n"))
    def regla_103(self):
        self.declare(Fact(resultado="The Elder ScrollsÂ® Online"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="n", Is_PVP="s", Genre_Rol="s", Genre_Multijugador_masivo="s", Genre_Estrategia="s"))
    def regla_104(self):
        self.declare(Fact(resultado="Black Desert"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="n", Genre_Estrategia="n"))
    def regla_105(self):
        self.declare(Fact(resultado="Assassinâs CreedÂ® III"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="n", Genre_Estrategia="s"))
    def regla_106(self):
        self.declare(Fact(resultado="L.A. Noire"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="n", Genre_Casual="n", Genre_Simuladores="n"))
    def regla_107(self):
        self.declare(Fact(resultado="A Plague Tale: Innocence"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="n", Genre_Casual="n", Genre_Simuladores="s"))
    def regla_108(self):
        self.declare(Fact(resultado="Contraband Police"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="n", Genre_Casual="s", Genre_Estrategia="n"))
    def regla_109(self):
        self.declare(Fact(resultado="The Wolf Among Us"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="n", Genre_Casual="s", Genre_Estrategia="s"))
    def regla_110(self):
        self.declare(Fact(resultado="Planet Coaster"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="s", Genre_Estrategia="n", Genre_Carreras="n"))
    def regla_111(self):
        self.declare(Fact(resultado="NARUTO SHIPPUDEN: Ultimate Ninja STORM 3 Full Burst HD"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="s", Genre_Estrategia="n", Genre_Carreras="s"))
    def regla_112(self):
        self.declare(Fact(resultado="Need for Speedâ¢ Most Wanted"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="n", Genre_Accion="s", Is_PVP="s", Genre_Estrategia="s"))
    def regla_113(self):
        self.declare(Fact(resultado="BATTLETECH"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="s", Genre_Accion="n"))
    def regla_114(self):
        self.declare(Fact(resultado="Pathfinder: Kingmaker â Enhanced Plus Edition"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="s", Genre_Accion="s", Genre_Simuladores="n", Gano_GOTY="n"))
    def regla_115(self):
        self.declare(Fact(resultado="Atomic Heart"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="s", Genre_Accion="s", Genre_Simuladores="n", Gano_GOTY="s"))
    def regla_116(self):
        self.declare(Fact(resultado="God of War"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="s", Genre_Accion="s", Genre_Simuladores="s", Genre_Estrategia="n"))
    def regla_117(self):
        self.declare(Fact(resultado="EVERSPACEâ¢ 2"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="n", Un_jugador="s", Genre_Rol="s", Genre_Accion="s", Genre_Simuladores="s", Genre_Estrategia="s"))
    def regla_118(self):
        self.declare(Fact(resultado="SPOREâ¢"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="n", Genre_Casual="n", Genre_Estrategia="n", Mixed="n"))
    def regla_119(self):
        self.declare(Fact(resultado="Antichamber"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="n", Genre_Casual="n", Genre_Estrategia="n", Mixed="s"))
    def regla_120(self):
        self.declare(Fact(resultado="A Hat in Time"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="n", Genre_Casual="n", Genre_Estrategia="s"))
    def regla_121(self):
        self.declare(Fact(resultado="Beholder"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="n", Genre_Casual="s", Multijugador="n"))
    def regla_122(self):
        self.declare(Fact(resultado="Coffee Talk"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="n", Genre_Casual="s", Multijugador="s"))
    def regla_123(self):
        self.declare(Fact(resultado="We Were Here Together"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="s", Un_jugador="n", Genre_Estrategia="n"))
    def regla_124(self):
        self.declare(Fact(resultado="SpiritfarerÂ®: EdiciÃ³n Farewell"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="s", Un_jugador="n", Genre_Estrategia="s"))
    def regla_125(self):
        self.declare(Fact(resultado="Satisfactory"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="s", Un_jugador="s", Genre_Casual="n"))
    def regla_126(self):
        self.declare(Fact(resultado="Don't Starve"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="n", Genre_Simuladores="s", Un_jugador="s", Genre_Casual="s"))
    def regla_127(self):
        self.declare(Fact(resultado="ABZU"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="n", Genre_Estrategia="n", Mixed="n"))
    def regla_128(self):
        self.declare(Fact(resultado="Temtem"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="n", Genre_Estrategia="n", Mixed="s", Genre_Casual="n"))
    def regla_129(self):
        self.declare(Fact(resultado="Sea of Stars"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="n", Genre_Estrategia="n", Mixed="s", Genre_Casual="s"))
    def regla_130(self):
        self.declare(Fact(resultado="My Time at Sandrock"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="n", Genre_Estrategia="s", Is_PVP="n"))
    def regla_131(self):
        self.declare(Fact(resultado="Divinity: Original Sin - Enhanced Edition"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="n", Genre_Estrategia="s", Is_PVP="s"))
    def regla_132(self):
        self.declare(Fact(resultado="For The King"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="s", Genre_Estrategia="n", Genre_Simuladores="n", Genre_Casual="n"))
    def regla_133(self):
        self.declare(Fact(resultado="Cloudpunk"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="s", Genre_Estrategia="n", Genre_Simuladores="n", Genre_Casual="s"))
    def regla_134(self):
        self.declare(Fact(resultado="Impostor Factory"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="s", Genre_Estrategia="n", Genre_Simuladores="s"))
    def regla_135(self):
        self.declare(Fact(resultado="Graveyard Keeper"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="s", Genre_Estrategia="s", Is_PVP="n"))
    def regla_136(self):
        self.declare(Fact(resultado="Shadowrun Returns"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="n", Genre_Rol="s", Un_jugador="s", Genre_Estrategia="s", Is_PVP="s"))
    def regla_137(self):
        self.declare(Fact(resultado="Armello"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="n", Is_PVP="n", Genre_Simuladores="n", Genre_Casual="n"))
    def regla_138(self):
        self.declare(Fact(resultado="Aragami"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="n", Is_PVP="n", Genre_Simuladores="n", Genre_Casual="s"))
    def regla_139(self):
        self.declare(Fact(resultado="Teenage Mutant Ninja Turtles: Shredder's Revenge"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="n", Is_PVP="n", Genre_Simuladores="s", Genre_Deportes="n"))
    def regla_140(self):
        self.declare(Fact(resultado="Green Hell"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="n", Is_PVP="n", Genre_Simuladores="s", Genre_Deportes="s"))
    def regla_141(self):
        self.declare(Fact(resultado="Skater XL - The Ultimate Skateboarding Game"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="n", Is_PVP="s", Genre_Casual="n"))
    def regla_142(self):
        self.declare(Fact(resultado="Absolver"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="n", Is_PVP="s", Genre_Casual="s"))
    def regla_143(self):
        self.declare(Fact(resultado="BattleBlock TheaterÂ®"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="n", Genre_Simuladores="n", Genre_Multijugador_masivo="n"))
    def regla_144(self):
        self.declare(Fact(resultado="Grim Dawn"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="n", Genre_Simuladores="n", Genre_Multijugador_masivo="s"))
    def regla_145(self):
        self.declare(Fact(resultado="ARK: Survival Evolved"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="n", Genre_Simuladores="s", Genre_Estrategia="n"))
    def regla_146(self):
        self.declare(Fact(resultado="Medieval Dynasty"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="n", Genre_Simuladores="s", Genre_Estrategia="s"))
    def regla_147(self):
        self.declare(Fact(resultado="The Riftbreaker"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="s", Genre_Multijugador_masivo="n", Genre_Estrategia="n"))
    def regla_148(self):
        self.declare(Fact(resultado="Hyper Light Drifter"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="s", Genre_Multijugador_masivo="n", Genre_Estrategia="s"))
    def regla_149(self):
        self.declare(Fact(resultado="Don't Starve Together"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="n", Genre_Rol="s", Is_PVP="s", Genre_Multijugador_masivo="s"))
    def regla_150(self):
        self.declare(Fact(resultado="Rust"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="n", Genre_Simuladores="n", Is_PVP="n"))
    def regla_151(self):
        self.declare(Fact(resultado="ANIMAL WELL"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="n", Genre_Simuladores="n", Is_PVP="s"))
    def regla_152(self):
        self.declare(Fact(resultado="Black Mesa"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="n", Genre_Simuladores="s", Genre_Estrategia="n"))
    def regla_153(self):
        self.declare(Fact(resultado="BONEWORKS"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="n", Genre_Simuladores="s", Genre_Estrategia="s"))
    def regla_154(self):
        self.declare(Fact(resultado="The Escapists"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="s", Genre_Estrategia="n", Genre_Simuladores="n", Genre_Casual="n"))
    def regla_155(self):
        self.declare(Fact(resultado="CrossCode"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="s", Genre_Estrategia="n", Genre_Simuladores="n", Genre_Casual="s"))
    def regla_156(self):
        self.declare(Fact(resultado="Book of Demons"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="s", Genre_Estrategia="n", Genre_Simuladores="s"))
    def regla_157(self):
        self.declare(Fact(resultado="Chernobylite Complete Edition"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="s", Genre_Estrategia="s", Is_PVP="n"))
    def regla_158(self):
        self.declare(Fact(resultado="Pathfinder: Wrath of the Righteous - Enhanced Edition"))

    @Rule(Juego(Genre_Aventura="s", Genre_Indie="s", Genre_Accion="s", Un_jugador="s", Genre_Rol="s", Genre_Estrategia="s", Is_PVP="s"))
    def regla_159(self):
        self.declare(Fact(resultado="Monster Sanctuary"))


    @Rule(Fact(resultado=MATCH.juego))
    def mostrar(self, juego):
        print(f"\n El juego es: → {juego} ← ;)")


def obtener_respuesta(pregunta):
    ans = input(pregunta + " (s/n): ").strip().lower()
    while ans not in ["s", "n"]:
        ans = input("Responde solo con 's' o 'n': ").strip().lower()
    return ans


if __name__ == "__main__":
    print("Sistema Experto | O'Dimm")
    print("Piensa en un videojuego y responde las preguntas\n")

    preguntas = {}
    preguntas["Is_free"] = obtener_respuesta("¿El juego tiene Is free?")
    preguntas["Is_PVP"] = obtener_respuesta("¿El juego tiene Is PVP?")
    preguntas["Gano_GOTY"] = obtener_respuesta("¿El juego tiene Gano GOTY?")
    preguntas["Genre_Accion"] = obtener_respuesta("¿El juego tiene género Accion?")
    preguntas["Genre_Aventura"] = obtener_respuesta("¿El juego tiene género Aventura?")
    preguntas["Genre_Carreras"] = obtener_respuesta("¿El juego tiene género Carreras?")
    preguntas["Genre_Casual"] = obtener_respuesta("¿El juego tiene género Casual?")
    preguntas["Genre_Deportes"] = obtener_respuesta("¿El juego tiene género Deportes?")
    preguntas["Genre_Estrategia"] = obtener_respuesta("¿El juego tiene género Estrategia?")
    preguntas["Genre_Indie"] = obtener_respuesta("¿El juego tiene género Indie?")
    preguntas["Mixed"] = obtener_respuesta("¿El juego tiene Mixed?")
    preguntas["Multijugador"] = obtener_respuesta("¿El juego tiene Multijugador?")
    preguntas["Un_jugador"] = obtener_respuesta("¿El juego tiene Un jugador?")
    preguntas["Genre_Multijugador_masivo"] = obtener_respuesta("¿El juego tiene género Multijugador masivo?")
    preguntas["Genre_Rol"] = obtener_respuesta("¿El juego tiene género Rol?")
    preguntas["Genre_Simuladores"] = obtener_respuesta("¿El juego tiene género Simuladores?")

    engine = GameExpert()
    engine.reset()
    engine.declare(Juego(**preguntas))
    engine.run()
    print("\nFin del juego")
