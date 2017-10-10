# Structure of [Sanskrit Rules](./sanskrit_rules.json)

 * vowel_sandhi : `{final: [(initial, sandhied), ...], ...}` [1] 
 * consonant_sandhi_1: `{final: [(initial, (new_final, new_initial)), ...], ...}`
 * consonant_sandhi_2: `{final: [(initial, new_final), ...], ...}` [2]
 * consonant_sandhi_1_vowels: `{finals: [(initial, new_second_final+new_final), ...], ...}` [3]
 * visarga_sandhi_1: `{finals: [(initial, new_second_final+new_final), ...], ...}`
 * visarga_sandhi_2: `{finals: [(initial, new_second_final+new_final), ...], ...}` [3]
 * absolute_finals_sandhi: `{final: [(empty_string, new_final), ...], ...}`
 * cC_words_sandhi: `{final: [(initial, new_final), ...], ...}` [4]
 * punar_sandhi: `{final: [(initial, new_final), ...], ...}` [2]

Notes:

 - [1] for i I u U, the application of these rules only when the form is not a dual has no incidence in the need to generate all sandhied forms here
 - [2] the initial consonant is unchanged
 - [3] `new_second_final+new_final` replaces the last two caracters of the previous word while the initial is unchanged
 - [4] the final consonant is unchanged

