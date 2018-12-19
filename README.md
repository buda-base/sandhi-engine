## Presentation 
This sandhi-engine does not hard-code any sandhi rule. 

* First, it parses [sandhi tables](./sanskrit_sandhi_charts/csv) that readily include all the rules, alternatives and exceptions. [Here](./resources/sanskrit_sandhi_charts/readme.md) is how.
* Then, the content of the tables is fed into a [nested structure](./sandhi_rules/readme.md).
* Finally, sandhying any two words becomes as simple as [looking up](./test_sandhi_engine.py#L18) the nested structure using the finals of word one and the initials of word two.  

Since the tables are filled with the result of applying all the sandhi rules, any person with sufficient knowledge in Sanskrit can correct/update/modify the engine, without needing to change anything in the code.

## Components

#### 1. `parse_sandhi_tables.py`
Parses the sandhi tables and fills the nested structure.

#### 2. `find_applicable_sandhis.py`
Looks up the nested structure for all sandhis applicable to a given word's ending.

#### 3. `sandhi_engine.py`
Takes as input two words, filters all the applicable sandhis and outputs the sandhi solutions.

#### 4. `test_sandhi_engine.py`
Tests all the [sandhi examples](https://ubcsanskrit.ca/lesson3/sandhirules.html) from UBC website and more.

## Acknowledgements:

The content of `UBC_sandhi_charts.odt` has has been taken from [UBC website](https://ubcsanskrit.ca/lesson3/sandhicharts.html), in turn taken from  Dr. Ashok Aklujkar's "Sanskrit: An Easy Introduction to an Enchanting Language", (Svādhyāya: 2005) Vol. 1B pp. 64-66.
