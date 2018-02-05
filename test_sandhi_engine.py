# encoding: utf-8
import unittest
from sandhi_engine import SandhiEngine


engine = SandhiEngine('sanskrit')


class Test(unittest.TestCase):
    """
    Tests all the sandhi examples given on the UBC website
    Note: there might be more than one found sandhi,
          only the presence of "expected" is tested in "found" (the list of possible sandhi solutions)
    """
    def bugfix1(self):
        word1, word2, expected = 'niH', 'Ikzina', 'nir Ikzina'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def bugfix2(self):
        word1, word2, expected = 'tattva', 'Ikzina', 'tattvekzina'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # ~C V~
    def test_1(self):
        word1, word2, expected = 'tat', 'eva', 'tad eva'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    #   ~V C~
    def test_2(self):
        word1, word2, expected = 'samyak', 'asti', 'samyag asti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # ~V V~
    def test_3(self):
        word1, word2, expected = 'rAmasya', 'CAtraH', 'rAmasya cCAtraH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # homorganic vowels
    def test_4(self):
        word1, word2, expected = 'mA', 'astu', 'mAstu'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_5(self):
        word1, word2, expected = 'gacCati', 'iti', 'gacCatIti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_6(self):
        word1, word2, expected = 'guru', 'upeti', 'gurUpeti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # guṇation
    def test_7(self):
        word1, word2, expected = 'na', 'iti', 'neti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_8(self):
        word1, word2, expected = 'rAmeRa', 'uktaH', 'rAmeRoktaH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_9(self):
        word1, word2, expected = 'mahA', 'fziH', 'maharziH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # vṛddhization
    def test_10(self):
        word1, word2, expected = 'na', 'eti', 'nEti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_11(self):
        word1, word2, expected = 'mahA', 'ozaDiH', 'mahOzaDiH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_12(self):
        word1, word2, expected = 'rAmasya', 'Ekyam', 'rAmasyEkyam'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # semivowels
    def test_13(self):
        word1, word2, expected = 'iti', 'uvAca', 'ityuvAca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_14(self):
        word1, word2, expected = 'devI', 'asti', 'devyasti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_15(self):
        word1, word2, expected = 'devI', 'AgacCati', 'devyAgacCati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_16(self):
        word1, word2, expected = 'kuru', 'adya', 'kurvadya'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_17(self):
        word1, word2, expected = 'bahu', 'iti', 'bahviti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_18(self):
        word1, word2, expected = 'maDu', 'admi', 'maDvadmi'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_19(self):
        word1, word2, expected = 'guru', 'Asanam', 'gurvAsanam'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # guṇa vowels
    def test_20(self):
        word1, word2, expected = "te", "api", "te 'pi"
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_21(self):
        word1, word2, expected = 'te', 'uvAca', 'ta uvAca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_22(self):
        word1, word2, expected = 'gfhe', 'uta', 'gfha uta'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # vṛḍdhi vowels
    def test_23(self):
        word1, word2, expected = 'SriyE', 'arTaH', 'SriyA arTaH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_24(self):
        word1, word2, expected = 'uBO', 'uvAca', 'uBAvuvAca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Final: non-palatal stops'
    # the space stands for an empty string triggering the final sandhi.
    def test_25(self):
        word1, word2, expected = 'anuzwuB', '', 'anuzwup'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_26(self):
        word1, word2, expected = 'suhfd', '', 'suhft'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Final: palatal stops
    def test_27(self):
        word1, word2, expected = 'vAc', '', 'vAk'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_28(self):
        word1, word2, expected = 'virAj', '', 'virAw'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_29(self):
        word1, word2, expected = 'diS', '', 'dik'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Final: nasals'
    def test_30(self):
        word1, word2, expected = 'pustakam', '', 'pustakam'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_31(self):
        word1, word2, expected = 'karman', '', 'karman'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Final: s and r
    def test_32(self):
        word1, word2, expected = 'tapas', '', 'tapaH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_33(self):
        word1, word2, expected = 'pitar', '', 'pitaH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Final: consonant clusters
    def test_34(self):
        word1, word2, expected = 'bhavant', '', 'bhavan'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_35(self):
        word1, word2, expected = 'bhavantkgtrnp', '', 'bhavan'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # final dentals
    def test_36(self):
        word1, word2, expected = 'Bavat', 'janma', 'Bavaj janma'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_37(self):
        word1, word2, expected = 'etat', 'Danam', 'etad Danam'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_38(self):
        word1, word2, expected = 'Bavat', 'deham', 'Bavad deham'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_39(self):
        word1, word2, expected = 'tat', 'Saram', 'tac Caram'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # final m
    def test_40(self):
        word1, word2, expected = 'pustakam', 'paWati', 'pustakaM paWati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_41(self):
        word1, word2, expected = 'vanam', 'gacCAmi', 'vanaM gacCAmi'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # final n
    def test_42(self):
        word1, word2, expected = 'mahAn', 'qamaraH', 'mahAR qamaraH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_43(self):
        word1, word2, expected = 'etAn', 'cCAtraH', 'etAMS cCAtraH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_44(self):
        word1, word2, expected = 'gacCan', 'ca', 'gacCaMS ca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_45(self):
        word1, word2, expected = 'tAn', 'tAn', 'tAMs tAn'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_46(self):
        # etAn gacCati changed to cCatraH (n+g = n g following table)
        word1, word2, expected = 'asmin', 'wIkA', 'asmiMz wIkA'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # before l
    def test_47(self):
        word1, word2, expected = 'tat', 'lokaH', 'tal lokaH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_48(self):
        word1, word2, expected = 'tAn', 'lokAn', 'tAl~ lokAn'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # before h
    def test_49(self):
        word1, word2, expected = 'vAk', 'hi', 'vAg Gi'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_50(self):
        word1, word2, expected = 'tat', 'hi', 'tad Di'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # -aḥ sandhi
    def test_51(self):
        word1, word2, expected = 'rAmaH', 'gacCati', 'rAmo gacCati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_52(self):
        word1, word2, expected = "rAmaH", "asti", "rAmo 'sti"
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_53(self):
        word1, word2, expected = 'rAmaH', 'karoti', 'rAmaH karoti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_54(self):
        word1, word2, expected = 'rAmaH', 'calati', 'rAmaS calati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_55(self):
        word1, word2, expected = 'rAmaH', 'wIkAm', 'rAmaz wIkAm'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_56(self):
        word1, word2, expected = 'rAmaH', 'tu', 'rAmas tu'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_57(self):
        word1, word2, expected = 'rAmaH', 'patati', 'rAmaH patati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_58(self):
        word1, word2, expected = 'rAmaH', 'uvAca', 'rAma uvAca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # -āḥ sandhi
    def test_59(self):
        word1, word2, expected = 'devAH', 'vadanti', 'devA vadanti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_60(self):
        word1, word2, expected = 'devAH', 'eva', 'devA eva'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_61(self):
        word1, word2, expected = 'devAH', 'kurvanti', 'devAH kurvanti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_62(self):
        word1, word2, expected = 'devAH', 'patanti', 'devAH patanti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_63(self):
        word1, word2, expected = 'devAH', 'ca', 'devAS ca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_64(self):
        word1, word2, expected = 'devAH', 'wIkA', 'devAz wIkA'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_65(self):
        word1, word2, expected = 'devAH', 'tu', 'devAs tu'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # -iḥ -īḥ -uḥ -ūḥ -eḥ -oḥ -aiḥ -auḥ
    def test_66(self):
        word1, word2, expected = 'muniH', 'vadati', 'munir vadati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_67(self):
        word1, word2, expected = 'tEH', 'uktam', 'tEr uktam'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_68(self):
        word1, word2, expected = 'BUH', 'Buvas', 'BUr Buvas'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_69(self):
        word1, word2, expected = 'muniH', 'karoti', 'muniH karoti'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_70(self):
        word1, word2, expected = 'agniH', 'ca', 'agniS ca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_71(self):
        word1, word2, expected = 'muneH', 'wIkAm', 'munez wIkAm'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_72(self):
        word1, word2, expected = 'tEH', 'tu', 'tEs tu'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_73(self):
        word1, word2, expected = 'guruH', 'patati', 'guruH patati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Exception: punar
    def test_74(self):
        word1, word2, expected = 'punar', 'punar', 'punaH punar'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_75(self):
        word1, word2, expected = 'punar', 'milAmaH', 'punar milAmaH'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_76(self):
        word1, word2, expected = 'punar', 'ramati', 'punaH ramati'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_77(self):
        word1, word2, expected = 'punar', 'uvAca', 'punar uvAca'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    # Special test_s from the tables
    def test_78(self):
        word1, word2, expected = 'wordi', 'aword', 'wordyaword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_79(self):
        word1, word2, expected = 'wordI', 'aword', 'wordyaword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_80(self):
        word1, word2, expected = 'wordu', 'aword', 'wordvaword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_81(self):
        word1, word2, expected = 'wordU', 'aword', 'wordvaword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_82(self):
        word1, word2, expected = "worde", "aword", "worde 'word"
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_83(self):
        word1, word2, expected = 'wordo', 'Aword', 'wordavAword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_84(self):
        word1, word2, expected = 'wordaN', 'aword', 'wordaNN aword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_85(self):
        word1, word2, expected = 'wordAN', 'aword', 'wordAN aword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_86(self):
        word1, word2, expected = 'wordan', 'aword', 'wordann aword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_87(self):
        word1, word2, expected = 'wordAn', 'aword', 'wordAn aword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_88(self):
        word1, word2, expected = 'wordn', 'Sword', 'wordY Sword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_89(self):
        word1, word2, expected = "wordaH", "aword", "wordo 'word"
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_90(self):
        word1, word2, expected = 'wordaH', 'oword', 'worda oword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_91(self):
        word1, word2, expected = 'wordiH', 'aword', 'wordir aword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_92(self):
        word1, word2, expected = 'wordiH', 'rword', 'wordI rword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_93(self):
        word1, word2, expected = 'wordUH', 'rword', 'wordU rword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_94(self):
        word1, word2, expected = 'wordaH', 'gword', 'wordo gword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_95(self):
        word1, word2, expected = 'wordaH', 'cword', 'wordaS cword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_96(self):
        word1, word2, expected = 'wordAH', 'gword', 'wordA gword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_97(self):
        word1, word2, expected = 'wordAH', 'cword', 'wordAS cword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_98(self):
        word1, word2, expected = 'wordiH', 'gword', 'wordir gword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)

    def test_99(self):
        word1, word2, expected = 'wordiH', 'cword', 'wordiS cword'
        found = engine.apply_sandhi(word1, word2)
        self.assertIn(expected, found)


if __name__ == '__main__':
    unittest.main()
