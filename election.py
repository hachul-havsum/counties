import json

class Election(object):
    @staticmethod
    def _calculate_county(record):
        total_votes = record["votes"]
        results = { k:v/total_votes for k,v in record["results"].items() }
        return results

    @staticmethod
    def _xform_db(db):
        new_db = {}
        for state in db:
            state_name = state["state_slug"].title().replace("-"," ")

            counties = {}
            for county in state["counties"]:
                results = Election._calculate_county(county)
                counties[county["name"].replace("-"," ")] = results

            new_db[state_name] = counties

        return new_db

    def __init__(self,filename,good, bad):
        self.db = json.loads(open(filename).read())
        self.xdb = Election._xform_db(self.db)
        self.good = good
        self.bad = bad

    def goodbad(self, state, county):
        """returns a tuple of the total percentages won by the good and the bad"""
        good, bad = 0.0, 0.0
        for candidate, result in self.xdb[state][county].items():
            if candidate in self.good:
                good += result
            if candidate in self.bad:
                bad += result
        return good, bad

    def __repr__(self):
        return "Election (Like:%s, Hate:%s)" % (self.good, self.bad)

class Election2016(Election):
    def __init__(self):
        super(Election2016, self).__init__("nyt_data2.json",
                                           good = ["trumpd"],
                                           bad=["clintonh"])

if __name__ == "__main__":
    e = Election2016()
