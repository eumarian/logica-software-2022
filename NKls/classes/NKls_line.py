class NKlsLine:

    def __init__(self, system, formula, source_type, base_lines=[], source_rule=None, source_lines=[]):
        self.system = None
        self.formula = None
        self.source_type = 'assumption'
        self.source_rule = None
        self.source_lines = []
        self.base_lines = []

        self.system = system
        self.system.lines.append(self)

        self.formula = formula
        if source_type in ['assumption', 'premise', 'rule']:
            self.source_rule = source_rule
            self.source_lines = source_lines
            self.base_lines = base_lines

        if len(self.base_lines) == 0:
            self.base_lines = [self.line_number()]


    def line_number(self, from1=False):
        add = 1 if from1 else 0

        # k = find_key de vazut array_search
        k = 0
        for line in self.system.lines:
            if line == self:
                break
            k += 1

        ret = k + add
        return ret

    def line_formula(self, from1=False):
        return self.formula.string()

    def base_lines(self):
        return self.base_lines

    def line_base_lines(self):
        news = []
        for bl in self.base_lines:
            news.append(bl + 1)

        return ', '.join(news)

    def line_source_info(self):
        ret = 'As'
        if self.source_type == 'premise':
            ret = 'Pr'
        elif self.source_type == 'rule':
            news = []
            for bl in self.source_lines:
                news.append(bl + 1)
            ret = self.source_rule.rule_short() + ' ' + ', '.join(news)

        return ret
