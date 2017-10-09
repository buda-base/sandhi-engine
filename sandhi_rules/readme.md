# Structure of Sanskrit Rules

* vowel_sandhi: `{final: [(initial, sandhied), ...], ...}`

Note: for i I u U, the application of these rules only when the form is not a dual has no incidence in the need to generate all sandhied forms here 

* consonant_sandhi_1: `{final: [(initial, (new_final, new_initial)), ...], ...}`

* consonant_sandhi_2: `{final: [(initial, new_final), ...], ...}`

Note: the initial consonant is unchanged 

* consonant_sandhi_1_vowels: `{finals: [(initial, new_second_final+new_final), ...], ...}`

Note: `new_second_final+new_final` replace the last two caracters of the previous word while the initial is unchanged

* visarga_sandhi_1: `{finals: [(initial, new_second_final+new_final), ...], ...}`

Note: `new_second_final+new_final` replace the last two caracters of the previous word while the initial is unchanged

* visarga_sandhi_2: `{finals: [(initial, new_second_final+new_final), ...], ...}`

Note: `new_second_final+new_final` replace the last two caracters of the previous word while the initial is unchanged

* absolute_finals_sandhi: `{final: [(empty_string, new_final), ...], ...}`

* cC_words_sandhi: `{final: [(initial, new_final), ...], ...}`

Note: the final consonant is unchanged

* punar_sandhi: `{final: [(initial, new_final), ...], ...}`

Note: the initial consonant is unchanged
