def get_num_words(text):
  words = text.split()
  num_words = len(words)
  return num_words

def get_character_counts(text):
  count = {}
  lowercase_text = text.lower()
  for c in lowercase_text:
    if c in count:
      count[c] += 1
    else:
      count[c] = 1
  return count

def ordered_character_list(count_dict):
  c_list = []
  for c in count_dict:
    if c.isalpha():
      c_list.append({
        "character": c,
        "num": count_dict[c]
      })

  def sort_on(count_dict):
    return count_dict["num"]

  c_list.sort(reverse=True, key=sort_on)
  return c_list