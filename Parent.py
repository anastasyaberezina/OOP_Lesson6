class Parent:
    
    def add_parents(self, parent_one, parent_two):
            self.family['parent'].append(parent_one)
            if parent_one not in parent_two.family['spouse']:
                parent_two.family['spouse'].append(parent_one)
            self.family['parent'].append(parent_two)
            if parent_two not in parent_one.family['spouse']:
                parent_one.family['spouse'].append(parent_two)

            parent_one.add_children(self)
            parent_two.add_children(self)

            self.add_siblings(parent_one, parent_two)

            if parent_one not in self.family['ancestor']:
                self.family['ancestor'].append(parent_one)
            for ancestor in parent_one.family['ancestor']:
                if ancestor not in self.family['ancestor']:
                    self.family['ancestor'].append(ancestor)

            if parent_two not in self.family['ancestor']:
                self.family['ancestor'].append(parent_two)
            for ancestor in parent_two.family['ancestor']:
                if ancestor not in self.family['ancestor']:
                    self.family['ancestor'].append(ancestor)

            self.add_cousins(parent_one, parent_two)

def add_children(self, child):
        self.family['children'].append(child)