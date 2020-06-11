import json
from appyter.fields import Field

class ExpandableTextAreaList(Field):
  def __init__(self):
    super().__init__(self)

  @property
  def raw_value(self):
    return json.loads(self.args['value'])
  
  def constraint(self):
    ''' Ensure we have something of the form:
    [
      ["a", "b", "c"],
      ["d", "e", "f"],
    ]
    '''
    assert type(self.raw_value) == list
    for s in self.raw_value:
      assert type(s) == list
      for el in s:
        assert type(el) == str
