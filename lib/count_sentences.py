import re
class MyString:

  def __init__(self, value = ""):
    self.value = value

  @property
  def value(self):
    return self._value 
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return True if self._value.endswith('.') else False
  
  def is_question(self):
    return True if self._value.endswith('?') else False
  
  def is_exclamation(self):
    return True if self._value.endswith('!') else False
  
  def count_sentences(self):
        cleaned_value = re.sub(r'[.!?]+', '.', self._value)
        sentences = cleaned_value.split('.')
        non_empty_sentences = [sentence for sentence in sentences if sentence]

        return len(non_empty_sentences)
