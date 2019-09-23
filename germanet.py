import os
import time
import logging
from collections import defaultdict
import progressbar
from utils import parse_xml
from synsetLoader import load_lexunits
from iliLoader import load_ili
from wictionaryLoader import load_wiktionary
from relationLoader import load_relations


class Germanet:

    def __init__(self, datadir, addiliRecords=True, addWictionary=True):
        # the data directory where all germanet XML files are stored in
        self.datadir = datadir
        self.addiliRecords = addiliRecords
        self.addWictionary = addWictionary

        # lexid 2 lexunit
        self._lexunits = {}

        # synid2synset
        self._synsets = {}

        # orthform2lexids (all variants)
        self._ortform2lexid = defaultdict(set)

        # orthform2lexids (only main form)
        self._mainOrtform2lexid = defaultdict(set)

        # lower cased orthform 2 lexids (all variants)
        self._lowercasedform2lexid = defaultdict(set)

        # wordcategory2synset
        self._wordcat2lexid = defaultdict(set)

        # wordclass2synset
        self._wordclass2lexid = defaultdict(set)

        self._compounds = set()

        # frame2id
        self._frames2id = defaultdict(set)

        self._wiktionary_entries = []
        self._ili_records = []

        self.load_data()

    def get_synsets_by_orthform(self, form, ignorecase=False):
        if ignorecase:
            lexunit_ids = self._lowercasedform2lexid[form.lower()]
        else:
            lexunit_ids = self._ortform2lexid[form]
        return [self._lexunits[id].synset for id in lexunit_ids]

    def get_synsets_by_wordcategory(self, category):
        lexunit_ids = self._wordcat2lexid[category.name]
        return [self._lexunits[id].synset for id in lexunit_ids]

    def get_synsets_by_wordclass(self, wordclass):
        lexunit_ids = self._wordclass2lexid[wordclass.name]
        return [self._lexunits[id].synset for id in lexunit_ids]

    def get_synset_by_id(self, id):
        assert id in self._synsets, "the given synset id is not in GermaNet"
        return self._synsets[id]

    def get_lexunit_by_id(self, id):
        assert id in self._lexunits, "the given lexunit id is not in GermaNet"
        return self._lexunits[id]

    def get_lexunits_by_orthform(self, form, ignorecase=False):
        if ignorecase:
            lexunit_ids = self._lowercasedform2lexid[form.lower()]
            return [self._lexunits[id] for id in lexunit_ids]
        lexunit_ids = self._ortform2lexid[form]
        return [self._lexunits[id] for id in lexunit_ids]

    def get_lexunits_by_wordclass(self, wordclass):
        lexunit_ids = self._wordclass2lexid[wordclass.name]
        return [self._lexunits[id] for id in lexunit_ids]

    def get_lexunits_by_wordcategory(self, category):
        lexunit_ids = self._wordcat2lexid[category.name]
        return [self._lexunits[id] for id in lexunit_ids]

    def get_synsets_by_frame(self, frame):
        synset_ids = self._frames2id[frame]
        return [self._synsets[id] for id in synset_ids]

    def get_number_of_senses(self, lexunits):
        senses = [unit.sense for unit in lexunits]
        return max(senses)

    def load_data(self):
        files = os.listdir(self.datadir)
        wikifiles = [f for f in files if "wiktionary" in f and "xml" in f]
        lexentries = [f for f in files if f.startswith("nomen") or f.startswith("verben") or f.startswith("adj")]
        ilifiles = [f for f in files if "interLingua" in f]

        with progressbar.ProgressBar(max_value=len(files)) as bar:
            counter = 0
            for f in lexentries:
                counter += 1
                tree = parse_xml(self.datadir, f)
                load_lexunits(germanet=self, tree=tree)
                bar.update(counter)
            tree = parse_xml(self.datadir, "gn_relations.xml")
            load_relations(germanet=self, tree=tree)
            if self.addWictionary:
                for f in wikifiles:
                    counter += 1
                    tree = parse_xml(self.datadir, f)
                    load_wiktionary(germanet=self, tree=tree)
                    bar.update(counter)
            if self.addiliRecords:
                for f in ilifiles:
                    counter += 1
                    tree = parse_xml(self.datadir, f)
                    load_ili(germanet=self, tree=tree)
                    bar.update(counter)

    def lexunits(self):
        return self._lexunits

    def synsets(self):
        return self._synsets

    def orthform2lexid(self):
        return self._ortform2lexid

    def main_orthform2lexid(self):
        return self._mainOrtform2lexid

    def lowercasedform2lexid(self):
        return self._lowercasedform2lexid

    def wordcate2lexid(self):
        return self._wordcat2lexid

    def wordclass2lexid(self):
        return self._wordclass2lexid

    def compounds(self):
        return self._compounds

    def frames2id(self):
        return self._frames2id

    def wiktionary_entries(self):
        return self._wiktionary_entries

    def ili_records(self):
        return self._ili_records


if __name__ == '__main__':
    germanet = Germanet('data')
    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(germanet.get_synsets())
    # print(germanet.get_lexunits())
    # print(germanet.get_compounds())
    # jetzt sind die daten geladen.
    # hier ein beispiel für funktionen. sagen wir du hast dein adjektiv 'tief'

    # extrahiere alle synsets zu 'tief'


    Stimme = germanet.get_synset_by_id("s29596")
    Stimmel = germanet._lexunits['l40408']
    print(Stimmel)

    print(Stimme)

    print(Stimme.relations())
    print(Stimme.incoming_relations())
    print(Stimme.direct_hypernyms())
    print(Stimme.direct_hyponyms())
    print(Stimme.all_hypernyms())

    Geräusch = germanet.get_synset_by_id("s40951")
    dackel = germanet.get_synset_by_id('s50944')
    dimension = germanet.get_synset_by_id("s15678")
    steigerung = germanet.get_synset_by_id("s22278")
    lokalisation = germanet.get_synset_by_id("s96965")
    knapp = germanet.get_synset_by_id("s5400")
    Stunde = germanet.get_synset_by_id("s51491")
    zeit = germanet.get_synset_by_id("s51002")
    kommunikation = germanet.get_synset_by_id("s29596")
    kommmittel = germanet.get_synset_by_id("s29473")

    # for p in hypernympaths:
    # print(p)